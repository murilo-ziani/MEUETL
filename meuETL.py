import requests, time
import logging, sys


class Extract():
    def __init__(self, url):
        # Url padrão para consumo
        self.__url = url
        self.get_beer_information = self.beer_information()

    @property
    def url(self):
        return self.__url

    def beer_information(self):
        
        beer_information = {}
        for id in range(1, 326):
            # Definindo objeto a ser requisitado
            beers = f'{self.url}/{id}'
            print(beers)
            # Requisição
            beer = requests.get(beers)

            # Tratamento de Erros de requisição

            if beer.status_code != 200:
                print(beer.status_code)
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
            beer_information.update({id: {'Nome da cerveja':name, 'Imagem':image, 'Graduação Alcoólica (ABV)':abv, 'IBU':ibu, 'Lúpulos':hop_list, 'Melhores combinações':combinations}})
            time.sleep(0.1)
        return beer_information
    