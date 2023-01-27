import json

class DB:
    def __init__(self) -> None:
        with open('db.json') as f:
            source = f.read()
            if source != '':
                self.data = json.loads(source)
            else:
                self.data = {}
        

    def get_data(self):
        return self.data


db = DB()
print(db.get_data())
        

