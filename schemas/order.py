from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
    id: Optional[int]
    date: datetime = datetime.now()
    phone: str
    prepayment: Optional[str]