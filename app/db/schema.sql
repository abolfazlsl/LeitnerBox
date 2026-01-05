CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Slots table
CREATE TABLE slots (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    review_interval_days INT
);

-- Cards table
CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    slot_id INT REFERENCES slots(id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_reviewed_at DATE,
    next_review_at DATE
);

-- Card Reviews table
CREATE TABLE card_reviews (
    id SERIAL PRIMARY KEY,
    card_id INT REFERENCES cards(id) ON DELETE CASCADE,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN
);
