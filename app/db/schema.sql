-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Slots table
CREATE TABLE IF NOT EXISTS slots (
    id INTEGER PRIMARY KEY,
    delay_days INTEGER NOT NULL,
    note VARCHAR(255)
);

-- Cards table
CREATE TABLE IF NOT EXISTS cards (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    slot_id INTEGER REFERENCES slots(id) DEFAULT 1,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    last_reviewed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Card Reviews table
CREATE TABLE IF NOT EXISTS card_reviews (
    id SERIAL PRIMARY KEY,
    card_id INTEGER REFERENCES cards(id) ON DELETE CASCADE,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_correct BOOLEAN NOT NULL,
    from_slot INTEGER,
    to_slot INTEGER
);
