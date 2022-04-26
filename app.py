from fastapi import FastAPI
from routes.order import order

app= FastAPI()

app.include_router(order)