SELECT	pt.patient_last+ ', ' + pt.patient_first AS 'Patient',
		ph.Phys_last + ', ' + ph.Phys_first AS 'Physician',
		COUNT(*) AS 'Visit Count'
FROM appointment ap
JOIN patient pt
ON ap.patient_MRN = pt.patient_mrn
JOIN Physician ph
ON ph.Phys_NPI = ap.Phys_npi
GROUP BY	pt.patient_last, pt.patient_first,
		Phys_last, ph.Phys_first
HAVING COUNT(*) > 1;