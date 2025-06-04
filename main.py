from fastapi import FastAPI
from app.routes import sessions, cart,products

app = FastAPI()
app.include_router(sessions.router)
app.include_router(cart.router)
app.include_router(products.router)
@app.get("/")
def read_root():
    return {"message": "Backend funcionando 🚀"}
