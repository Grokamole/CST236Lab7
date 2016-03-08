"""
Joseph Miller
CST236 - Lab 2
Test for source.shape_checker
"""
from unittest import TestCase
from source.main import Interface
from test.plugins.ReqTracer import requirements

def fave_color_function():
    """
    Gives a specific test string as a function.
    :return: "Blue. No, yellaaaaaah!"
    :rtype: str
    """
    return "Blue. No, yellaaaaaah!"

class TestInterface(TestCase):
    '''
    This class tests the QA interface for certain system requirements.
    '''
    @requirements(['#0006', '#0007', '#0014'])
    def test_main_how_question_asker(self):
        '''
        This tests the interface for unknown question response with how.
        '''
        result = Interface().ask("How are you?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0014'])
    def test_main_what_question_asker(self):
        '''
        This tests the interface for unknown question response with what.
        '''
        result = Interface().ask("What are you?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0014'])
    def test_main_where_question_asker(self):
        '''
        This tests the interface for unknown question response with where.
        '''
        result = Interface().ask("Where are you?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0014'])
    def test_main_why_question_asker(self):
        '''
        This tests the interface for unknown question response with why.
        '''
        result = Interface().ask("Why are you here?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0014'])
    def test_main_who_question_asker(self):
        '''
        This tests the interface for unknown question response with who.
        '''
        result = Interface().ask("Who are you?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0008'])
    def test_main_no_question_asker(self):
        '''
        This tests the interface for not asking a question.
        '''
        result = Interface().ask("Is that you?")
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0009'])
    def test_main_no_question_asked(self):
        '''
        This tests the interface for asking without a question mark.
        '''
        result = Interface().ask("Who are you")
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0010', '#0013'])
    def test_main_sep_spaced_words(self):
        '''
        This tests the interface for separarely spaced words.
        '''
        result = Interface().ask("What type of triangle is 3 3 3?")
        self.assertEqual(result, "equilateral")

    @requirements(['#0011'])
    def test_main_ninety_percent(self):
        '''
        This tests the interface for the 90% clause.
        '''
        result = Interface().ask("What typ of trangle is 4 4 4?")
        self.assertEqual(result, "equilateral")

    @requirements(['#0012'])
    def test_exclude_number(self):
        '''
        This tests the interface for number manueverability.
        '''
        result = Interface().ask("What type of 5 triangle is 5 5?")
        self.assertEqual(result, "equilateral")

    @requirements(['#0015'])
    def test_previous_question_answer(self):
        '''
        This tests the interface for previous question teaching.
        '''
        interface = Interface()
        interface.ask("What makes you think she is a witch?")
        interface.teach("Oh, she turned me into a newt!")
        result = interface.ask("What makes you think she is a witch?")
        self.assertEqual(result, "Oh, she turned me into a newt!")

    @requirements(['#0016', '#0020'])
    def test_stored_function_answer(self):
        '''
        This tests the interface for storing answers as functions.
        '''
        interface = Interface()
        interface.ask("What is your favorite color?")
        interface.teach(fave_color_function)
        result = interface.question_answers["What is your favorite color"]
        # pylint's recommended syntax does not work here
        # pylint: disable=singleton-comparison
        self.assertEqual(not (result.function == None), True)

    @requirements(['#0016', '#0020'])
    def test_stored_string_answer(self):
        '''
        This tests the interface for storing answers as strings.
        '''
        interface = Interface()
        interface.ask("What is your quest?")
        interface.teach("To seek the Holy Grail.")
        result = interface.question_answers["What is your quest"].value
        self.assertEqual(isinstance(result, str), True)

    @requirements(['#0017', '#0021'])
    def test_no_questions_asked(self):
        '''
        This tests the interface for not asking a question.
        '''
        result = Interface().teach("Weird.")
        self.assertEqual(result, "Please ask a question first")
        result = Interface().correct("Weird.")
        self.assertEqual(result, "Please ask a question first")

    @requirements(['#0018'])
    def test_noupdate_answer_question(self):
        '''
        This tests the interface for not updating an answer with teach().
        '''
        interface = Interface()
        interface.ask("What is your name?")
        interface.teach("My name is Sir Lancelot of Camelot.")
        interface.ask("What is your name?")
        result = interface.teach("Sir Robin of Camelot.")
        self.assertEqual(result, "I don\'t know about that. "+
                         "I was taught differently")

    @requirements(['#0019'])
    def test_update_answered_question(self):
        '''
        This tests the interface for updating an answer with correct().
        '''
        interface = Interface()
        interface.ask("What is your name?")
        interface.teach("My name is Sir Lancelot of Camelot.")
        interface.ask("What is your name?")
        interface.correct("Sir Robin of Camelot.")
        result = interface.ask("What is your name?")
        self.assertEqual(result, "Sir Robin of Camelot.")
