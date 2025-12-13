from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)


fruits =  [

    {"name" : "Apple", "price": 1.2},
    {"name" : "Banana", "price": 0.8},
    {"name" : "Pineapple", "price": 2.2},
    {"name" : "Cherry", "price": 1.2},
    {"name" : "Mango", "price": 4.2},
    {"name" : "Orange", "price": 7.2},
    {"name" : "kiwi", "price": 3.2},
    {"name" : "Organic Cucumber", "price": 5.2},
    {"name" : "Lime", "price": 6.2},
    {"name" : "Bluberry", "price": 5.2},
]



@app.get("/fruits")
def get_fruits():
    return {"fruits": fruits}