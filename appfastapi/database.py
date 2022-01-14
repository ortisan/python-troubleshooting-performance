from contextvars import ContextVar
from peewee import MySQLDatabase, Model, AutoField, CharField, BigIntegerField
from fastapi import Depends

from typing import Any, List, Optional

from pydantic import BaseModel
from pydantic.utils import GetterDict

import peewee

DATABASE_NAME = "tickdb"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db = MySQLDatabase(DATABASE_NAME, user='root', password='123456',
                         host='localhost', port=3306)

db = MySQLDatabase(DATABASE_NAME, user='root', password='123456',
                         host='mysql', port=3306)


db._state = PeeweeConnectionState()

class MyBaseModel(Model):
    class Meta:
        database = db

class Tick(MyBaseModel):
    class Meta:
        db_table = 'tick'

    id = AutoField()
    epoch_timestamp = BigIntegerField()
    symbol = CharField(max_length=50)
    value = BigIntegerField()

    def __str__(self):
        return f"{self.epoch_timestamp} - {self.symbol} - {self.value}" 


class TickModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    epoch_timestamp: int
    value: int
    

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()

def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()