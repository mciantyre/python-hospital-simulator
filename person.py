"""
A person class.

You see, both a patient and a doctor are a type of person. So, I define the 
general behavior of a person in here, and it extends to any type of person, be
it a patient or a doctor. Essentially, all people have names and jobs.

Give the person below the ability to say his name! Then, patients and doctors can say 
say their names, too.
"""
import unittest


class Person:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    # Take a look at the get_occupation function below. See how it returns the
    # occupation of this person? The 'self' keyword referes to the current
    # Person. So, when asked for his job with get_occupation, he replies with
    # his job: self.occupation.
    # 
    # With that in mind, create a similar method that returns the person's name.
    # Look above at the __init__, or person set-up, method to see what the
    # name variable might be called.
    def get_name(self):
        pass # Replace the word 'pass' and this comment line with your answer

    def get_occupation(self):
        return self.occupation

"""
Don't edit anything below this line! Below is the test case of the person you
created. If you implemented all of the functions correctly, you'll pass all of
these tests. It's immediate feedback for your work! You can run the tests from
the command line:

(1) Change directory to the same directory as this file
(2) Run the command

        python person.py

(3) Look at the output from the command line. Did you pass all the tests?

"""
class TestPerson(unittest.TestCase):

    def setUp(self):
        self.subject = Person("Kilichan", "Professor")

    def test_person_has_name(self):
        self.assertIsNotNone(self.subject.get_name(), "The person can't say his name!")
        self.assertEqual("Kilichan", self.subject.get_name(), "The person did not say his correct name!")

    def test_person_has_occupation(self):
        self.assertIsNotNone(self.subject.get_occupation(),
                             "The person cannot say his occupation!")
        self.assertEqual("Professor", self.subject.get_occupation(), "The person did not say the correct job!")

if __name__ == '__main__':
    unittest.main()