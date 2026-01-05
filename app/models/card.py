class Card:
    def __init__(self, id, user_id, slot_id, question, answer, created_at=None, last_reviewed_at=None,
                 next_review_at=None):
        self.id = id
        self.user_id = user_id
        self.slot_id = slot_id
        self.question = question
        self.answer = answer
        self.created_at = created_at
        self.last_reviewed_at = last_reviewed_at
        self.next_review_at = next_review_at

    #Output of database -> Card instance
    @staticmethod
    def from_dict(data):
        if data is None:
            return None
        return Card(
            id=data.get('id'),
            user_id=data.get('user_id'),
            slot_id=data.get('slot_id'),
            question=data.get('question'),
            answer=data.get('answer'),
            created_at=data.get('created_at'),
            last_reviewed_at=data.get('last_reviewed_at'),
            next_review_at=data.get('next_review_at'),
        )
