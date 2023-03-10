from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "Hello World"}


# https://fastapi.tiangolo.com/tutorial/path-params/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/