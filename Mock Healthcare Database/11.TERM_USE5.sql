EXEC UPDATE_patient_balance 30, 111111;
EXEC UPDATE_patient_balance 40, 111115;
EXEC UPDATE_patient_balance 30, 111112;
EXEC UPDATE_patient_balance 50, 111117;

SELECT pt.patient_mrn, pt.Patient_balance
FROM patient pt;