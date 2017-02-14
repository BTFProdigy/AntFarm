CREATE PROCEDURE add_waitlist
@waitlist_priority_arg DECIMAL(30),
@phys_npi_arg DECIMAL(12),
@patient_mrn_arg DECIMAL(12)
AS
BEGIN
	UPDATE waitlist 
SET waitlist_priority = waitlist_priority + 1 
WHERE waitlist_Priority >= @waitlist_priority_arg
AND @phys_npi_arg = waitlist.phys_npi;

INSERT INTO waitlist (waitlist_priority, phys_npi, patient_mrn, date_added)
VALUES (@waitlist_priority_arg, @phys_npi_arg, @patient_mrn_arg, GETDATE());
END;