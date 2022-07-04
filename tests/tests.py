from genericpath import exists
from requisitor import Extract
from writer import writer


class Tests:

    def requisitor_api(self):
        extract = Extract(url='https://api.punkapi.com/v2/beers')
        assert isinstance(extract, Extract)
        assert extract.url == 'https://api.punkapi.com/v2/beers'

        beer_information = Extract.beer_information()
        assert isinstance(beer_information, Extract.beer_information)
        assert isinstance(beer_information, dict)
        assert isinstance(beer_information[1], dict)
        assert isinstance(beer_information[1][4], list)

    def writer_csv(self, file_name):
        obj = writer
        assert isinstance(obj, writer)

        file_name = writer(file_name)
        assert isinstance(file_name, str)
        assert exists(f'./{file_name}/{file_name}.csv')
