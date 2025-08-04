CREATE DATABASE BloodManagementSystem;
USE BloodManagementSystem;

CREATE TABLE Donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18 AND age <= 65),
    contact VARCHAR(15) UNIQUE NOT NULL,
    blood_type ENUM('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-') NOT NULL,
    donation_date DATE
);

CREATE TABLE BloodBanks (
    bank_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    contact VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE Recipients (
    recipient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    contact VARCHAR(15) UNIQUE NOT NULL,
    blood_type ENUM('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-') NOT NULL,
    request_date DATE NOT NULL,
    status ENUM('Pending', 'Completed', 'Rejected') DEFAULT 'Pending'
);

CREATE TABLE BloodInventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    bank_id INT,
    quantity INT CHECK (quantity >= 0),
    expiry_date DATE NOT NULL,
    blood_type ENUM('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-') NOT NULL,
    FOREIGN KEY (bank_id) REFERENCES BloodBanks(bank_id)
);

CREATE TABLE Hospitals (
    hospital_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    staff INT CHECK (staff >= 0),
    contact VARCHAR(15) UNIQUE NOT NULL
);
