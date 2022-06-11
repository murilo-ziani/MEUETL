import requests, json
import logging, sys


# Url padrão para consumo
url = "https://api.punkapi.com/v2/beers/"

# Variável para buscar as cervejas no API
# Será necessário realizar um loop para coletar todas as cervejas disponíveis na API
id = 1

# Definindo objeto a ser requisitado
beers = f'{url}/{id}'

# Requisição
beer = requests.get(beers)

# Tratamento de Erros de requisição

if beer.status_code != 200:
    logging.warning('Não houve retorno da API')
    sys.exit()
else:
    beer = beer.json()

# Configurando as informações a serem impressas no catálogo
name = beer[0]['name']
# style = beers[0]['']
image = beer[0]['image_url']
abv = beer[0]['abv']
ibu = beer[0]['ibu']
hop_list = []
hops = beer[0]['ingredients']['hops']
for hop in hops:
    hop_list.append(hop['name'])
    #     # print(hop)
combinations = beer[0]['food_pairing']

beer_information = {'Nome: ':name, 'Imagem: ':image, 'ABV: ':abv, 'IBU: ':ibu, 'Lúpulos: ':hop_list, 'Melhores combinações: ':combinations}
print(beer_information)
    