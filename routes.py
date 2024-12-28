from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user/')
async def get_user( id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str , db: Session = Depends(get_db)):
    return await service.get_user(db , id, Address, first_name, last_name, age, Email Id)

@router.get('/user/id')
async def get_user_id( id: int , db: Session = Depends(get_db)):
    return await service.get_user_id(db , id)

@router.post('/user/')
async def post_user( id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str , db: Session = Depends(get_db)):
    return await service.post_user(db , id, Address, first_name, last_name, age, Email Id)

@router.put('/user/id/')
async def put_user_id( id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str , db: Session = Depends(get_db)):
    return await service.put_user_id(db , id, Address, first_name, last_name, age, Email Id)

@router.delete('/user/id')
async def delete_user_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_user_id(db , id)

