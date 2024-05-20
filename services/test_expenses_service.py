import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from services.expensesService import get_expenses_by_user_id, add_new_expenses, update_new_expenses, delete_one_expenses
from models.expenses import Expenses

@pytest.mark.asyncio
@patch('your_module.collection')
async def test_get_expenses_by_user_id(mock_collection):
    mock_collection.find.return_value = [{"id": 1, "user_id": "user1", "amount": 100}, {"id": 2, "user_id": "user1", "amount": 200}]
    expenses = await get_expenses_by_user_id("user1")
    assert len(expenses) == 2
    assert expenses[0]["id"] == 1
    assert expenses[1]["id"] == 2
    mock_collection.find.assert_called_with({"user_id": "user1"})

@pytest.mark.asyncio
@patch('your_module.collection')
@patch('your_module.expenses_id', 0)
async def test_add_new_expenses(mock_collection):
    new_expenses = Expenses(id=0, user_id="user1", amount=100)
    await add_new_expenses(new_expenses)
    mock_collection.insert_one.assert_called_once()
    inserted_expense = mock_collection.insert_one.call_args[0][0]
    assert inserted_expense["id"] == 1
    assert inserted_expense["user_id"] == "user1"
    assert inserted_expense["amount"] == 100

@pytest.mark.asyncio
@patch('your_module.collection')
async def test_update_new_expenses(mock_collection):
    new_expenses = Expenses(id=1, user_id="user1", amount=150)
    mock_collection.find.return_value = [{"id": 1, "user_id": "user1", "amount": 100}]
    updated_expense = await update_new_expenses(new_expenses, 1, "user1")
    assert updated_expense.amount == 150
    mock_collection.update_one.assert_called_with({"id": 1}, {"$set": new_expenses.dict()})

    with pytest.raises(HTTPException):
        await update_new_expenses(new_expenses, 1, "user2")

    with pytest.raises(HTTPException):
        await update_new_expenses(new_expenses, 2, "user1")

@pytest.mark.asyncio
@patch('your_module.collection')
async def test_delete_one_expenses(mock_collection):
    await delete_one_expenses(1, "user1")
    mock_collection.delete_one.assert_called_with({"id": 1, "user_id": "user1"})
