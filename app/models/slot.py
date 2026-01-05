class Slot:
    def __init__(self, id, name, review_interval_days):
        self.id = id
        self.name = name
        self.review_interval_days = review_interval_days

    #Output of database -> Slot instance
    @staticmethod
    def from_dict(data):
        if not data:
            return None
        return Slot(
            id=data.get('id'),
            name=data.get('name'),
            review_interval_days=data.get('review_interval_days'),
        )