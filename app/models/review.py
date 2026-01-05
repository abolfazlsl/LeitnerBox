class CardReview:
    def __init__(self, id,card_id,reviewed_at,success):
        self.id=id
        self.card_id=card_id
        self.reviewed_at=reviewed_at
        self.success=success

    @staticmethod
    def from_dict(data):
        if not data:
            return None
        return CardReview(
            id=data.get('id'),
            card_id=data.get('card_id'),
            reviewed_at=data.get('reviewed_at'),
            success=data.get('success'),
        )
