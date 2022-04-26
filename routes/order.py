from fastapi import APIRouter, Response
from config.db import conn
from models.order import orders
from schemas.order import Order
from starlette.status import HTTP_204_NO_CONTENT
order = APIRouter()

@order.get('/orders')
def get_orders():
    return conn.execute(orders.select()).fetchall()

@order.get('/orders/{id}')
def get_order(id: int):
    return conn.execute(orders.select().where(orders.c.id == id)).first()

@order.post('/orders')
def create_order(order: Order):
    new_order = order.dict()
    result = conn.execute(orders.insert().values(new_order))
    print(result.lastrowid)
    return conn.execute(orders.select().where(orders.c.id == result.lastrowid)).first()

@order.delete('/orders/{id}')
def delete_order(id: int):
    conn.execute(orders.delete().where(orders.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@order.put('/orders/{id}')
def update_order(id: int, order: Order):
    conn.execute(orders.update()
                 .values(phone=order.phone, prepayment = order.prepayment)
                 .where(orders.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)