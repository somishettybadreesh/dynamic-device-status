INSERT INTO companies (name) VALUES ('Acme Corp'), ('Beta Ltd'), ('Gamma Inc');

INSERT INTO devices (company_id, name) VALUES
(1, 'Acme-Device-1'),
(1, 'Acme-Device-2'),
(1, 'Acme-Device-3'),
(2, 'Beta-Device-A'),
(2, 'Beta-Device-B'),
(3, 'Gamma-Device-1'),
(3, 'Gamma-Device-2');

-- Simulated readings (some old -> offline)
INSERT INTO device_readings (device_id, reading_value, created_at) VALUES
(1, 42, now()),                        -- online
(2, 33, now() - INTERVAL '3 minutes'), -- offline
(3, 21, now() - INTERVAL '1 minute'),  -- online
(4, 60, now() - INTERVAL '10 minutes'),-- offline
(5, 22, now() - INTERVAL '50 seconds'),-- online
(6, 55, now() - INTERVAL '5 minutes'), -- offline
(7, 10, now() - INTERVAL '20 seconds');-- online
