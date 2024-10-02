# importação do dataclass
from dataclasses import dataclass

# criar a classe pessoa
@dataclass
class Pessoa:
    codigo: int
    nome: str
    cpf: str
    email: str
    profissao: str
    
    # destrutor
    def __del__(self):
        print(f'Objeto {self.nome} de código {self.codigo} foi destruído')

# Exemplo de uso
p = Pessoa(codigo=1, nome="João", cpf="123.456.789-00", email="joao@example.com", profissao="Desenvolvedor")