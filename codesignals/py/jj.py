import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        _data = self._data
        _tag = self.query_tag

        for index, value in enumerate(_data['items']):
            if tag in value['tags']:
                yield _data['items'][index]
        

    def first(self):
        res = self.search()
        if not res:
            return "not Found"
        else:
            return self.search().next()

datafile = '/home/brian/somegit/codesignals/py/jj.json'
r = SearchByTag(data_file=datafile, query_tag='crime')
r.search()
r.first()