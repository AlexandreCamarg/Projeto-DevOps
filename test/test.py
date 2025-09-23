"""Testes unitários para o módulo main da API."""

from unittest.mock import patch
from src.main import (
    root,
    funcaoteste,
    Estudante,
    create_estudante,
    update_estudante,
    delete_estudante,
)


def test_root():
    result = root()
    yield result
    assert result == {"message": "API rodando com sucesso 🚀"}


def test_funcaoteste():
    """Testa se a função de teste retorna o número aleatório esperado."""
    with patch("random.randint", return_value=12345):
        result = funcaoteste()
        yield result
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    """Testa a criação de um estudante."""
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result


def test_update_estudante_negativo():
    result = update_estudante(-5) == {"updated": False}
    yield result
    assert not result


def test_update_estudante_positivo():
    result = update_estudante(10) == {"updated": True}
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5) == {"deleted": False}
    yield result
    assert result


def test_delete_estudante_positivo():
    result = delete_estudante(10) == {"deleted": True}
    yield result
    assert result
    
