# This is a sample Python script.
import uvicorn
from fastapi import FastAPI

from controllers.userController import User_Router

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

app.include_router(User_Router, prefix='/Tasks', tags=["Tasks"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
