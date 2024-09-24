import pytest
from project.models.pessoa import Pessoa
from project.models.enums.sexo import Sexo

#teste unitário

#Modelo
@pytest.fixture
def pessoa_valida():
    #Instanciando classe pessoa
    pessoa1 = Pessoa("Marta", 22, Sexo.FEMININO)
    return pessoa1

def test_pessoa_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Jose"
    assert pessoa_valida._nome == "Jose"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida._nome == "Marta"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida._idade == 22

def test_pessoa_idade_negativa(pessoa_valida):
    pessoa_valida._verificar_idade_negativa == (-1)
    assert pessoa_valida._idade == 0   