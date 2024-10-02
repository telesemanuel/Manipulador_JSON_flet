import json 
import flet as ft
from pessoa import Pessoa
from manipulador import Manipulador

def main(page: ft.Page):
    page.title = "Manipulador de Arquivos JSON"
    page.scroll = "adaptive"

    m = Manipulador()
    usuarios = []
    abrir_arquivo = ""

    
        


    # Interface

    arquivo_mostrar = ft.TextField(label= "Nome do arquivo")
    exibicao = ft.TextField(label="Conteudo do arquivo")

    info = {"nome":ft.TextField(label="Nome:"),
            "cpf":ft.TextField(label="CPF:"),
            "email":ft.TextField(label="E-amil:"),
            "profissao":ft.TextField(label="Profissão:"),
            }
    
    btn_abrir_arquivo = ft.ElevatedButton("Abrir arquivo", on_click=lambda e:abrir_arquivo)
    # btn_salvar_usario = ft.ElevatedButton("Salvar Usúario", on_click= salvar_dados)
    # btn_del_usario = ft.ElevatedButton("Salvar Usúario", on_click= deletar_usuario)

    page.add(
        btn_abrir_arquivo
    )

ft.app(main)
