from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle


with open("model.pkl", "rb") as f:
    model=pickle.load(f)

app=FastAPI()
templates= Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": None}
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    TV: float= Form(...),
    Radio: float= Form(...),
    Newspaper: float= Form(...),
):
    predicted_value = model.predict([[TV, Radio, Newspaper]])[0]
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "prediction": round(float(predicted_value),2)
        }
    )