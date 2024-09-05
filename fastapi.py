# from fastapi import FastAPI

# app =FastAPI()
# @app.get("/")

# def hi():
#     return {"message":"hello python"}

from fastapi import FastAPI

app=FastAPI()
@app.get("/")

def hi():
    return {"message":"hello pyhton"}