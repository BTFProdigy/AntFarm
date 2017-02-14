CREATE PROCEDURE UPDATE_patient_balance
@balance_arg DECIMAL,
@patient_arg DECIMAL
AS
BEGIN
UPDATE patient
SET patient.patient_balance = @balance_arg
WHERE patient.patient_mrn = @patient_arg;
END;