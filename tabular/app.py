from fastapi import FastAPI
import joblib
import uvicorn

app = FastAPI()
joblib_in = open("model.pkl","rb")
model = joblib.load(joblib_in)

@app.get('/')
def index():
    return {'message': 'ML Model API is running!'}

@app.post('/predict')
def predict_car_type(data: dict):
    print()
    print("="*50)
    print(data)
    print("="*50)
    print()

    # get the data from the request
    beds = data['BEDS']
    bath = data['BATH']
    propertysqft = data['PROPERTYSQFT']

    # create a prediction
    prediction = model.predict([[beds, bath, propertysqft]])
    print()
    print("="*50)
    print(prediction)
    print(prediction[0])
    print(prediction[0][0])
    print("="*50)
    print()

    return {
        'prediction': prediction[0][0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)