-- Table: public."Doctors"

-- DROP TABLE public."Doctors";

CREATE TABLE public.doctors
(
    id integer NOT NULL DEFAULT nextval('user_id_seq'::regclass),
    username character varying(50) COLLATE pg_catalog."default",
    password character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

CREATE TABLE public.history
(
    id integer NOT NULL DEFAULT nextval('history_id_seq'::regclass),
    patientid integer NOT NULL,
    history character varying(1500) COLLATE pg_catalog."default",
    treatment character varying(1500) COLLATE pg_catalog."default",
    CONSTRAINT "hasHistory" FOREIGN KEY (patientid)
        REFERENCES public.patients (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE public.patients
(
    id integer NOT NULL,
    name_first character varying(35) COLLATE pg_catalog."default" NOT NULL,
    name_last character varying(35) COLLATE pg_catalog."default" NOT NULL,
    dob date NOT NULL,
    email character varying(254) COLLATE pg_catalog."default",
    address character varying(95) COLLATE pg_catalog."default",
    phone character varying(13) COLLATE pg_catalog."default",
    CONSTRAINT "Patients_pkey" PRIMARY KEY (id)
)

CREATE TABLE public.medication
(
    id integer NOT NULL,
    patientid integer NOT NULL,
    medication character varying(100) COLLATE pg_catalog."default" NOT NULL,
    dose character varying(50) COLLATE pg_catalog."default",
    frequency character varying(50) COLLATE pg_catalog."default",
    startdate date,
    enddate date,
    CONSTRAINT "Medication_pkey" PRIMARY KEY (id),
    CONSTRAINT "hasMeds" FOREIGN KEY (patientid)
        REFERENCES public.patients (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE public.visits
(
    id integer NOT NULL,
    weight integer,
    height integer,
    symptoms character varying(500) COLLATE pg_catalog."default",
    diagnostics character varying(500) COLLATE pg_catalog."default",
    comorbidities character varying(500) COLLATE pg_catalog."default",
    treatment character varying(500) COLLATE pg_catalog."default",
    doctorid integer NOT NULL,
    patientid integer NOT NULL,
    clinical_progress character varying(250) COLLATE pg_catalog."default",
    support_services character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT "Visits_pkey" PRIMARY KEY (id),
    CONSTRAINT "withDoctor" FOREIGN KEY (doctorid)
        REFERENCES public.doctors (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)