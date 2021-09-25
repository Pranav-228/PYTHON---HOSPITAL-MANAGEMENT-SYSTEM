import sqlite3
conn=sqlite3.connect("HospitalDB.db")

print("DATABASE CONNECTION SUCCESSFUL")

conn.execute("Drop table if EXISTS PATIENT")
c = conn.cursor()
conn.execute("""Create table PATIENT
            (PATIENT_ID int(10) primary key,
              NAME VARCHAR(20) not null,
              SEX varchar(10) not null,
              BLOOD_GROUP varchar(5) not null,
              DOB date not null,
              ADDRESS varchar(100) not null,
              CONSULT_TEAM varchar(50) not null,
              EMAIL varchar(20) not null
              );
              """)

print("PATIENT TABLE CREATED SUCCESSFULLY")

conn.execute("Drop table if EXISTS CONTACT_NO")
c = conn.cursor()
conn.execute("""CREATE TABLE CONTACT_NO
            (PATIENT_ID int(10) PRIMARY KEY,
             CONTACTNO int(15) not null,
             ALT_CONTACT int(15),
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
             );
             """)

print("CONTACT_NO TABLE CREATED SUCCESSFULLY")

conn.execute("Drop table if EXISTS employee")
c = conn.cursor()
conn.execute("""create table employee
            (EMP_ID varchar(10) primary key,
             EMP_NAME varchar(20)not null,
             SEX varchar(10) not null,
             AGE int(5) not null,
             DESIG varchar(20) not null,
             SAL int(10) not null,
             EXP varchar(100) not null,
             EMAIL varcahr(20) not null,
             PHONE int(12)
             );
             """)

print("EMPLOYEE TABLE CREATED SUCCESSFULLY")

conn.execute("Drop table if EXISTS APPOINTMENT")
c = conn.cursor()
c.execute("""create table appointment
            (
             PATIENT_ID int(20) not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) primary key,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
             FOREIGN KEY(PATIENT_ID) references PATIENT(PATIENT_ID),
             FOREIGN KEY(EMP_ID) references employee(EMP_ID)
             );
             """)
print("APPOINTMENT TABLE CREATED SUCCESSFULLY")
conn.commit()
conn.close()