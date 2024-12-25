from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def roof ():
    return "hello world"