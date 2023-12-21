from operator import and_
from module.batch_product import BatchProduct
from module.item import Item
import random
from db.session import session
from schemas.batch_product import BatchProductSupplier, BatchProductName
from datetime import datetime
import gradio as gr
from sqlalchemy import and_

def create_batch_product_and_items(session, supplier, product_name, number_of_cloth):
    number_of_cloth = int(number_of_cloth) 
    batch_product = BatchProduct(
        supplier=supplier,
        product_name=product_name,
        number_of_cloth=number_of_cloth,
    )
    session.add(batch_product)
    session.commit()

    item_inspector = random.choice(["Andy","Alice"])
    for _ in range(number_of_cloth):
        #item_status = random.choice(["sampling", "no_sampling", "wait_sampling", "unknown"])
        item = Item(
            batch_number=batch_product.id,
            status=random.choice(["sampling", "no_sampling"]),
            inspectors=item_inspector,
            sampling_date=None  
        )
        session.add(item)

    session.commit()

def insert_demander(id_to_update, new_demander):
    id_to_update = id_to_update
    new_demander = new_demander

    # 查找指定的紀錄
    record_to_update = session.query(BatchProduct).filter(BatchProduct.id == id_to_update).first()

    if record_to_update:
    
        # 更新 demander 欄位
        record_to_update.demander = new_demander
    
        # 提交更改到數據庫
        session.commit()
    else:
        print(f"No record with id {id_to_update} found.")


def update_sampling_status_and_date(batch_number_to_update):
    new_sampling_date = datetime.now()

    # Update the Item records from 'need_sampling' to 'done_sampling'
    session.query(Item).filter(
        and_(
            Item.batch_number == batch_number_to_update,
            Item.status == 'sampling'
        )
    ).update({
        Item.status: 'done_sampling',
        Item.sampling_date: new_sampling_date
    }, synchronize_session=False)

    session.commit()

    # Check if all Items in the batch are either 'done_sampling' or 'no_sampling'
    whether_done_sampling(batch_number_to_update)

def whether_done_sampling(batch_number):
    items = session.query(Item).filter(Item.batch_number == batch_number).all()
    all_done_or_no_sampling = all(item.status in ['done_sampling', 'no_sampling'] for item in items)
    
    if all_done_or_no_sampling:
        # Update the 'done_sampling' field in the 'batch_product' table to True
        session.query(BatchProduct).filter(BatchProduct.id == batch_number).update({
            BatchProduct.done_sampling: True
        })
        session.commit()

        print("This batch is done sampling.")
        return True
    else:
        print("This batch is not done sampling.")
        return False

    


"""
batch_product = BatchProduct(
supplier=random.choice(["companyA","companyB","companyC","companyD"]),
product_name=random.choice(["pants_male", "pants_female", "coat_long", "coat_short"]),
number_of_cloth=random.uniform(1000, 30000),
demander=random.choice(["companye","companyf","companyg","companyh"]))
"""

# 使用函數生成 BatchProduct 和 Item

# Gradio 函數包裝器
def gradio_create_batch_product_and_items(supplier, product_name, number_of_cloth):
    # 調用您的 SQLAlchemy 函數
    create_batch_product_and_items(session, supplier, product_name, number_of_cloth)
    return "Batch product and items created successfully!"

update_sampling_status_and_date(16)
whether_done_sampling(16)
#create_batch_product_and_items(session, "companyA", "jean_male", 20)


"""
# 創建 Gradio 介面
iface = gr.Interface(
    fn=gradio_create_batch_product_and_items,
    inputs=[
        gr.Textbox(label="Supplier"),
        gr.Textbox(label="Product Name"),
        gr.Number(label="Number of Cloth", value=1, step=1)
    ],
    outputs="text"
)


if __name__ == '__main__':
    # 運行應用
    app, local_url, share_url = iface.launch(share=True)
    print(f"Running on local URL: {local_url}")
    print(f"To access from another device, use the shareable link: {share_url}")

"""

# 關閉資料庫連接
session.close()
