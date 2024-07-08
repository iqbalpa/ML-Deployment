from predict import read_image
from predict import transform
from fastapi import FastAPI, File
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "The app is running"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/predict/")
async def create_upload_file(file: bytes = File(...)):
    # read image
    imagem = read_image(file)
    # transform and prediction 
    prediction = transform(imagem)
    return prediction

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

