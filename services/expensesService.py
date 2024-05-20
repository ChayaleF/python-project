from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.expenses import Expenses
from models.users import User

collection = db['expenses']


async def get_expenses_by_user_id(user_id):
    print("service")
    try:
        expenses_by_user_id =list(collection.find({"user_id": user_id}))
        for i in expenses_by_user_id:
            i.pop("_id")
    except Exception as e:
        raise e
    return expenses_by_user_id

async def add_new_expenses(new_expenses:Expenses):
    try:
        collection.insert_one(new_expenses.dict())
    except Exception as e:
        raise e
