from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_user(db: Session, id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str):

    user_all = db.query(models.User).all()
    res = {
        'user_all': user_all,
    }
    return res

async def get_user_id(db: Session, id: int):

    user_one = db.query(models.User).filter(models.User.id == id).first()
    res = {
        'user_one': user_one,
    }
    return res

async def post_user(db: Session, id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str):

    record_to_be_added = {'id': id, 'Address': Address, 'first_name': first_name, 'last_name': last_name, 'age': age, 'Email Id': Email Id}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_inserted_record = new_user

    record_to_be_added = {'id': id, 'Address': Address, 'first_name': id, 'last_name': id, 'age': id, 'Email Id': Email Id}
    new_user = models.User(**record_to_be_added)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user = new_user
    res = {
        'user_inserted_record': user_inserted_record,
    }
    return res

async def put_user_id(db: Session, id: str, Address: str, first_name: str, last_name: str, age: str, Email Id: str):

    user_edited_record = db.query(models.User).filter(models.User.id == id).first()
    for key, value in {'id': id, 'Address': Address, 'first_name': first_name, 'last_name': last_name, 'age': age, 'Email Id': Email Id}.items():
          setattr(user_edited_record, key, value)
    db.commit()
    db.refresh(user_edited_record)
    user_edited_record = user_edited_record

    res = {
        'user_edited_record': user_edited_record,
    }
    return res

async def delete_user_id(db: Session, id: int):

    user_deleted = None
    record_to_delete = db.query(models.User).filter(models.User.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          user_deleted = record_to_delete
    res = {
        'user_deleted': user_deleted,
    }
    return res

