import unittest
from person import Person
from patient import Patient
from doctor import Doctor

"""
Here comes the hard part. You're going to program the hospital simulator.
Here's how it should work:

on_doctor_called passes in a doctor. It means that the doctor has been called
to help waiting patients. She may or may not already be with a patient, and
you'll need to check for that (remember the is_with_patient() function). If she
is busy, she cannot help any of the patients in the waiting room.

If the doctor is not busy, she can only help certain patients in the waiting
room. For instance, if her occupation is "Oncologist", she can only help patients
with the "Cancer" condition. The mapping of patient conditions to doctor
occupations is below.

    "Broken arm": "Emergency medicine",
    "Cancer": "Oncologist",
    "Stomach pain": "Gastroenterologist",
    "Kidney issues": "Urologist"

If there are no patients that the doctor can help, she goes into the list of
waiting doctors. If there is a patient that the doctor can help, the doctor
should be assigned that patient, and that patient should be removed from the
waiting room. The doctor should never enter the waiting list if she is helping
a patient.

~~~

on_patient_visit passes in a patient. It means that a sick patient has come to
get help from a doctor. The patient may or may not be insured. If he is not
insured, he should be turned away and not have the chance to see a doctor.

If the patient is insured, he should be matched up with an available doctor who
can help with his condition. Remember the mapping of conditions to doctor
specialities above. If there is a doctor available, the patient should be
assigned to the doctor, and he should not enter the waiting room. Additionally,
The doctor who is helping the patient should be removed from the list of waiting
doctors.

If there are no doctors that can help the patient, the patient should enter the 
waiting room for the next available doctor.

~~~

Remember the functions of the patients and doctors that you programmed earlier!
You'll need them to get the necessary information from the doctors and patients
that are passed into the hospital.

Use flow control (if / else conditions, for / while loops) to help you. You
may need to iterate through the list of waiting patients or waiting doctors. The
tests for the hospital are at the bottom of this text file. As before, run
the tests from the command line while in this directory.

    python hospital.py

Feel free to go back and change your implementation of doctors and patients.
However, as long as you passed the tests for doctors and patients, you shouldn't
have to change anything with them. If you do change those classes, it would be
beneficial to ensure that your implementations remain consistent by running the
tests again.
"""


class Hospital:

    # Don't touch me. I hold variables that are necessary for a hospital
    def __init__(self):
        # If there's no patients to help, doctors go into this list
        # When doctors are helping patients, they should not be in this list
        self.doctors = []   # The doctor waiting area

        # If there are no doctors that can help the condition, patients
        # are in the waiting room.
        # When they are being helped by a doctor, they are not in the
        # waiting room.
        self.patients = []  # The patient waiting room

    # Fix me!
    def on_doctor_called(self, doctor):
        # This doesn't work! Modify the on_doctor_called method to satisfy
        # the simulation. You'll find the two methods below helpful

        # This method adds a doctor to the list of available doctors
        self.doctors.append(doctor)

        # This method removes the doctor in the () from the waiting area
        self.doctors.remove(doctor)

        # Remember the functions of the doctor you programmed earlier!
        speciality = doctor.get_occupation()
        busy = doctor.is_with_patient()

    # Fix me!
    def on_patient_visit(self, patient):
        # This doesn't work! Modify the on_patient_visit method to satisfy
        # the simulation. You'll find the two methods below helpful.

        # This method adds patients to the waiting room
        self.patients.append(patient)

        # This method removes the patient in the () from the waiting room
        self.patients.remove(patient)

        # Remember the functions of the patient you programmed earlier!
        problem = patient.get_condition()


"""
Tests of your work are below. Do not edit anything below this line!
Run the tests from the command line when this directory is your current working
directory:

    python hospital.py


"""
class TestHospital(unittest.TestCase):

    def setUp(self):
        self.h = Hospital()

    def test_patient_insurance(self):
        p = Patient("Don", "Broken arm")
        self.h.on_patient_visit(p)
        self.assertEqual(self.h.patients, [p], "Don should be in the waiting room!")

        ni = Patient("Kilichan", "Cancer", has_insurance=False)
        self.h.on_patient_visit(ni)
        self.assertEqual(self.h.patients, [p], "Kilichan didn't have insurance and was turned away!")

    def test_doctor_busy(self):
        d = Doctor("Joe", "Gastroenterologist")
        d.assign_patient(Patient("Someone", "Stomach pain"))
        self.h.on_doctor_called(d)

        self.assertEqual(self.h.doctors, [], "That doctor was busy and should not be waiting for anyone!")

        dd = Doctor("Edward", "Emergency medicine")
        self.h.on_doctor_called(dd)
        self.assertEqual(self.h.doctors, [dd], "That doctor was busy and should not be waiting for anyone!")

    def test_patient_first(self):

        p = Patient("Alan", "Broken arm")
        self.h.on_patient_visit(p)
        self.assertEqual(self.h.patients, [p], "Alan should be waiting for an ER doctor!")

        d = Doctor("Larry", "Emergency medicine")
        self.h.on_doctor_called(d)
        self.assertTrue(d.is_with_patient(), "The doctor should be seeing the patient with the broken arm!")

    def test_doctor_first(self):

        d = Doctor("Jack", "Urologist")
        self.h.on_doctor_called(d)
        self.assertIsNotNone(self.h.doctors, "The doctor should be waiting for a patient!")

        p = Patient("Alicia", "Kidney issues")
        self.h.on_patient_visit(p)
        self.assertTrue(d.is_with_patient(), "The doctor should be seeing the patient!")
        self.assertEqual(self.h.patients, [], "There should be no patients in the waiting room!")

        pp = Patient("Edward", "Kidney issues")
        self.h.on_patient_visit(pp)
        self.assertEqual(self.h.patients, [pp], "The new patient should be waiting for the urologist")
        self.h.on_doctor_called(d)
        self.assertEqual(self.h.patients, [pp], "The urologist is still with his other patient, "
                                                "even though he was called! "
                                                "The patient should still be waiting!")

        self.assertEqual(self.h.doctors, [], "There should be no available doctors!")

    def test_patient_doc_match(self):
        p = Patient("Joe", "Broken arm")
        d = Doctor("Lil Dicky", "Urologist")
        c = Doctor("Alicia", "Oncologist")

        self.h.on_patient_visit(p)
        self.assertEqual(self.h.patients, [p], "Joe with the broken arm should be in the waiting room!")

        self.h.on_doctor_called(c)
        self.h.on_doctor_called(d)
        self.assertEqual(self.h.doctors, [c, d], "Lil Dicky the urologist should be waiting for a patient!")

        n = Patient("Suzzy", "Stomach pain")
        m = Doctor("Alan", "Gastroenterologist")

        self.h.on_patient_visit(n)
        self.assertEqual(self.h.patients, [p, n], "There should be two patients in the waiting room!")

        self.h.on_doctor_called(m)
        self.assertEqual(self.h.patients, [p], "Suzzy with the stomach pain was help! "
                                               "Joe with the broken arm should be waiting!")
        self.assertEqual(self.h.doctors, [c, d], "Lil Dicky the urologist should be waiting for a patient!")
        self.assertTrue(m.is_with_patient(), "Alan the gastroenterologist should be helping Suzzy!")

        a = Doctor("Ian", "Emergency medicine")
        self.h.on_doctor_called(a)
        self.assertEqual(self.h.patients, [], "The ER doctor arrived! There should be no one left to help")
        self.assertEqual(self.h.doctors, [c, d], "Lil Dicky the urologist should be waiting for a patient!")

        s = Patient("Nate", "Cancer")
        self.h.on_patient_visit(s)
        self.assertEqual(self.h.patients, [], "The oncologist is available! There should be no one left to help")
        self.assertEqual(self.h.doctors, [d], "Lil Dicky the urologist should be waiting for a patient!")

        ki = Patient("Angela", "Kidney issues")
        self.h.on_patient_visit(ki)
        self.assertEqual(self.h.patients, [], "The urologist is available! There should be no one left to help")
        self.assertEqual(self.h.doctors, [], "All the doctors should be helping people!")

    def test_too_many_patients(self):
        n = 100
        many = [None] * n
        for i in range(n):
            many[i] = Patient("SameName", "Kidney issues")

        for p in many:
            self.h.on_patient_visit(p)

        self.assertEqual(self.h.patients, many, "There should be 100 patients waiting for the urologist!")

        er = Doctor("Mark", "Urologist")
        self.h.on_doctor_called(er)

        self.assertTrue(er.is_with_patient(), "The urologist should be seeing one of those 100 patients!")
        self.assertEqual(self.h.patients, many[1:n], "One of the patients should have been helped!")
        self.assertEqual(self.h.doctors, [], "There's so many patients to help! The urologist shouldn't be waiting around")

        er.current_patient = None
        self.assertFalse(er.is_with_patient(), "The urologist finished with a patient and should be free!")

        for j in range(1, n):
            self.h.on_doctor_called(er)
            self.assertTrue(er.is_with_patient(), "The urologist should be seeing one of those 100 patients!")
            self.assertEqual(self.h.patients, many[j+1:n], "One of the patients should have been helped!")
            self.assertEqual(self.h.doctors, [], "There's so many patients to help! The urologist shouldn't be waiting around")
            er.current_patient = None

        for i in range(n):
            many[i] = Patient("NotInsured", "Stomach pain", has_insurance=False)

        for p in many:
            self.h.on_patient_visit(p)

        self.assertEqual(self.h.patients, [], "None of those people had insurance!")

if __name__ == '__main__':
    unittest.main()
