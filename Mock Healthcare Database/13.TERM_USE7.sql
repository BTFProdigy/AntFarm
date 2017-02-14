SELECT apt.Phys_npi, ph.Phys_last + ', ' + ph.Phys_first AS 'Physician'
FROM appointment apt
JOIN Physician ph
ON ph.phys_npi = apt.phys_npi
WHERE Apt_date = CAST(GETDATE() AS DATE) OR Apt_date = CAST(GETDATE()+1 AS DATE)
GROUP BY ph.apt_max, apt.Phys_npi, ph.Phys_last, ph.Phys_first
HAVING COUNT(apt.Phys_npi) >= ph.apt_max;