Projeto Meu ETL para o NAPP Academy
Projeto desenvolvido utilizando a API: Punk API que retorna dados de todas as cervejas produzidas pela cervejaria Brew Dog, trata-os e tranforma-os em um csv contendo:

- Nome da cerveja;
- Link da Imagem;
- Graduação Alcóolica (ABV);
- IBU;
- Lúpulos; e
- Melhores combinações

Como executar:

Step.1 - Clonar o projeto
git clone https://github.com/murilo-ziani/MEUETL.git

Step.2 - Instalar a lib utilizada para a máquina virtual
pip install virtualenv

Step.3 - Abrir o terminal na pasta onde foi clonado o projeto (a venv estará fora dessa pasta, ao lado da pasta MeuETL)
python3 -m venv venv

Step.4 - Ativar o ambiente virtual
source ../venv/bin/activate (Linux ou macOS)
../venv/Scripts/activate.bat (Windows)

Step.5 - Instalar as bibliotecas necessárias
pip install -r requirements.txt

Step.6 - Executar em linha de comando
python3 -m __main__.py
