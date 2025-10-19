from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello"}

@app.get("/files/myfile.txt")
def get_file():
    return FileResponse("myfile.txt", media_type="text/plain")