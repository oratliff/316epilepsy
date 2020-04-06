--Login a Doctor
SELECT *
FROM public."Doctors"
WHERE username = 'kate';

--Get all Doctors Working
SELECT username
FROM public."Doctors";

--Test no doctor
SELECT *
FROM public."Doctors"
WHERE username = '';

--Test working username password pair
SELECT *
FROM public."Doctors"
WHERE username = 'kate' AND password = 'pbkdf2:sha256:150000$mQklhWU7$319a2be22b5e87faaf8efee10ae9616859aa46ef343674e1abfec8b63c20ad4e';

--Test wrong username password pair
SELECT *
FROM public."Doctors"
WHERE username = 'kate' AND password = 'pbkdf2:sha256:150000$mQklhWU7$aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';

--Get Patient Data
SELECT *
FROM public."Patients"
WHERE patientid = 1;

--Get Current Medication
SELECT current_med_dose, current_med_freq, current_medication
FROM public."Visits"
WHERE patientid = 1 AND visitid = (SELECT MAX(visitid) FROM public."Visits" WHERE patientid = 1)

--Get Patient History
SELECT patient_history
FROM public."Visits"
WHERE patientid = 1;

--Find all current medications
SELECT current_medication
FROM public."Visits";