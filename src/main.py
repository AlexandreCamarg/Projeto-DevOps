
import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@app.get("/")
def root():
    return {"message": "API rodando com sucesso 🚀"}


@app.get("/teste")
def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 100000)}


@app.post("/estudante")
def create_estudante(estudante: Estudante):
    return estudante


@app.put("/estudante/{id_estudante}")
def update_estudante(id_estudante: int):
    return {"updated": id_estudante > 0}


@app.delete("/estudante/{id_estudante}")
def delete_estudante(id_estudante: int):
    return {"deleted": id_estudante > 0}


