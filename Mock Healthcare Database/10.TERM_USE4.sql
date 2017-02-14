SELECT ph.Phys_first + ', ' + ph.Phys_last AS Physician
FROM physician ph
WHERE ph.phys_npi NOT IN (
			SELECT apt.Phys_npi 
			FROM appointment apt
			WHERE apt.patient_MRN = 111111)
ORDER BY phys_last;