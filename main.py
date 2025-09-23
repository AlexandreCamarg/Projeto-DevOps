"""Módulo principal da API com FastAPI para gerenciar estudantes."""

import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    """Modelo que representa um estudante."""
    name: str
    curso: str
    ativo: bool


@app.get("/")
def root():
    """Rota raiz da API."""
    return {"message": "API rodando com sucesso 🚀"}


@app.get("/teste")
def funcaoteste():
    """Rota de teste que retorna um número aleatório."""
    return {"teste": True, "num_aleatorio": random.randint(0, 100000)}


@app.post("/estudante")
def create_estudante(estudante: Estudante):
    """Cria um novo estudante."""
    return estudante


@app.put("/estudante/{id_estudante}")
def update_estudante(id_estudante: int):
    """Atualiza os dados de um estudante com base no ID."""
    return {"updated": id_estudante > 0}


@app.delete("/estudante/{id_estudante}")
def delete_estudante(id_estudante: int):
    """Deleta um estudante com base no ID."""
    return {"deleted": id_estudante > 0}
