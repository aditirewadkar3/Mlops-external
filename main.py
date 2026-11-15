from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def addition(num1: float, num2: float):

    result = num1 + num2

    return {
        "num1": num1,
        "num2": num2,
        "addition": result
    }