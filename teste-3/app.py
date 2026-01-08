from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + Mangum!!!"}


@app.get("/hello")
def hello():
    return {"message": "Hello from another path!"}


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Recurso encontra-se em outra galáxia!", "path_incorreto": str(request.url.path)},
    )

handler = Mangum(app)
