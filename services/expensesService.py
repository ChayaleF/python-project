from dataAccess.dataAccess import db
from models.users import User

collection = db['expenses']


async def getExpenses(user_id):
    expenses = collection.find({"id": user_id}).collection()
    # try:
    #
    # except:
    #      raise ValueError("error!!!")

    return expenses