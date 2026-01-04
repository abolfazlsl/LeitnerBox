INSERT INTO slots (id, delay_days, note) VALUES 
(1, 1, 'First review: 1 day'),
(2, 3, 'Second review: 3 days'),
(3, 7, 'Third review: 7 days'),
(4, 15, 'Fourth review: 15 days'),
(5, 30, 'Fifth review: 30 days')
ON CONFLICT (id) DO NOTHING;
