"""
A patient class.

It's a special type of person. He has a condition, a condition priority level,
and an insurance boolean. A condition is one of the following strings:

    "Broken arm"
    "Cancer"
    "Stomach pain"
    "Kidney issues"

These match up with what the doctors are able to fix.
"""

from person import Person
import unittest


class Patient(Person):

    # We assume patients have insurance. Thanks Obama...
    def __init__(self, name, condition, has_insurance=True, priority="LOW"):
        super().__init__(name, occupation="Who cares? This person is sick!")
        self.condition = condition
        self.insured = has_insurance
        self.priority = priority

    # Return the medical condition of this patient as a string.
    def get_condition(self):
        pass # Remove the pass and this comment with your implementation

    # When asked if the person is insured, he should return True or False
    # Take a look at the __init__ method and what the has_insurance
    # parameter is. Make sure it's a boolean, see where it is assigned, and
    # Return the corresponding 'self' variable in the __init__ function.
    def is_insured(self):
        pass # Remove the pass and this comment with your implementation

    # Return the condition priority of the patient. This will be used for
    # patient triaging in the hospital
    def get_priority(self):
        pass # Remove the pass and this comment with your implementation

"""
Don't edit anything below this line! Below is the test case of the patient you
created. If you implemented all of the functions correctly, you'll pass all of
these tests. It's immediate feedback for your work! You can run the tests from
the command line:

(1) Change directory to the same directory as this file
(2) Run the command

        python patient.py

(3) Look at the output from the command line. Did you pass all the tests?
"""
class TestPatient(unittest.TestCase):

    def setUp(self):
        # Dr G is a risk taker. He broke his arm, and he has no insurance
        self.p = Patient("Kilichan", "Broken arm", has_insurance=False)

    def test_get_condition(self):
        self.assertIsNotNone(self.p.get_condition(),
                             "The patient cannot say his condition!")
        self.assertEqual("Broken arm", self.p.get_condition(), "The patient did not say the correct condition!")

    def test_has_insurance(self):
        self.assertIsNotNone(self.p.is_insured(),
                             "There is no way to know if the person has insurance!")
        self.assertEqual(False, self.p.is_insured(), "The patient lied about his insurance!")

if __name__ == '__main__':
    unittest.main()