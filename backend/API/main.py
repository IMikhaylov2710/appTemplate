from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.db import database, User, Variant
from typing import Union
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI(title='Backend server for data analysis pipeline')

origins = [
    "http://localhost:3000", 
    "http://172.21.0.4:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return print('hello world')

@app.get("/users/")
async def getUsers():
    return await User.objects.all()

@app.get("/variants/")
async def getVariants():
    return await Variant.objects.all()

@app.get("/variants/{variant_id}")
async def getVariantById(variant_id:int):
    return await Variant.objects.filter(id=variant_id).get()

@app.post("/users/new/")
async def registerNewUser(item:User):
    await User.objects.create(item)

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")
    await Variant.objects.get_or_create(chromosome="2", position=25241123, consequence='Benign', gene='BRCA2', depth=243)
    await Variant.objects.get_or_create(chromosome="1", position=165126523, consequence='Malignant', gene='MAPKAPK', depth=125, exonic=True)

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()