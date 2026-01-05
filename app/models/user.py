class User:
    def __init__(self, id, username, password, created_at=None):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at
