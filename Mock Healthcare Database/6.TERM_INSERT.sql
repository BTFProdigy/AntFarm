INSERT INTO facility (facility_code, facility_name)
VALUES (1, 'Boston University Ambulatory Health Center');

INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (1, 'agnes', '1 fake street', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (2, 'palladius', '31 makeThisUp street', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (3, 'argent', '72 whysoblue', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (4, 'coopric', '1 fake street', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (5, 'tintin', '3 fake street', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (6, 'silver', '6 lovers lane', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (7, 'zinc', '38 dead end driver', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (8, 'titan', '78 fake street', 02115, 1 );
INSERT INTO building (B_nr, B_name, B_street, B_zip, facility_code)
VALUES (9, 'tintin', '90 rabbit hole street', 02115, 1 );

INSERT INTO copay(copay_code, copay_amt)
VALUES (100, 5);
INSERT INTO copay(copay_code, copay_amt)
VALUES (101, 10);
INSERT INTO copay(copay_code, copay_amt)
VALUES (102, 15);
INSERT INTO copay(copay_code, copay_amt)
VALUES (103,20);
INSERT INTO copay(copay_code, copay_amt)
VALUES (104, 25);
INSERT INTO copay(copay_code, copay_amt)
VALUES (105, 30);
INSERT INTO copay(copay_code, copay_amt)
VALUES (106, 35);
INSERT INTO copay(copay_code, copay_amt)
VALUES (107, 40);
INSERT INTO copay(copay_code, copay_amt)
VALUES (108, 45);
INSERT INTO copay(copay_code, copay_amt)
VALUES (109, 50);
INSERT INTO copay(copay_code, copay_amt)
VALUES (110, 55);

INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (200, 105, 'BCBS HMO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (201, 106, 'BCBS PPO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (202, 105, 'vanguard HMO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (203, 108, 'vanguard PPO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (204, 105, 'aetna HMO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (205, 107, 'aetna PPO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (206, 105, 'united health HMO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (207, 105, 'united health PPO');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (208, 104, 'medicare');
INSERT INTO Insurance_plan (insurance_plan_code, copay_code, insurance_plan_name)
VALUES (209, 110, 'cobra');

INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,100);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,101);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,102);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,103);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,104);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,105);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,106);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,107);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,108);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,109);
INSERT INTO coverage_network(facility_code, insurance_plan_code)
VALUES (1,110);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111111, 'Edward', 'Elrich', CAST('08-jun-1989' AS DATE), 111111111, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 200);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111112, 'alphonse', 'Elrich', CAST('08-jun-1989' AS DATE), 111111112, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 208);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111113, 'whinrey', 'rockbell', CAST('08-jun-1989' AS DATE), 111111113, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, NULL);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111114, 'reesa', 'hawkeye', CAST('08-jun-1989' AS DATE), 111111114, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 207);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111115, 'roy', 'mustang', CAST('08-jun-1989' AS DATE), 111111115, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 204);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111116, 'hinata', 'hyuga', CAST('08-jun-1989' AS DATE), 111111116, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 200);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111117, 'ella', 'windfall', CAST('08-jun-1989' AS DATE), 111111117, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 200);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111118, 'Greenly', 'Elder', CAST('08-jun-1989' AS DATE), 111111118, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 206);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111119, 'karen', 'king', CAST('08-jun-1989' AS DATE), 111111119, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 200);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111120, 'Matt', 'cobalt', CAST('08-jun-1989' AS DATE), 111111120, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 209);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111121, 'john', 'smith', CAST('08-jun-1989' AS DATE), 111111121, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 200);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111122, 'jane', 'cornell', CAST('08-jun-1989' AS DATE), 111111122, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 207);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111123, 'Ed', 'Dominic', CAST('08-jun-1989' AS DATE), 111111123, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, 204);

INSERT INTO patient (patient_mrn, patient_first, patient_last, patient_dob, patient_ssn, patient_street, patient_zip, patient_phone, patient_email, patient_balance, Insurance_plan_code)
VALUES (111124, 'zolo', 'calme', CAST('08-jun-1989' AS DATE), 111111124, '1 fake road', 02115, 6177810001, 'email@mail.com', 0, NULL);

INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400500, 'niko', 'robin', 1);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400501, 'Tony', 'Chopper', 2);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400502, 'Blue', 'Ivy', 3);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400503, 'robin', 'oak', 1);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400504, 'niko', 'pine',2);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400505, 'nena', 'dogwood', 3);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400506, 'michael', 'stone',7);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400507, 'john', 'snow', 4);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400508, 'susan', 'chestnut', 8);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400509, 'dana', 'beech', 2);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400510, 'kaeki', 'ash', 3);
INSERT INTO Physician (Phys_npi, phys_first, Phys_last, b_nr)
VALUES (300400511, 'Andy', 'berch', 2);

INSERT INTO specialty(specialty_code, specialty_type)
VALUES (100, 'Internal medicine');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (101, 'cardiology');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (102, 'neurology');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (103, 'interventional radiology');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (104, 'neonatal');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (105, 'Psychology');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (106, 'anesthesia');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (107, 'perfusion');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (108, 'gastroenterology');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (109, 'orthopedics');
INSERT INTO specialty(specialty_code, specialty_type)
VALUES (110, 'oncology');

INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400500, 100);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400501, 102);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400502, 103);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400503, 104);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400504, 105);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400505, 106);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400506, 107);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400507, 108);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400508, 109);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400509, 110);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400510, 109);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400511, 107);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400503, 102);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400505, 101);
INSERT INTO physician_directory (phys_npi, specialty_code)
VALUES (300400506, 100);

INSERT INTO appointment (phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111111, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111112, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111113, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111114, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111115, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111116, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111117, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111118, GETDATE());
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111119, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111120, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111121, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111122, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111123, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111124, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111111, GETDATE()+1);
INSERT INTO appointment ( phys_npi, patient_mrn, apt_date)
VALUES (300400508, 111112, GETDATE()+1);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111111, GETDATE());
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111111, GETDATE()+14);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111111, GETDATE()+21);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111116, GETDATE()+7);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111119, GETDATE()+14);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111120, GETDATE()+14);
INSERT INTO appointment ( Phys_npi, patient_MRN, Apt_date)
VALUES (300400506, 111124, GETDATE()+14);

EXEC add_waitlist 1, 300400500, 111111;
EXEC add_waitlist 2, 300400500, 111112;
EXEC add_waitlist 3, 300400500, 111113;
EXEC add_waitlist 4, 300400500, 111114;
EXEC add_waitlist 1, 300400501, 111115;
EXEC add_waitlist 2, 300400501, 111116;
EXEC add_waitlist 3, 300400501, 111117;
EXEC add_waitlist 4, 300400501, 111118;
EXEC add_waitlist 1, 300400502, 111119;
EXEC add_waitlist 2, 300400502, 111111;
EXEC add_waitlist 1, 300400504, 111122;
EXEC add_waitlist 2, 300400504, 111123;
EXEC add_waitlist 1, 300400505, 111124;
EXEC add_waitlist 2, 300400505, 111111;