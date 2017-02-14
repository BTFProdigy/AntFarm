CREATE TABLE facility (
Facility_code 	DECIMAL(12) PRIMARY KEY,
Facility_name 	VARCHAR(60) NOT NULL
);

CREATE TABLE Copay(
Copay_code 	DECIMAL(12) UNIQUE NOT NULL,
Copay_amt 	DECIMAL(12) UNIQUE NOT NULL,
CONSTRAINT pk_copay PRIMARY KEY (copay_code, copay_amt)
);

CREATE TABLE Building (
B_nr 		DECIMAL(12) PRIMARY KEY,
B_name 		VARCHAR(30) NOT NULL,
B_street 	VARCHAR(30) NOT NULL,
B_zip 		DECIMAL(5) NOT NULL,
Facility_code 	DECIMAL(12) 
FOREIGN KEY REFERENCES facility(facility_code)
);

CREATE TABLE Insurance_plan(
Insurance_plan_code 	DECIMAL(12) PRIMARY KEY,
Copay_code		DECIMAL(12) 
CONSTRAINT copay_code_fk FOREIGN KEY REFERENCES copay(copay_code),
Insurance_plan_name 	VARCHAR(60)
);

CREATE TABLE coverage_network(
Facility_code 		DECIMAL(12),
insurance_plan_code 	DECIMAL(12)
CONSTRAINT pk_coverage_network PRIMARY KEY (facility_code, insurance_plan_code)
);


CREATE TABLE patient (
patient_mrn 		DECIMAL(12) PRIMARY KEY,
patient_first 		VARCHAR(30) NOT NULL,
patient_last 		VARCHAR(30) NOT NULL,
patient_dob 		DATE NOT NULL,
patient_ssn 		DECIMAL(9) UNIQUE NOT NULL,
patient_Street 		VARCHAR(30) NOT NULL,
patient_zip 		DECIMAL(5) NOT NULL,
patient_phone 		DECIMAL(10),
Patient_email 		VARCHAR(60),
Patient_balance 	DECIMAL(12,2) NOT NULL,
Insurance_plan_code 	DECIMAL(12)
FOREIGN KEY REFERENCES insurance_plan(insurance_plan_code)
);

CREATE TABLE Physician (
Phys_NPI 		DECIMAL(12) PRIMARY KEY,
Phys_first 		VARCHAR(30) NOT NULL,
Phys_last 		VARCHAR(30) NOT NULL,
B_nr 			DECIMAL(12),
apt_max 		INT NOT NULL DEFAULT 8
);

ALTER TABLE physician
ADD CONSTRAINT physician_fk FOREIGN KEY (b_nr) REFERENCES building(b_nr);


CREATE TABLE specialty(
Specialty_code 	DECIMAL(4) PRIMARY KEY,
Specialty_type 	VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE waitlist(
waitlist_id 				INT IDENTITY(1,1) PRIMARY KEY,
waitlist_priority 			DECIMAL(30),
phys_npi 				DECIMAL(12) NOT NULL 
CONSTRAINT waitlist_fk1		FOREIGN KEY REFERENCES physician(phys_npi), 
patient_mrn 				DECIMAL(12) NOT NULL
CONSTRAINT waitlist_fk2 	FOREIGN KEY REFERENCES patient(patient_mrn),
date_added 				DATE NOT NULL
);

CREATE UNIQUE INDEX waitlist_index
ON waitlist (Waitlist_priority, phys_npi);

CREATE TABLE Physician_directory(
Phys_npi 		DECIMAL(12) NOT NULL
CONSTRAINT Physician_directory_fk1 FOREIGN KEY REFERENCES physician(Phys_npi),
Specialty_code 		DECIMAL(4) NOT NULL
CONSTRAINT Physician_directory_fk2 FOREIGN KEY REFERENCES specialty(specialty_code),
CONSTRAINT pk_physician_directory PRIMARY KEY (phys_npi, specialty_code)
);

CREATE TABLE appointment(
Appointment_nr 		INT IDENTITY(1,1) PRIMARY KEY,
Phys_npi 		DECIMAL(12) NOT NULL
CONSTRAINT appointment_fk1 REFERENCES physician(phys_npi),
patient_MRN 		DECIMAL(12) NOT NULL
CONSTRAINT appointment_fk2 REFERENCES patient(patient_mrn),
Apt_date 		DATE NOT NULL
);

CREATE TABLE bill(
Invoice_nr			INT IDENTITY,
appointment_nr		DECIMAL(12) UNIQUE NOT NULL, 
Invoice_date		DATE NOT NULL DEFAULT GETDATE(),
Copay_amt			DECIMAL(12) NOT NULL,
Amt_paid			DECIMAL(12,2) NOT NULL DEFAULT 0,
CONSTRAINT pk_bill	PRIMARY KEY (invoice_nr, appointment_nr)
);