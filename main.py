import requests

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, insert,update, delete
import uvicorn

from database import engine
from models import User
from payer.cryptocloud import create_invoce, check_invoce

from pydantic import BaseModel
from typing import Optional

import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
SHOP_ID = os.getenv('SHOP_ID')
SECRET_KEY = os.getenv('SECRET_KEY')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Users(BaseModel):
    id: int
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    username: Optional[str] = None 
    email: Optional[str] = None 
    wallet: Optional[str] = None 
    balance: Optional[str] = None 
    pincode: Optional[int] = None 
    boolpin: bool
    tg_id: Optional[str] = None # id телеграма
    referal: bool # является ли рефералом
    whoreferal: Optional[str] = None # id человека кто привел этого пользователя
    visibility_balance: bool # видимость баланса

class NewUser(BaseModel):
    first_name: Optional[str] = None 
    last_name: Optional[str] = None
    username: Optional[str] = None 
    email: Optional[str] = None 
    wallet: Optional[str] = None 
    balance: Optional[str] = None 
    pincode: Optional[str] = None 
    boolpin: bool = False
    tg_id: Optional[str] = None # id телеграма
    referal: bool = False # является ли рефералом
    whoreferal: Optional[str] = None # id человека кто привел этого пользователя
    visibility_balance: bool = True # видимость баланса

# Модели для обновления данных
class UpdateBalance(BaseModel):
    balance: str

class UpdatePincode(BaseModel):
    pincode: int

class UpdateEmail(BaseModel):
    email: str

class CreateInvoce(BaseModel):
    amount: Optional[int] = 5 
    cryptocurrency: Optional[str] = "USDT_TRC20"


# class TakeUser(BaseModel):
#     pass

@app.get("/all")
async def all_users() -> list[Users]: #dict:#
    async with engine.connect() as conn:
        print('Подключились!!!')
        result = await conn.execute(select(User).select_from(User))        
        return [
            Users(
                id=data.id,
                first_name=data.first_name,
                last_name=data.last_name,
                username=data.username,
                email=data.email,
                wallet=data.wallet,
                balance=data.balance,
                pincode=data.pincode,
                boolpin=data.boolpin,
                tg_id = data.tg_id,
                referal = data.referal,
                whoreferal = data.whoreferal,
                visibility_balance = data.visibility_balance
            )
            for data in result.mappings().all()
        ]
        



@app.post("/new_user", status_code=201)
async def new_user(user: NewUser):
    async with engine.begin() as conn:
        # Проверяем существование пользователя по email
        check_query = select(User).where(User.email == user.email)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="email уже есть"
            )
        
        # Проверяем существование пользователя по username
        check_query = select(User).where(User.username == user.username)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username уже есть!"
            )

        # Если пользователя нет - создаем
        await conn.execute(
            insert(User).values(
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
                wallet=user.wallet,
                balance=user.balance,
                pincode=user.pincode,
                boolpin=user.boolpin,
                tg_id = user.tg_id,
                referal = user.referal,
                whoreferal = user.whoreferal,
                visibility_balance = user.visibility_balance
            )
        )
        
    return {"message": "User created successfully"}

@app.delete("/delete_user/{tg_id}")
async def delete_user(tg_id: str):
    async with engine.begin() as conn:
        # Проверяем существование пользователя
        check_query = select(User).where(User.tg_id == tg_id)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        # Удаляем пользователя
        delete_query = delete(User).where(User.tg_id == tg_id)
        await conn.execute(delete_query)
        
    return {"message": "User deleted successfully"}

@app.delete("/delete_user_email/{email}")
async def delete_use_by_mail(email: str):
    async with engine.begin() as conn:
        # Проверяем существование пользователя
        check_query = select(User).where(User.email == email)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        # Удаляем пользователя
        delete_query = delete(User).where(User.email == email)
        await conn.execute(delete_query)
        
    return {"message": "User deleted successfully"}

@app.get("/user/{tg_id}")
async def get_user_by_tgid(tg_id: str) -> Users:
    async with engine.connect() as conn:
        query = select(User).where(User.tg_id == tg_id)
        result = await conn.execute(query)
        user_data = result.mappings().first()
        
        if not user_data:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
            
        return Users(
            id=user_data.id,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            email=user_data.email,
            wallet=user_data.wallet,
            balance=user_data.balance,
            pincode=user_data.pincode,
            boolpin=user_data.boolpin,
            tg_id=user_data.tg_id,
            referal=user_data.referal,
            whoreferal=user_data.whoreferal,
            visibility_balance=user_data.visibility_balance
        )

@app.patch("/update_balance/{tg_id}")
async def update_user_balance(tg_id: str, update_data: UpdateBalance):
    async with engine.begin() as conn:
        # Проверяем существование пользователя
        check_query = select(User).where(User.tg_id == tg_id)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        # Обновляем баланс
        update_query = (
            update(User)
            .where(User.tg_id == tg_id)
            .values(balance=update_data.balance)
        )
        await conn.execute(update_query)
        
    return {"message": "Balance updated successfully"}

@app.patch("/update_pincode/{tg_id}")
async def update_user_pincode(tg_id: str, update_data: UpdatePincode):
    async with engine.begin() as conn:
        # Проверяем существование пользователя
        check_query = select(User).where(User.tg_id == tg_id)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        # Обновляем пин-код
        update_query = (
            update(User)
            .where(User.tg_id == tg_id)
            .values(pincode=update_data.pincode,
                    boolpin=True)
        )
        
    return {"message": "Pincode updated successfully"}


@app.patch("/update_email/{tg_id}")
async def update_user_email(code_mail: str, tg_id: str, update_data: UpdateEmail):
    async with engine.begin() as conn:
        # Проверяем существование пользователя
        check_query = select(User).where(User.tg_id == tg_id)
        result = await conn.execute(check_query)
        existing_user = result.first()
        
        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="Пользователь не найден"
            )
        
        # Проверяем занятость новой почты
        email_check_query = select(User).where(User.email == update_data.email)
        email_result = await conn.execute(email_check_query)
        if email_result.first():
            raise HTTPException(
                status_code=400,
                detail="Email уже занят другим пользователем"
            )
        
        # Обновляем email
        update_query = (
            update(User)
            .where(User.tg_id == tg_id)
            .values(email=update_data.email)
        )
        await conn.execute(update_query)
        
    return {"message": "Email updated successfully"}


@app.get("/last_price")
async def get_last_price():
    # Подключение к базе данных
    conn = sqlite3.connect('./p2p-course/course_database.db', check_same_thread=False)
    cursor = conn.cursor()
    
    # Запрос для получения последней my_price
    cursor.execute('''
    SELECT my_price 
    FROM course 
    ORDER BY timestamp DESC 
    LIMIT 1
    ''')
    
    result = cursor.fetchone()
    
    # Закрытие соединения
    conn.close()
    
    if result:
        return {"last_price": result[0]}
    else:
        return {"error": "No prices found in database"}


# @app.post("/callback")
# async def get_callback():

@app.post("/create_invoces")
async def create_invoces(data: CreateInvoce):
    create_invoce(API_KEY, SHOP_ID, data.amount, data.cryptocurrency)
    # amount = 105
    # cryptocurrency = "USDT_TRC20"
    # create_invoce(amount, cryptocurrency)

@app.post("/check_invoces")
async def check_invoces():   
    check_invoce()


@app.post("/postback")
async def get_callback(data: dict):  # FastAPI автоматически распарсит JSON
    print("Received data:", data)
    return {"received_data": data}  # Возвращаем данные в ответе

    


if __name__ == "__main__":
    uvicorn.run("main:app", host = '0.0.0.0', port=3030)

