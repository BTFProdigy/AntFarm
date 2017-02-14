SELECT ph.Phys_first + ', ' + ph.Phys_last AS 'Physician',
		building.B_name AS 'Building'
FROM physician ph
JOIN building
ON ph.b_nr = building.b_nr
WHERE building.B_name = 'agnes' OR building.B_name = 'palladius'
ORDER BY B_name;