-- Create database
CREATE DATABASE IF NOT EXISTS logdb;
USE logdb;

-- Create logs table
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(50),
    ip VARCHAR(50),
    status VARCHAR(10)
);

-- Insert sample log data
INSERT INTO logs (user, ip, status) VALUES
('admin', '192.168.1.10', 'FAILED'),
('admin', '192.168.1.10', 'FAILED'),
('admin', '192.168.1.10', 'FAILED'),

('user1', '8.8.8.8', 'FAILED'),
('user1', '8.8.8.8', 'FAILED'),

('user2', '10.0.0.5', 'SUCCESS'),
('user2', '172.16.0.3', 'FAILED'),
('user2', '172.16.0.3', 'FAILED'),
('user2', '172.16.0.3', 'FAILED'),

('user3', '45.23.12.90', 'FAILED'),
('user3', '45.23.12.90', 'FAILED'),
('user3', '45.23.12.90', 'FAILED'),
('user3', '45.23.12.90', 'FAILED');