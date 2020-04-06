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
numPatients = 50
maxVisits = 5

# Doctor
for id in range (10, 10 + numDoctors):
    phrase = fake_data.word()
    password = "pbkdf2:sha256:150000$" + hashlib.sha256(phrase.encode()).hexdigest()
    statement = ("INSERT INTO public.\"Doctors\" Values (" + str(id) + ", '" + fake_data.name()
                 + "', '" + password + "');\n")
    fw.write(statement)

# Patient
for id in range (0, numPatients):
    phone = (str(fake_data.random_digit()) + str(fake_data.random_digit()) + 
             str(fake_data.random_digit()) + str(fake_data.random_digit()) + 
             str(fake_data.random_digit()) + str(fake_data.random_digit()))
    dob = fake_data.date_of_birth()
    myDob = dob.strftime('%Y-%m-%d')
    statement = ("INSERT INTO public.\"Patients\" Values (" + str(id) + ", '" + fake_data.first_name()
                 + "', '" + fake_data.last_name() + "', '" + myDob + "', '" 
                 + fake_data.email() + "', '" + fake_data.address() + "', '"
                 + str(2560712) + str(phone) + "');\n")
    fw.write(statement)

visitId = 0
# Visit
for patientid in range(0, numPatients):
    for id in range(0, math.ceil(random.random() * maxVisits)):
        statement = ("INSERT INTO public.\"Visits\" Values (" + str(visitId) + ", '"
                     + str(fake_data.random_int(25, 200)) + "', '"
                     + str(fake_data.random_int(1, 100)) + "', '"
                     + fake_data.text()[0:1000] + "', '" #patient history
                     + fake_data.text()[0:500] + "', '" #symptoms
                     + fake_data.text()[0:500] + "', '" #diagnostics
                     + fake_data.text()[0:500] + "', '" #comorbidities
                     + fake_data.text()[0:1000] + "', '" #previous_treatment
                     + fake_data.text()[0:500] + "', '" #current_treatment
                     + fake_data.text()[0:250] + "', '" #current_medication
                     + fake_data.text()[0:250] + "', '" #current_med_dose
                     + fake_data.text()[0:500] + "', " #current_med_freq
                     + str(10 + math.floor(random.random() * numDoctors)) + ", " #doctorid
                     + str(math.floor(random.random() * numPatients)) + ");\n") #patientid
        visitId += 1
        fw.write(statement)
fw.close()