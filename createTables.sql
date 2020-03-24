-- create the relational database tables

-- Patients Table

CREATE TABLE Patients(
    patient_id INT PRIMARY KEY,
    name_first VARCHAR(20),
    name_last VARCHAR(20),
    dob DATE,
    sex VARCHAR(6),
    phone INT,
    email VARCHAR(50),
    address VARCHAR(100),
    email VARCHAR(100),
    --visits                     --TODO: figure out how to store the list of visitids

);

CREATE TABLE Doctors(
  doctor_id INT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(100),
  admin BOOLEAN
);

CREATE TABLE Visits(
  visitid INT PRIMARY KEY,
  patient_id FOREIGN KEY REFERENCES Patients.patient_id,
  doctor_id FOREIGN KEY REFERENCES Doctors.doctor_id,
  visit_date DATETIME,
  weight FLOAT,
  height FLOAT,
  patient_history VARCHAR(500),
  symptoms VARCHAR(250),
  diagnostics VARCHAR(250),
  comorbidities VARCHAR(100),
  previous_treatment VARCHAR(250),
  current_treatment VARCHAR(250),
  current_medications VARCHAR(250),         --deal with this three medication related lists as strings, then separate into lists during analysis
  current_med_freq VARCHAR(20),
  current_med_dose VARCHAR(20)
);
