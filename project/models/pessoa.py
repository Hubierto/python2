from project.models.enums.sexo import Sexo

class Pessoa:

    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self._nome = nome
        self._idade = idade
        self._sexo = sexo

    def set_idade(self,idade):
        if not _verificar_idade_negativa(idade):
            self._idade = idade

    def _verificar_idade_negativa(self, idade) -> int:
        if idade < 0:
            self._idade = 0
        return True

    def __str__(self) -> str:
        return (
            f"\nNome: {self._nome}"
            f"\nIdade: {self._idade}"
            f"\nSexo: {self._sexo.value}"
        )
    