class User:
    def __init__(self, id, username, password, created_at=None):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at

    @staticmethod
    def from_dict(data):
        if not data:
            return None
        return User(
            id=data.get('id'),
            username=data.get('username'),
            password=data.get('password'),
            created_at=data.get('created_at')
        )