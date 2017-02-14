SELECT  patient.patient_last + ', ' + patient.patient_first AS Patient,
		insurance_plan.insurance_plan_name
FROM patient
JOIN insurance_plan
ON patient.insurance_plan_code = insurance_plan.insurance_plan_code
ORDER BY patient.patient_last;