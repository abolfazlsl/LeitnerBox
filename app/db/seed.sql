INSERT INTO slots (id, name, review_interval_days) VALUES 
(1, 'Slot 1', 1),
(2, 'Slot 2', 3),
(3, 'Slot 3', 7),
(4, 'Slot 4', 15),
(5, 'Slot 5', 30)
ON CONFLICT (id) DO NOTHING;
