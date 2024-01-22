from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz

app = FastAPI()

origins = [
    "https://matheusferraz.tech",
    "https://ferrazrezende.github.io",
]




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():

    fuso_horario = pytz.timezone('America/Sao_Paulo')

    data_nascimento = datetime(2023, 7, 24, 14, 56, tzinfo=fuso_horario)
    data_atual = datetime.now(pytz.utc).astimezone(fuso_horario)

    idade = calcular_idade_miguel(data_atual, data_nascimento)


    return {"anos": idade.years,
            "meses": idade.months,
            "semanas": idade.weeks,
            "dias": idade.days,
            "horas": idade.hours,
            "minutos": idade.minutes,}

@app.get("/index")
async def get_index():
    with open("frontend/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)



def calcular_idade_miguel(data_atual, data_nascimento):
    diff = relativedelta(data_atual, data_nascimento)
    return diff


