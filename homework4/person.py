class Person:
    def __init__(self, id: int, fio: str, card_number: int, hash_pass: int, login: str):
        self.id = id
        self.fio = fio
        self.card_number = card_number
        self.hash_pass = hash_pass
        self.login = login

    def get_id(self):
        pass

    def get_fio(self):
        pass

    def get_login(self):
        pass

    def set_login(self, login):
        self.login = login

    def get_hash_pass(self):
        pass

    def set_hash_pass(self, hash_pass):
        self.hash_pass = hash_pass