CREATE PROCEDURE remove_insurance
@patient_arg DECIMAL
AS
BEGIN
	UPDATE patient
	SET patient.insurance_plan_code = NULL
	WHERE patient.patient_mrn = @patient_arg
END;