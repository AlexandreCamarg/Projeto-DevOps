from src.main import root, funcaoteste, Estudante, create_estudante, update_estudante, delete_estudante
from unittest.mock import patch


def test_root():
    assert root() == {"message": "API rodando com sucesso 🚀"}


def test_funcaoteste():
    with patch("random.randint", return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    created = create_estudante(estudante_teste)
    # Comparar atributos ao invés do objeto inteiro (caso não tenha __eq__)
    assert created.name == estudante_teste.name
    assert created.curso == estudante_teste.curso
    assert created.ativo == estudante_teste.ativo


def test_update_estudante_negativo():
    assert update_estudante(-5) is False


def test_update_estudante_positivo():
    assert update_estudante(10) is True


def test_delete_estudante_negativo():
    assert delete_estudante(-5) is False


def test_delete_estudante_positivo():
    assert delete_estudante(10) is True
