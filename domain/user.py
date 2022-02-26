class User:
    currentUser = None
    def __init__(self, name, password, level, pokepy_id):
        self.name = name
        self.password = password
        self.level = level
        self.pokepy_id = pokepy_id

