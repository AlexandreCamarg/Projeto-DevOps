from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "API rodando com sucesso 🚀"}

@pytest.mark.asyncio
async def test_funcaoteste():
    """Testa se a função de teste retorna o número aleatório esperado."""
    with patch("random.randint", return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    """Testa a criação de um estudante."""
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5) == {"updated": False}
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10) == {"updated": True}
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5) == {"deleted": False}
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10) == {"deleted": True}
    assert result


