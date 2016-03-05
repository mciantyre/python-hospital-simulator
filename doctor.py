"""
A doctor class. A doctor is a type of person. His speciality is one of the
following strings:

    "Emergency medicine"
    "Oncologist"
    "Gastroenterologist"
    "Urologist"

These match up to the patients' conditions.
The doctor's speciality will be returned in the get_occupation method.

Doctors can be with patients, they can be assigned patients by the hospital,
and they can say whether they are with or not with a patient.
"""

from person import Person
from patient import Patient
import unittest


class Doctor(Person):

    def __init__(self, name, occupation):
        super().__init__(name, occupation)
        self.current_patient = None

    # Doctors can say which patient they are with
    # Return the patient this doctor is seeing.
    # If he is not with a patient, he should return None
    def get_current_patient(self):
        pass # Remove the pass and this comment with your implementation

    # This method takes a parameter 'patient' and assigns it to the doctor's
    # current patient. This function is similar to the __init__ methods you've
    # seen earlier. That is, __init__ takes in a parameter, and assigns it to
    # the various 'self' variables. Implement that functionality here.
    def assign_patient(self, patient):
        pass # Remove the pass and this comment with your implementation

    # This method should return True if the doctor has a current patient, and
    # False if the doctor is not with a patient.
    def is_with_patient(self):
        pass # remove the pass and this comment with your implementation

"""
Don't edit anything below this line! Below is the test case of the doctor you
created. If you implemented all of the functions correctly, you'll pass all of
these tests. It's immediate feedback for your work! You can run the tests from
the command line:

(1) Change directory to the same directory as this file
(2) Run the command

        python doctor.py

(3) Look at the output from the command line. Did you pass all the tests?
"""
class TestDoctor(unittest.TestCase):

    def setUp(self):
        self.d = Doctor("Samosky", "Anesthesiologist")

    def test_doctor(self):
        self.assertIsNotNone(self.d.get_occupation(), "The doctor cannot announce his speciality!")
        self.assertEqual(self.d.get_occupation(), "Anesthesiologist",
                         "The doctor lied about his speciality!")

    def test_patient_interaction(self):
        patient = Patient("Don", "Entrepreneur", "Kidney issues")
        self.assertFalse(self.d.is_with_patient(),
                         "The doctor lied about being with a patient! He said he was with a patient, "
                         "but that's incorrect")
        self.d.assign_patient(patient)
        self.assertTrue(self.d.is_with_patient(), "The doctor lied about being with a patient! "
                                                  "He said he was available when he was with a patient")
        self.assertEqual(self.d.get_current_patient(), patient, "The doctor lied about the patient he was with!")

if __name__ == '__main__':
    unittest.main()