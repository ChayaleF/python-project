from fastapi import HTTPException

from models.expenses import Expenses
from services.userService import collection


def check_user_id(new_expenses: Expenses,user_id):
    print(new_expenses)
    try:
        print("try0")

        result = list(collection.find({"id": new_expenses.user_id}))
        print("try1")

        print(result[0])
        user_id = int(user_id)
        print("try2")
    except Exception as e:
        print("except")
        # print(e)
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    if len(result) == 0 or user_id != new_expenses.user_id:
        raise HTTPException(status_code=401, detail="unauthorized")

    return user_id