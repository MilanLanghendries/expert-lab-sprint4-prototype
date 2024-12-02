from fastapi import FastAPI
from app import crud, models, schemas, database
from app.router import auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(crud.router)
app.include_router(auth.router)
