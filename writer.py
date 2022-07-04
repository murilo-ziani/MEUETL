from requisitor import Extract
from pathlib import Path
import pandas as pd

# Classe para gravar arquivos em CSV
class writer:

    def __init__(self) -> None:
        self.extract = Extract(url="https://api.punkapi.com/v2/beers")
        self.beer_information = self.extract.get_beer_information
        
    
    def writer(self, file_name=None):
        path = Path(f'./{file_name}').mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame.from_dict(self.beer_information)
        arquivo = df.transpose()
        arquivo.index.name = "ID"
        return arquivo.to_csv(f'./{file_name}/{file_name}.csv', index=True)
