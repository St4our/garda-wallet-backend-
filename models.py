from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column (String, nullable = True)# имя
    last_name = Column (String, nullable = True)# фамилия
    username = Column(String, nullable = True)# тэг
    email = Column(String, nullable = True) # почта
    wallet = Column(String, nullable = True) # номер кошелька
    balance = Column(String, nullable = True) # баланс
    pincode = Column(String, nullable = True) # пинкод
    boolpin = Column(Boolean, default=False, nullable = True) # есть ли код
    tg_id = Column(String, nullable = True) # id телеграма
    referal = Column(Boolean, default=False, nullable = True) # является ли рефералом
    whoreferal = Column(String, nullable = True) # id человека кто привел этого пользователя
    visibility_balance = Column(Boolean, default=True, nullable = True) # видимость баланса


class transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user = Column (String, nullable = True) # пользователь
    datatime = Column(String, nullable = True) # время транзакции
    amount = Column(String, nullable = True) # количество денег
    users_id = Column(Integer, ForeignKey("users.id"), primary_key=True) # id пользователя кто совершил транзакцию
    referal = Column(Boolean, default=False, nullable = True) # является ли рефералом
    whoreferal = Column(String, nullable = True) # id человека кто привел этого пользователя

