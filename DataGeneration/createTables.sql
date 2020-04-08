-- Table: public."Doctors"

-- DROP TABLE public."Doctors";

CREATE TABLE public."Doctors"
(
    doctorid integer NOT NULL DEFAULT nextval('user_id_seq'::regclass),
    username character varying(50) COLLATE pg_catalog."default",
    password character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (doctorid)
)

CREATE TABLE public."Patients"
(
    patientid integer NOT NULL,
    name_first character varying(35) COLLATE pg_catalog."default" NOT NULL,
    name_last character varying(35) COLLATE pg_catalog."default" NOT NULL,
    dob date NOT NULL,
    email character varying(254) COLLATE pg_catalog."default",
    address character varying(95) COLLATE pg_catalog."default",
    phone character varying(13) COLLATE pg_catalog."default",
    CONSTRAINT "Patients_pkey" PRIMARY KEY (patientid)
)

CREATE TABLE public."Medication"
(
    medid integer NOT NULL,
    patientid integer NOT NULL,
    medication character varying(100) COLLATE pg_catalog."default" NOT NULL,
    dose character varying(50) COLLATE pg_catalog."default",
    frequency character varying(50) COLLATE pg_catalog."default",
    startDate date,
    endDate date,
    CONSTRAINT "Medication_pkey" PRIMARY KEY (medid),
    CONSTRAINT "hasMeds" FOREIGN KEY (patientid)
        REFERENCES public."Patients" (patientid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE public."Visits"
(
    visitid integer NOT NULL,
    weight integer,
    height integer,
    patient_history character varying(1000) COLLATE pg_catalog."default",
    symptoms character varying(500) COLLATE pg_catalog."default",
    diagnostics character varying(500) COLLATE pg_catalog."default",
    comorbidities character varying(500) COLLATE pg_catalog."default",
    previous_treatment character varying(1000) COLLATE pg_catalog."default",
    current_treatment character varying(500) COLLATE pg_catalog."default",
    doctorid integer NOT NULL,
    patientid integer NOT NULL,
    CONSTRAINT "Visits_pkey" PRIMARY KEY (visitid),
    CONSTRAINT "forPatient" FOREIGN KEY (patientid)
        REFERENCES public."Patients" (patientid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "withDoctor" FOREIGN KEY (doctorid)
        REFERENCES public."Doctors" (doctorid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)