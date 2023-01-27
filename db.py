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

    def save(self):
        with open('db.json', 'w') as f:
            f.write('')
            f.write(json.dumps(self.data, indent=4))

    def add_user(self, user_id: str):
        self.data[user_id] = {
            'like': 0,
            'dislike': 0
        }
        self.save()
    
    def increase_like(self, user_id: str):
        self.data[user_id]['like'] += 1
        self.save()
    
    def increase_dislike(self, user_id: str):
        self.data[user_id]['dislike'] += 1
        self.save()

    def get_likes(self, user_id: str) -> dict:
        return self.data[user_id]


db = DB()
db.increase_like('51514352')
db.increase_like('51514352')
db.increase_like('51514352')
db.increase_like('51514352')
db.increase_like('51514352')
print(db.get_data())


