from meuETL import Extract
import csv
import pandas as pd

# Classe para gravar arquivos em CSV
class writer:

    def __init__(self) -> None:
        self.extract = Extract(url="https://api.punkapi.com/v2/beers")
        self.beer_information = self.extract.get_beer_information
        
    
    def writer(self):
        df = pd.DataFrame.from_dict(self.beer_information, orient='index')
        arquivo = df.transpose()
        return arquivo.to_csv('Catalogo.csv')

information = writer()
catalogo = information.writer()