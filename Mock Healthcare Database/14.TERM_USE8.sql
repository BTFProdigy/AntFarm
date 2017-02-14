SELECT	TOP 1 COUNT(pt.insurance_plan_code) AS 'Nr_enrolled',
		ip.Insurance_plan_code AS 'Plan Code', 
		ip.Insurance_plan_name AS 'Insurance Provider', 
		FORMAT(cp.copay_amt, 'C', 'en-us') AS 'Copay'
		
FROM patient pt
JOIN Insurance_plan ip
ON pt.Insurance_plan_code = ip.Insurance_plan_code
JOIN copay cp
ON ip.copay_code = cp.Copay_code
GROUP BY	pt.Insurance_plan_code, ip.Insurance_plan_code,
			ip.Insurance_plan_name, cp.Copay_amt, pt.Insurance_plan_code
ORDER BY Nr_enrolled DESC;