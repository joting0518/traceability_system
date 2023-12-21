import uuid
from datetime import datetime, timedelta
from sqlalchemy import DECIMAL, Boolean, Column, DateTime, Enum, ForeignKey, String, ForeignKey, Integer
from sqlalchemy.dialects.mysql import INTEGER
from db.base_class import GUID, Base
from schemas.item import ItemStatus, ItemInspector

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    cloth_uuid = Column(String, default=uuid.uuid4, nullable=False)
    batch_number = Column(String, ForeignKey("batch_product.id"), nullable=False)
    status = Column(String, Enum(ItemStatus),nullable=False)
    inspectors = Column(String, Enum(ItemInspector))
    sampling_date = Column(DateTime)

