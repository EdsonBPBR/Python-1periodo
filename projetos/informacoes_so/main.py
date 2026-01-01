import platform
import socket
import datetime

def gerar_relatorio():
    nome_maquina = socket.gethostname()
    sistema = platform.system()
    versao = platform.release()
    processador = platform.processor()
    data_atual = datetime.datetime.now().strftime("%d/%a/%Y %H:%M:%S")

    relatorio = f"""
    {'='*40}
    {'RELATÓRIO DE INFORMAÇÕES DO SISTEMA':^40}
    {'-'*40}
    {'DATA DA COLETA: ':<20} {data_atual}
    {'NOME DA MÁQUINA: ':<20} {nome_maquina}
    {'SISTEMA OPERACIONAL: ':<20} {sistema} {versao}
    {'PROCESSADOR: ':<20} {processador}
    """
    return relatorio

def gerar_arquivo(dados):
    with open('projetos/informacoes_so/relatorio.txt', 'w', encoding='UTF-8') as arquivo:
        arquivo.write(dados)
        
if __name__ == '__main__':
    dados = gerar_relatorio()
    gerar_arquivo(dados)
    