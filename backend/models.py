from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
import uuid
from database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    order_code = Column(String, unique=True, index=True)
    fiat_amount_brl = Column(Float)
    crypto_asset = Column(String)
    crypto_address = Column(String)
    pix_status = Column(String, default="PENDING")
    conversion_status = Column(String, default="WAITING")
    tx_hash = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
