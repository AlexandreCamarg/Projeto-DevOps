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
    """Testa se a rota raiz retorna a mensagem correta."""
    assert root() == {"message": "API rodando com sucesso 🚀"}


def test_funcaoteste():
    """Testa se a função de teste retorna o número aleatório esperado."""
    with patch("random.randint", return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    """Testa a criação de um estudante."""
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    created = create_estudante(estudante_teste)
    assert created.name == estudante_teste.name
    assert created.curso == estudante_teste.curso
    assert created.ativo == estudante_teste.ativo


def test_update_estudante_negativo():
    """Testa atualização de estudante com ID inválido."""
    assert update_estudante(-5) == {"updated": False}


def test_update_estudante_positivo():
    """Testa atualização de estudante com ID válido."""
    assert update_estudante(10) == {"updated": True}


def test_delete_estudante_negativo():
    """Testa exclusão de estudante com ID inválido."""
    assert delete_estudante(-5) == {"deleted": False}


def test_delete_estudante_positivo():
    """Testa exclusão de estudante com ID válido."""
    assert delete_estudante(10) == {"deleted": True}
