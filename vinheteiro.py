import os
import random
import sys
from pydub import AudioSegment
from tkinter import Tk, filedialog, messagebox

# Configuração do FFmpeg (ajuste o caminho se necessário)
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"

def selecionar_diretorio():
    """Seleciona a pasta com as músicas"""
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Selecione a pasta com as músicas")

def selecionar_vinheta():
    """Seleciona o arquivo da vinheta"""
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Selecione o arquivo da vinheta",
        filetypes=[("Arquivos de Áudio", "*.mp3 *.wav *.ogg *.flac")]
    )

def mixar_vinheta(musica, vinheta, ponto_insercao, volume_vinheta=-8):
    """Mixa a vinheta em segundo plano na música"""
    vinheta_ajustada = vinheta + volume_vinheta  # Ajuste de volume
    return musica.overlay(vinheta_ajustada, position=ponto_insercao)

def calcular_ponto_insercao(duracao_musica, duracao_vinheta):
    """Calcula pontos de inserção entre 40s iniciais ou últimos 50s"""
    pontos = []
    
    # Intervalo dos 40 segundos iniciais (em milissegundos)
    inicio_max = min(40 * 1000, duracao_musica - duracao_vinheta)
    if inicio_max > 0:
        pontos.append(random.randint(0, inicio_max))
    
    # Intervalo dos últimos 50 segundos (em milissegundos)
    fim_min = max(duracao_musica - (50 * 1000) - duracao_vinheta, 0)
    if fim_min < duracao_musica - duracao_vinheta:
        pontos.append(random.randint(fim_min, duracao_musica - duracao_vinheta))
    
    return random.choice(pontos) if pontos else None

def processar_musicas(diretorio, vinheta_path, volume_vinheta=-8):
    """Processa todas as músicas do diretório"""
    try:
        vinheta = AudioSegment.from_file(vinheta_path)
        duracao_vinheta = len(vinheta)
        formatos = ('.mp3', '.wav', '.ogg', '.flac')
        
        for arquivo in [f for f in os.listdir(diretorio) if f.lower().endswith(formatos)]:
            try:
                caminho = os.path.join(diretorio, arquivo)
                musica = AudioSegment.from_file(caminho)
                duracao = len(musica)
                
                # Verifica se a música é longa o suficiente
                if duracao < (40 * 1000) + duracao_vinheta:
                    print(f"⚠ Pulando {arquivo} (muito curta para inserção)")
                    continue
                
                # Calcula ponto de inserção
                ponto = calcular_ponto_insercao(duracao, duracao_vinheta)
                if ponto is None:
                    print(f"⚠ {arquivo} - Não há pontos adequados")
                    continue
                
                # Mixa e salva
                musica_mixada = mixar_vinheta(musica, vinheta, ponto, volume_vinheta)
                musica_mixada.export(caminho, format=arquivo.split('.')[-1], bitrate="320k")
                os.utime(caminho, None)  # Atualiza data/hora
                
                print(f"✓ {arquivo} - Vinheta em {ponto//1000}s")
                
            except Exception as e:
                print(f"❌ Erro em {arquivo}: {str(e)}")
        
        messagebox.showinfo("Sucesso", "Processamento concluído!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Falha geral: {str(e)}")

if __name__ == "__main__":
    # Interface amigável
    print("=== MIXADOR DE VINHETAS ===")
    print("1. Selecione a pasta com as músicas")
    pasta = selecionar_diretorio()
    if not pasta: sys.exit()
    
    print("\n2. Selecione o arquivo da vinheta")
    vinheta = selecionar_vinheta()
    if not vinheta: sys.exit()
    
    print("\n3. Processando...")
    processar_musicas(pasta, vinheta, volume_vinheta=-1)  # Ajuste o volume aqui
    
    input("\nPressione Enter para sair...")