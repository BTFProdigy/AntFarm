EXEC remove_insurance 111111;
EXEC remove_insurance 111114;

SELECT pt.patient_mrn, pt.Insurance_plan_code
FROM patient pt;
