該專案為系統分析與設計課程中的期末專案，要針對假貨問題進行mis方案設計
我們利用一個產銷系統的概念，去紀錄產品的供應商和利用系統進行抽樣輔助，
包含但不限於利用設定好的抽樣設計，在商品記錄到系統中時，
就自動標記哪些商品需要被抽樣。

舉例來說，若有一批jean_male進貨，他被分配到一個batch_number批號，而這批貨裡面有五十件商品(也就是batch_product這個table)
每個商品也會被自動賦予獨一的uuid，並標記上是否需要抽樣。(也就是item這個table)
當該批的五十件商品都顯示不用抽樣或已抽樣，則整批貨會自動被標記可以出貨。(確認item.status後，系統自動修正batch_product.done_sampling)

database design:

batch_product:
| id | |import_date| | supplier | | product_name | | number_of_cloth | | demander | | done_sampling |
  16    2023-12-19     companyA     jean_male              50             null           0(false)

item:
| id | | cloth_uuid |       | batch_number | | status | | inspectors | | sampling_date |
  225   6a3ad91e-929c-4a           16       no_sampling      Andy             null
       4a-af18-3ffb21ffd2f4

...隱藏49條商品

Tech Stack
前端：gradio
language: python
db: MYSQL database by xammp
db_operate: sqlalchemy
db_driver: pymysql(一個用於 Python 連接 MySQL 資料庫的驅動)




