from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    assert result == {"message": "API rodando com sucesso 🚀"}

def test_funcaoteste():
    """Testa se a função de teste retorna o número aleatório esperado."""
    with patch("random.randint", return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

def test_create_estudante():
    """Testa a criação de um estudante."""
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result

def test_update_estudante_negativo():
    result = update_estudante(-5)
    assert result == {"updated": False}

def test_update_estudante_positivo():
    result = update_estudante(10)
    assert result == {"updated": True}

def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    assert result == {"deleted": False}

def test_delete_estudante_positivo():
    result = delete_estudante(10)
    assert result == {"deleted": True}
