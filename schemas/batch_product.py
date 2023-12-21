# schemas/order.py
from enum import Enum


class BatchProductSupplier(str, Enum):
    Supplier1 = "companyA"
    Supplier2 = "companyB"
    Supplier3 = "companyC"
    Supplier4 = "companyD"

class BatchProductName(str, Enum):
    PANTSMALE = "pants_male"
    PANTFEMALE = "pants_female"
    COATLONG = "coat_long"
    COATSHORT = "coat_short"

class BatchProductDemander(str, Enum):
    Supplier1 = "branch1"
    Supplier2 = "branch2"
    Supplier3 = "branch3"
    Supplier4 = "branch4"

