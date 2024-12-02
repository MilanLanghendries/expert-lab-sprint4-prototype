from fastapi import FastAPI
from app import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(crud.router)
