from fastapi import FastAPI
from starlette.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

@app.get("/")
async def read_root():
    
    data_nascimento = datetime(2023, 7, 24, 14, 56)
    data_atual = datetime.now()

    idade = calcular_idade_miguel(data_atual, data_nascimento)

    diferenca_tempo = calcular_diferenca_de_tempo(data_atual, data_nascimento)

    return {"idade": idade, "diferenca_tempo": diferenca_tempo}

@app.get("/index")
async def get_index():
    with open("frontend/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)



def calcular_idade_miguel(data_atual, data_nascimento):
    delta = data_atual - data_nascimento

    anos = delta.days // 365
    meses = (delta.days % 365) // 30
    dias = (delta.days % 365) % 30

    idade = f"{anos} anos, {meses} meses e {dias} dias"
    return idade


def calcular_diferenca_de_tempo(data_atual, data_nascimento):

    delta_tempo = data_atual - data_nascimento

    dias = delta_tempo.days
    horas = delta_tempo.seconds // 3600
    minutos = (delta_tempo.seconds // 60) % 60

    diferenca_tempo = f"{dias} dias, {horas} horas, {minutos} minutos"
    return diferenca_tempo

