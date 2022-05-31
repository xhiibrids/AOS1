from typing import List,Optional
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import bbdd.models as models
import schemas
from bbdd.database import SessionLocal, engine
import crud as crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return "Hello World"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/facturas/{factura_id}")
async def read_item(factura_id: int, q: Optional[str] = None):
    return {"factura_id":factura_id}

@app.post("/clientes/", response_model=schemas.Cliente)
def create_user(user: schemas.Cliente, db: Session = Depends(get_db)):
    db_user = crud.get_Cliente(db, Cliente_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Cliente already registered")
    return crud.create_user(db=db, user=user)

@app.get("/clientes/", response_model=List[schemas.Cliente])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_clients(db, skip=skip, limit=limit)
    return users
    
@app.get("/facturas/", response_model=List[schemas.Factura])
def get_facturas(db: Session = Depends(get_db), skip: int =0, limit: int = 100):
    return crud.get_facturas(db)

@app.get("/facturas/{factura_id}")
def get_facturas_by_id(factura_id:int, db: Session = Depends(get_db)):
    return crud.get_factura_by_id(db,id=factura_id)
@app.get("/facturas/clientes/{cliente_id}")
def get_facturas_by_clienteid(cliente_id: int,db : Session = Depends(get_db)):
    return crud.get_facturas_by_cliente_id(db,cliente_id=cliente_id)

@app.post("/facturas/",response_model=schemas.Factura)
def create_factura(factura: schemas.Factura, db: Session = Depends(get_db)):
    return crud.create_factura(db,factura,id=factura.cliente_id)


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port="8000")