import pytest
from mongomock.patch import patch
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

from services.expensesService import get_expenses_by_user_id, collection


@pytest.mark.asyncio
async def test_get_expenses_by_user_id():

    mock_expenses_first = { "id": 1, "user_id": 3, "description":"test1","amount": 100,"date":1/5/2020}


    mock_expenses_second ={ "id": 2, "user_id": 3, "description":"test2","amount": 200,"date":1/5/2020}


    # הוספת הרשומות למסד הנתונים
    collection.insert_one(mock_expenses_first)
    collection.insert_one(mock_expenses_second)

    # קריאה לפונקציה הנבדקת
    expenses = await get_expenses_by_user_id(3)
    # בדיקת התוצאות
    assert len(expenses) == 2
    assert expenses[0]["id"] == 1
    assert expenses[0]["amount"] == 100
    assert expenses[1]["id"] == 2
    assert expenses[1]["amount"] == 200





# @pytest.mark.asyncio
# @patch('services.expensesService.collection')
# async def test_update_new_expenses(mock_collection):
#     new_expenses = Expenses(id=1, user_id="user1", amount=150)
#     mock_collection.find.return_value = [{"id": 1, "user_id": 1, "amount": 100}]
#     updated_expense = await update_new_expenses(new_expenses, 1, 1)
#     assert updated_expense.amount == 150
#     mock_collection.update_one.assert_called_with({"id": 1}, {"$set": new_expenses.dict()})
#
#     with pytest.raises(HTTPException):
#         await update_new_expenses(new_expenses, 1, 2)
#
#     with pytest.raises(HTTPException):
#         await update_new_expenses(new_expenses, 2, 2)
#
# @pytest.mark.asyncio
# @patch('services.expensesService.collection')
# async def test_delete_one_expenses(mock_collection):
#     await delete_one_expenses(1, 1)
#     mock_collection.delete_one.assert_called_with({"id": 1, "user_id": 2})

# @pytest.mark.asyncio
# @patch('services.expensesService.collection')
# async def test_get_expenses_by_user_id(mock_collection):
#     mock_collection.find.return_value = [{"id": 1, "user_id": 1, "amount": 100}, {"id": 2, "user_id": 1, "amount": 200}]
#     expenses = await get_expenses_by_user_id(1)
#     assert len(expenses) == 2
#     assert expenses[0]["id"] == 1
#     assert expenses[1]["id"] == 2
#     mock_collection.find.assert_called_with({"user_id": 1})