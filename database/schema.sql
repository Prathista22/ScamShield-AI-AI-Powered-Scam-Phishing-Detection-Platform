CREATE DATABASE IF NOT EXISTS scamshield;
USE scamshield;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS scan_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    input_type ENUM('text', 'url', 'image', 'qr') NOT NULL,
    raw_input TEXT NOT NULL,
    extracted_text TEXT NULL,
    risk_level ENUM('safe', 'suspicious', 'dangerous') NOT NULL,
    risk_score FLOAT NOT NULL,
    category VARCHAR(100) NOT NULL,
    reasons JSON NOT NULL,
    recommendation TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS model_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    version VARCHAR(50) NOT NULL,
    accuracy FLOAT,
    precision_score FLOAT,
    recall_score FLOAT,
    f1_score FLOAT,
    trained_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
