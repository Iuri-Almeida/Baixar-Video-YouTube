# Projeto Baixa Vídeo YouTube - Python e PyTube
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 30/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou a biblioteca
# 			 PyTube como base. Ele faz o download de um vídeo do YouTube a partir
# 			 da URL do vídeo e do nome que deseja salvar, com esses dados sendo
# 			 passados pela linha de comando (terminal), e salva esse vídeo baixado
# 			 em uma pasta.
# Forma de uso: python baixa-video-ytb.py -u [URL do youtube] -n [nome para salvar o vídeo]


# Importações necessárias.
from pytube import YouTube
import os, argparse


# Define uma descrição sobre o que o programa faz.
parser = argparse.ArgumentParser(description='Fazer o download de vídeos do YouTube.')

# Define uma 'flag' para poder passar a URL do vídeo.
# Ex.: python baixa-video-ytb.py -l https://www.youtube.com/watch?v=uqvs2Yi7imA
parser.add_argument('-u', dest='url_youtube', help='URL do vídeo no youtube')

# Define uma 'flag' para poder passar o nome desejado para salvar o vídeo.
parser.add_argument('-n', dest='nome', help='nome que deseja salvar o vídeo')

# Define uma váriavel que vai poder ser chamada para ter acesso aos dados que foram
# passados pela linha de comando (terminal).
args = parser.parse_args()


# Função responsável por fazer o download dos vídeos do YouTube.
def baixa_Video_YTB():

	print('[INFO] Iniciando o programa...')

	# Se não existir uma pasta chamada 'videos' no diretório, crie.
	if (os.path.exists('videos') == False):
		os.mkdir('videos')

	print('[INFO] Iniciando o download...')

	# Função que recebe a URL do vídeo.
	ytb = YouTube(args.url_youtube)

	# streams -> representa todos os níveis de qualidade e as extensões do vídeo no YouTube.
	# filter() -> faz a filtragem dos streams escolhendo todas as qualidades do vídeo que
	# 			  possuem a extensão escolhida para baixar.
	nome_video = ytb.streams.filter(file_extension='mp4')

	# Pega a qualidade mais alta dos vídeos com extensão mp4.
	nome_video = nome_video.get_highest_resolution()

	# Faz o download do vídeo.
	nome_video = nome_video.download()

	# Renomeie o vídeo para 'video.mp4' e salve na pasta 'videos/'.
	# Obs.: É feito isso pela facilidade para localizar depois dentro da pasta, pois
	# 		depois de baixado vem com um nome muito grande.
	os.rename(nome_video, 'videos/' + args.nome + '.mp4')

	print('[INFO] Vídeo ' + args.nome + '.mp4 baixado!')

	print('[INFO] Termiando o programa...')


# Função principal, onde serão chamadas as outras funções.
def main():
	
	# Chamando a função para fazer o download de um vídeo no YouTube.
	baixa_Video_YTB()


if __name__ == "__main__":
	main()