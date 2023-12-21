import uuid
from datetime import datetime, timedelta
from sqlalchemy import DECIMAL, Boolean, Column, DateTime, Enum, ForeignKey, String, ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER
from db.base_class import GUID, Base
from schemas.batch_product import BatchProductSupplier, BatchProductName

class BatchProduct(Base):
    __tablename__ = 'batch_product'

    id = Column(Integer, primary_key=True)
    import_date = Column(DateTime, nullable=False, default=datetime.now)
    supplier = Column(String, Enum(BatchProductSupplier), nullable=False)
    product_name = Column(String, Enum(BatchProductName), nullable=False)
    number_of_cloth = Column(Integer, nullable=False)
    demander = Column(String)
    done_sampling = Column(String, default=False, nullable=False)