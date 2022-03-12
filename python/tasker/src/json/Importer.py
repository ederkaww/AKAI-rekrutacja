import json


class Importer:

    def __init__(self):
        self.data = []

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open("taski.json", "r") as data_file:
            self.data = json.load(data_file)
            
    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.data