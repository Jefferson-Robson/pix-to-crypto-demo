from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models, database
import uuid
import random
import urllib.request
import json

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title="API Soluções de Pagamento")

class QuoteRequest(BaseModel):
    amount_brl: float
    crypto: str

class OrderCreate(BaseModel):
    amount_brl: float
    crypto: str
    address: str

def obter_cotacao_real(crypto_symbol: str) -> float:
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto_symbol.upper()}BRL"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return float(data['price'])
    except Exception as e:
        return {"USDT": 5.10, "BTC": 300000.0}.get(crypto_symbol.upper(), 5.10)

@app.post("/api/quote")
def simulate_quote(request: QuoteRequest):
    price = obter_cotacao_real(request.crypto)
    crypto_amount = request.amount_brl / price
    return {
        "fiat_amount_brl": request.amount_brl,
        "crypto_asset": request.crypto.upper(),
        "estimated_crypto": round(crypto_amount, 6),
        "exchange_rate": round(price, 2)
    }

@app.post("/api/orders")
def create_order(order: OrderCreate, db: Session = Depends(database.get_db)):
    new_order = models.Order(
        order_code=f"ORD-{random.randint(10000, 99999)}",
        fiat_amount_brl=order.amount_brl,
        crypto_asset=order.crypto,
        crypto_address=order.address
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.post("/api/orders/{order_code}/pay")
def simulate_payment(order_code: str, db: Session = Depends(database.get_db)):
    order = db.query(models.Order).filter(models.Order.order_code == order_code).first()
    if not order:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    
    order.pix_status = "PAID"
    order.conversion_status = "DONE"
    order.tx_hash = f"0x{uuid.uuid4().hex}"
    db.commit()
    db.refresh(order)
    return order

@app.get("/api/orders")
def list_orders(db: Session = Depends(database.get_db)):
    return db.query(models.Order).order_by(models.Order.created_at.desc()).all()
