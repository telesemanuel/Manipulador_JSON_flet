import flet as ft
import json
from dataclasses import dataclass

@dataclass
class Pessoa:
    codigo: int
    nome: str
    cpf: str
    email: str
    profissao: str

    def __del__(self):
        return(f'Objeto {self.nome} de código {self.codigo} foi destruído')

class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [{'codigo': 0, 'nome': 'Admin', 'cpf': '000.000.00-00', 'email': 'admin@admin.com', 'profissao': 'Administrador'}]
            json_dados = json.dumps(usuarios, ensure_ascii=False)
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                f.write(json_dados)
            return f'{nome_arquivo}.json criado com sucesso'
        except Exception as e:
            return f'Não foi possível criar o arquivo. {e}'
    
    def abrir_arquivo(self, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
            return dados
        except Exception as e:
            return f'Não foi possível abrir o arquivo. {e}'

    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False)
            return "Dados gravados com sucesso."
        except Exception as e:
            return f"Não foi possível salvar os dados. {e}."
    
    def deletar_usuario(self, usuarios, codigo, nome_arquivo):
        if 0 <= codigo < len(usuarios):
            del(usuarios[codigo])
            self.salvar_dados(usuarios, nome_arquivo)
            return f"Usuário de código {codigo} deletado com sucesso."
        else:
            return "Código inválido."

def main(page: ft.Page):
    page.title = "Gerenciador de Usuários"
    page.scroll = "adaptive"
    
    manipulador = Manipulador()
    usuarios = []
    nome_arquivo = ft.TextField(label="Nome do arquivo", width=300)
    resultado = ft.Text(value="Resultado aparecerá aqui", width=300, size=20)
    
    # Funções para as ações
    def criar_arquivo_click(e):
        res = manipulador.criar_arquivo(nome_arquivo.value)
        resultado.value = res
        page.update()

    def abrir_arquivo_click(e):
        nonlocal usuarios
        res = manipulador.abrir_arquivo(nome_arquivo.value)
        if isinstance(res, list):
            usuarios = res
            resultado.value = f"Arquivo {nome_arquivo.value}.json aberto com sucesso!"
        else:
            resultado.value = res
        page.update()

    def listar_usuarios_click(e):
        if usuarios:
            lista = "\n".join([f"{u['codigo']} - {u['nome']} ({u['profissao']})" for u in usuarios])
            resultado.value = f"Usuários:\n{lista}"
        else:
            resultado.value = "Nenhum usuário encontrado."
        page.update()

    def adicionar_usuario_click(e):
        nonlocal usuarios
        novo_usuario = Pessoa(
            codigo=len(usuarios),
            nome=nome_input.value,
            cpf=cpf_input.value,
            email=email_input.value,
            profissao=profissao_input.value
        )
        usuarios.append(novo_usuario.__dict__)
        res = manipulador.salvar_dados(usuarios, nome_arquivo.value)
        resultado.value = res
        page.update()

    def deletar_usuario_click(e):
        try:
            codigo = int(codigo_input.value)
            res = manipulador.deletar_usuario(usuarios, codigo, nome_arquivo.value)
            resultado.value = res
        except ValueError:
            resultado.value = "Por favor, insira um código válido."
        page.update()

    # Titulo
    titulo = ft.Text("Manipulador de Arquivos JSON", font_family= "Times New Roman", weight= "bold", size=35)

    # Entradas para adicionar usuário
    nome_input = ft.TextField(label="Nome", width=300)
    cpf_input = ft.TextField(label="CPF", width=300)
    email_input = ft.TextField(label="Email", width=300)
    profissao_input = ft.TextField(label="Profissão", width=300)

    # Entrada para deletar usuário
    codigo_input = ft.TextField(label="Código do usuário para deletar", width=300)

    # Botões
    criar_arquivo_btn = ft.ElevatedButton("Criar Arquivo", width=250, on_click=criar_arquivo_click)
    abrir_arquivo_btn = ft.ElevatedButton("Abrir Arquivo", width=250, on_click=abrir_arquivo_click)
    listar_usuarios_btn = ft.ElevatedButton("Listar Usuários", width=250, on_click=listar_usuarios_click)
    adicionar_usuario_btn = ft.ElevatedButton("Adicionar Usuário", width=250, on_click=adicionar_usuario_click)
    deletar_usuario_btn = ft.ElevatedButton("Deletar Usuário", width=250, on_click=deletar_usuario_click)

    # Adicionando os elementos na página
    page.add(
        ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nome_arquivo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([criar_arquivo_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([abrir_arquivo_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([listar_usuarios_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text("Adicionar novo usuário:", size=15)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nome_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([cpf_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([email_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([profissao_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([adicionar_usuario_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text("Deletar usuário:", size=15)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([codigo_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([deletar_usuario_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([resultado], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main)
