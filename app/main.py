#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel # allows us to model data
import json
import os

app = FastAPI()

@app.get("/")  # zone apex z3 #decorator
def zone_apex():
    return {"Hello": "Hello Vinith, How's your day?"} # returns json

@app.get("/square/{a}")
def square(a: int):
    return {"square": a*a}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
   return {"product": c * d}

@app.get("/subtract/{e}/{f}")
def multiply(e: int, f: int):
   return {"subtract": e - f}
