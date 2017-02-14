SELECT  ph.Phys_last +', '+ ph.Phys_first AS 'Physician',
		COUNT(nr.Phys_npi) AS 'Number of patients'		
FROM	(SELECT  DISTINCT ap.patient_MRN, ap.Phys_npi
		FROM appointment ap
		GROUP BY ap.patient_MRN, ap.Phys_npi) nr
RIGHT JOIN Physician ph
ON ph.Phys_NPI = nr.Phys_npi
GROUP BY ph.Phys_last, ph.Phys_first
ORDER BY [Number of patients] DESC;