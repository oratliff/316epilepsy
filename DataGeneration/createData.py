# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:00:52 2020

@author: Rob
"""

from faker import Faker
fake_data = Faker()
import hashlib
from datetime import datetime
import random
import math

fw = open('createData.sql','w')

numDoctors = 10
numPatients = 100
maxVisits = 5
maxMedication = 3

# Doctor
for id in range (10, 10 + numDoctors):
    phrase = fake_data.word()
    password = "pbkdf2:sha256:150000$" + hashlib.sha256(phrase.encode()).hexdigest()
    statement = ("INSERT INTO public.doctors Values (" + str(id) + ", '" + fake_data.name()
                 + "', '" + password + "');\n")
    fw.write(statement)

# Patient
for id in range (0, numPatients):
    phone = (str(fake_data.random_digit()) + str(fake_data.random_digit()) + 
             str(fake_data.random_digit()) + str(fake_data.random_digit()) + 
             str(fake_data.random_digit()) + str(fake_data.random_digit()))
    dob = fake_data.date_of_birth()
    myDob = dob.strftime('%Y-%m-%d')
    statement = ("INSERT INTO public.patients Values (" + str(id) + ", '" + fake_data.first_name()
                 + "', '" + fake_data.last_name() + "', '" + myDob + "', '" 
                 + fake_data.email() + "', '" + fake_data.address() + "', '"
                 + str(2560712) + str(phone) + "');\n")
    fw.write(statement)

# Medication
med_names = ["hydrocodone/acetaminophen", "Simvastatin ", "Lisinopril", "Levothyroxine",
             "Azithromycin", "Metformin", "Lipitor", "Amlodipine",
             "Amoxicillin", "Hydrochlorothiazide"]

doses = ["25 mg", "50 mg", "75 mg", "100 mg", "1 pill", "2 pills", "50 mL", 
         "10 mL",   "20 mg / Kg", "5 mg / Kg"]

frequency = ["once a day", "twice a day", "as required", "hourly", "every morning", 
             "every night", "with lunch", "weekly", "every 4 hours", "every 8 hours"]
medid = 0
for patientid in range(0, numPatients):
    for med in range(0, math.ceil(random.random() * maxMedication)):
        start = fake_data.date_this_century()
        end = "NULL"
        if(random.random() > 0.5):
            end = fake_data.date_between_dates(date_start=start, date_end=None).strftime('%Y-%m-%d')
        start = start.strftime('%Y-%m-%d')
        statement = ("INSERT INTO public.medication VALUES (" + str(medid)
                     + ", " + str(patientid)
                     + ", '" + random.choice(med_names)
                     + "', '" + random.choice(doses)
                     + "', '" + random.choice(frequency)
                     + "', '" + start
                     + "', ")
        if(end == "NULL"):
            statement = statement + end + ");\n"
        else:
            statement = statement + "'" + end + "');\n"
        medid += 1
        fw.write(statement)


# Visit
visitId = 0
for patientid in range(0, numPatients):
    for id in range(0, math.ceil(random.random() * maxVisits)):
        statement = ("INSERT INTO public.visits Values (" + str(visitId) + ", '"
                     + str(fake_data.random_int(25, 200)) + "', '"
                     + str(fake_data.random_int(1, 100)) + "', '"
                     + fake_data.text()[0:500] + "', '" #symptoms
                     + fake_data.text()[0:500] + "', '" #diagnostics
                     + fake_data.text()[0:500] + "', '" #comorbidities
                     + fake_data.text()[0:500] + "', " #treatment
                     + str(10 + math.floor(random.random() * numDoctors)) + ", " #doctorid
                     + str(math.floor(random.random() * numPatients)) + ", '" #patientid
                     + fake_data.text()[0:250] + "', '" #clinical_progress
                     + fake_data.text()[0:500] + "');\n") #support_services
        visitId += 1
        fw.write(statement)

# History
historyId = 0
for patientid in range(0, numPatients):
    statement = ("INSERT INTO public.history Values (" + str(historyId) + ", "
                 + str(patientid) + ", '"
                 + fake_data.text()[0:1500] + "', '" #history
                 + fake_data.text()[0:1500] + "');\n") #treatment
    historyId += 1
    fw.write(statement)
fw.close()