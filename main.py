from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
def root():
    return {"message": "API rodando com sucesso 🚀"}

# http://127.0.0.1:8000/helloworld
@app.get("/helloworld")
def hello_world():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/funcaoteste
@app.get("/funcaoteste")
def funcao_teste():
    return {"message": "Função de teste funcionando"}
