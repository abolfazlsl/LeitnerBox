from app.db.connection import Database
from app.models.card import Card

class ReviewService:
    # TODO: [Member 2 & 3] Implement Review Logic.
    # Member 2: Define query to get cards where next_review_at <= CURRENT_DATE.
    # Member 3: Implement record_review(card_id, success) which:
    #    - Updates slot_id based on success
    #    - Updates last_reviewed_at and recalculates next_review_at using slots.review_interval_days
    #    - Inserts into card_reviews (success, reviewed_at)
    @staticmethod
    def get_due_cards(user_id):
        query = """
        SELECT c.* FROM cards c
        JOIN slots s ON c.slot_id = s.id
        WHERE c.user_id = %s
        AND(
        c.last_reviewed_at IS NULL OR
        (c.last_reviewed_at + (s.review_interval_days || 'days')::interval) <=CURRENT_DATE
        )
        AND c.slot_id < 6
                """
        with Database() as db:
            rows = db.fetch_all(query, (user_id,))
            return [Card.from_dict(row) for row in rows]
