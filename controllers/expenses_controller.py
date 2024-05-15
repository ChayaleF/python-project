import uvicorn

from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,constr, ValidationError, validator, field_validator

from models.users import User
from services.userService import login, signUp, update

Expenses_Router = APIRouter()

@Expenses_Router.get("/{userId}")
async def get_expenses(userId:int):
  try:
   expenses=await get_expenses(userId)
  except :
    raise HTTPException(status_code=400, detail="oops... an error occurred" )
  return expenses
