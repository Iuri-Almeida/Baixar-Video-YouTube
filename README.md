# Baixar Vídeo YouTube

Programa que faz o download de vídeos do YouTube.

# Descrição

Esse programa foi escrito na linguagem Python e usou a biblioteca <a href="https://pypi.org/project/pytube/">PyTube</a> como base. Ele faz o download de um vídeo do YouTube a partir da URL do vídeo e do nome que deseja salvar, com esses dados sendo passados pela linha de comando (terminal), e salva esse vídeo baixado em uma pasta.

# Como funciona?

O programa recebe como parâmetros a URL de onde está o vídeo (-u [URL]) e o nome que o usuário deseja usar para salvar o vídeo (-n [NOME]). Após ter passado os parâmetros necessários, o programa irá criar uma pasta, caso não exista, para armazenar o vídeo baixado nesta pasta.

<b>Obs.:</b> O nome que dará para o vídeo não precisa conter a extensão, pois já está setada para ter a extensão <b>.mp4</b> para todos os vídeos que serão baixados.

# Instalação

É preciso ter o python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). Para fazer o uso desse recurso, é preciso baixar uma biblioteca, é ela:

* PyTube - Forma de instalação: <b>pip install pytube</b>

<b>Obs.:</b> Essa instalação pode ser feita pelo terminal do seu computador (necessário que já tenha o python instalado) ou pelo <a href="https://www.jetbrains.com/pt-br/pycharm/download/">PyCharm</a>, se preferir.

# Uso

Após a instalação, para começar a usar basta clonar esse repositório e digitar o comando <b>python baixa-video-ytb.py -u [URL] -n [NOME]</b> no terminal ou rodar pelo PyCharm.

# Referências

* <a href="https://www.youtube.com/channel/UCEn6kONg6EC_Ylh0RlInsMw">Canal YouTube - Universo Discreto</a>
* <a href="https://universodiscreto.com/">Blog - Universo Discreto</a>