"""
Joseph Miller
CST236 - Lab 7
Test for interface
"""
import datetime
import time
import os
from unittest import TestCase
import mock
from source.main import Interface
from test.plugins.ReqTracer import job_stories, requirements

class TestJobStoriesPart1(TestCase):
    '''
    This class is used as a test for the QA interface.
    '''
    @job_stories('When I ask "What time is it?" I want to be given '
                 +'the current date/time so I can stay up to date')
    def test_date_time(self):
        '''
        This function tests the interface for the corret time.
        '''
        interface = Interface()
        result = interface.ask("What time is it?")
        self.assertEqual(result[:17], datetime.datetime.now().isoformat()[:17])

    @job_stories('When I ask "What is the n digit of fibonacci" I want to '+
                 'receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_digit(self):
        '''
        This function tests the interface for the fibonacci sequence.
        '''
        interface = Interface()
        result = interface.ask("What is the 10 digit of fibonacci?")
        self.assertEqual(result, 34)

    @job_stories('When I ask "What is the n digit of pi" I want to receive'+
                 ' the answer so I don\'t have to figure it out myself')
    def test_pi_digit(self):
        '''
        This function tests the interface for pi digits.
        '''
        interface = Interface()
        result = interface.ask("What is the 5 digit of pi?")
        self.assertEqual(result, 5)

    @job_stories('When I ask "Please clear memory" I was the application'+
                 ' to clear user set questions and answers so I can reset'+
                 ' the application')
    def test_clear_qa_userquestions(self):
        '''
        This function tests the interface for clearing QA.
        '''
        interface = Interface()
        interface.ask("Who are you?")
        interface.teach("I am who I am.")
        interface.clear()
        result = interface.ask("Who are you?")
        self.assertNotEqual(result, "I am who I am.")

    @job_stories('When I say "Open the door hal", I want the application'+
                 ' to say "I\'m afraid I can\'t do that <user name> so I'+
                 ' know that is not an option')
    def test_open_door_hal(self):
        '''
        This function tests the interface for the 2001 spec.
        '''
        interface = Interface()
        interface.set_user("Dave")
        result = interface.ask("Open the door hal")
        self.assertEqual(result, "I'm afraid I can't do that Dave")

    @job_stories('When I use the interface, I want to be able to set a'+
                 ' username so that it recognizes my name as the user')
    def test_set_user_name(self):
        '''
        This function tests the interface for username recognition.
        '''
        interface = Interface()
        result = interface.set_user("Dave")
        self.assertEqual(result, "Hello, Dave.")

    @job_stories('When I ask "Convert <number> <units> to <units>" I want'+
                 ' to receive the converted value and units so I can know'+
                 ' the answer.')
    def test_convert_units_to_units(self):
        '''
        This function tests the interface for unit conversion.
        '''
        interface = Interface()
        result = interface.ask("Convert 1 meter to centimeters")
        self.assertEqual(result, "100.0 centimeters")

    @job_stories('When I ask for a numberic conversion I want at least 10'+
                 ' different units I can convert from/to')
    def test_numberic_conversion(self):
        '''
        This function tests the interface for multiple unit conversion.
        '''
        interface = Interface()
        result1 = interface.ask("Convert 1 meter to gigameters")
        self.assertEqual(result1, "1e-09 gigameters")
        result2 = interface.ask("Convert 1 meter to megameters")
        self.assertEqual(result2, "1e-06 megameters")
        result3 = interface.ask("Convert 1 meter to kilometers")
        self.assertEqual(result3, "0.001 kilometers")
        result4 = interface.ask("Convert 1 meter to hectometers")
        self.assertEqual(result4, "0.01 hectometers")
        result5 = interface.ask("Convert 10 meter to decameters")
        self.assertEqual(result5, "1 decameter")
        result6 = interface.ask("Convert 1 meter to decimeters")
        self.assertEqual(result6, "10.0 decimeters")
        result7 = interface.ask("Convert 1 meter to centimeters")
        self.assertEqual(result7, "100.0 centimeters")
        result8 = interface.ask("Convert 1 meter to millimeters")
        self.assertEqual(result8, "1000.0 millimeters")
        result9 = interface.ask("Convert 1 meter to micrometers")
        self.assertEqual(result9, "1000000.0 micrometers")
        result10 = interface.ask("Convert 1 meter to nanometers")
        self.assertEqual(result10, "1000000000.0 nanometers")

    @job_stories("When I ask for an unsupported number conversion, I want"+
                 " the interface to respond with \"Sorry, I can't convert"+
                 " that.\"")
    def test_numberic_no_conversion(self):
        '''
        This function tests the interface for incorrect unit conversion.
        '''
        interface = Interface()
        result = interface.ask("Convert 1 meter to quadrillometers")
        self.assertEqual(result, "Sorry, I can't convert that.")

    @job_stories('When I ask "What is the n prime number" I want to receive'+
                 ' the answer so I don\'t have to figure it out myself')
    def test_prime_number(self):
        '''
        This function tests the interface for prime number retrieval.
        '''
        interface = Interface()
        result = interface.ask("What is the 10 prime number?")
        self.assertEqual(result, 29)

    @job_stories('When I ask "What directory is this using" I want to'+
                 ' receive the answer so I know what directory it may'+
                 ' affect')
    def test_current_directory(self):
        '''
        This function tests the interface for current directory retrieval.
        '''
        interface = Interface()
        result = interface.ask("What directory is this using?")
        self.assertEqual(result.lower(), os.getcwd().lower())

    @job_stories('When I say "Roll a D6" I want to get a random integer from'+
                 ' 1 to 6 so that I don\'t have to roll a die')
    def test_d6(self):
        '''
        This function tests the interface for a random d6 roll.
        '''
        interface = Interface()
        result = interface.ask("Roll a D6")
        self.assertEqual((isinstance(result, int) and (result >= 1) and
                          (result <= 6)), True)

    @job_stories('When I send a string into the interface, I want it to'+
                 ' ignore case so that I don\'t have to consider case when'+
                 ' asking a question')
    def test_ignore_case(self):
        '''
        This function tests the interface for lower caseness.
        '''
        interface = Interface()
        result = interface.ask("roll a d6")
        self.assertEqual((isinstance(result, int) and (result > 0) and
                          (result < 7)), True)

    @requirements(['#0022'])
    def test_nonstring_ask(self):
        '''
        This function tests for failure of an incorrect value pass.
        '''
        try:
            Interface().ask(5)
            self.assertEqual('Not a String!', 'Did not throw Exception.')
        # ask returns a non-specific Exception
        # pylint:disable=broad-except
        except Exception as exc:
            self.assertEqual(isinstance(exc, Exception), True)

    @requirements(['#0023'])
    def test_convert_non_numeric(self):
        '''
        This function tests for interface failure on incorrect conversion.
        '''
        result = Interface().ask("Convert a meter to centimeters")
        self.assertEqual(result, 'could not convert string to float: a')

    @requirements(['#0024'])
    def test_incorrect_conversion_arg(self):
        '''
        This function tests for failure when converting w/o units.
        '''
        result = Interface().ask("Convert this!")
        self.assertEqual(result, 'Argument count incorrect for conversion')

    @requirements(['#0025'])
    def test_incorrect_conversion_typ(self):
        '''
        This function tests that the interface fails on incorrect conversion.
        '''
        result = Interface().ask("Convert 1 liter to meters")
        self.assertEqual(result, "Sorry, I can't convert that.")

    @requirements(['#0026'])
    def test_incorrect_pi_digit(self):
        '''
        This function tests for interface failure when getting pi digit.
        '''
        try:
            Interface().ask("What is the 0 digit of pi?")
            self.assertEqual('Exception', 'Did not throw Exception.')
        # ask returns a non-specific Exception
        # pylint:disable=broad-except
        except Exception as exc:
            self.assertEqual(isinstance(exc, Exception), True)

    @requirements(['#0027'])
    def test_incorrect_prime_place(self):
        '''
        This function tests for interface failure for nan prime numbers.
        '''
        try:
            Interface().ask("What is the 0 prime number?")
            self.assertEqual('Exception', 'Did not throw Exception.')
        # ask returns a non-specific Exception
        # pylint:disable=broad-except
        except Exception as exc:
            self.assertEqual(isinstance(exc, Exception), True)

    @requirements(['#0028'])
    def test_first_prime_number(self):
        '''
        This function tests the interface for the first prime number.
        '''
        result = Interface().ask("What is the 1 prime number?")
        self.assertEqual(result, 2)

class TestJobStoriesPart2(TestCase):
    '''
    This class is used as a test for the QA interface.
    '''
    @job_stories('When I say "Backwards: ", I want the proceeding string'+
                 ' to be repeated backwards to me so that I don\'t have to'+
                 ' type it out myself')
    def test_backwards_phrase(self):
        '''
        This function tests the interface for backwards string transformation.
        '''
        result = Interface().ask("Backwards: I live for evil")
        self.assertEqual(result, "live rof evil I")

    @job_stories('When I say "Count: ", I want the proceeding string to be'+
                 ' counted, ignoring whitespace, so that I don\'t have to'+
                 ' calculate it myself')
    def test_word_count(self):
        '''
        This function tests the interface for whitespace counting.
        '''
        result = Interface().ask("Count: This should be counted at 23")
        self.assertEqual(result, 23)

    @job_stories('When I say "Word Commonality: ", I want the proceeding'+
                 ' word to be checked to see where it places on the 4000'+
                 ' most used American English words list so that I don\'t'+
                 ' have to find it myself')
    def test_word_commonality(self):
        '''
        This function tests the interface for word commonality.
        '''
        result = Interface().ask("Word Commonality: the")
        self.assertEqual(result, 1)

    @requirements(['#0029'])
    def test_word_not_common(self):
        '''
        This function tests the interface for unknown word commonality.
        '''
        result = Interface().ask("Word Commonality: ZZZAX")
        self.assertEqual(result, "Word not found in common words list: ZZZAX")

    @job_stories('When I say "Rock:", "Paper:", or "Scissors:" I want the'+
                 ' system to respond with its random rock, paper, scissors'+
                 ' choice and tell me "You win!", "You lose!", or "Tie!"'+
                 ' depending on the case so that I can play by myself')
    def test_rock(self):
        '''
        This function tests the interface for rock in Rock Paper Scissors.
        '''
        result = Interface().ask("Rock:")
        self.assertEqual(True, ((result == "Rock: Tie!") or
                                (result == "Paper: You lose!") or
                                (result == "Scissors: You win!")))

    @job_stories('When I say "Rock:", "Paper:", or "Scissors:" I want the'+
                 ' system to respond with its random rock, paper, scissors'+
                 ' choice and tell me "You win!", "You lose!", or "Tie!"'+
                 ' depending on the case so that I can play by myself')
    def test_paper(self):
        '''
        This function tests the interface for paper in Rock Paper Scissors.
        '''
        result = Interface().ask("Paper:")
        self.assertEqual(True, ((result == "Rock: You win!") or
                                (result == "Paper: Tie!") or
                                (result == "Scissors: You lose!")))

    @job_stories('When I say "Rock:", "Paper:", or "Scissors:" I want the'+
                 ' system to respond with its random rock, paper, scissors'+
                 ' choice and tell me "You win!", "You lose!", or "Tie!"'+
                 ' depending on the case so that I can play by myself')
    def test_scissors(self):
        '''
        This function tests the interface for scissors in Rock Paper Scissors.
        '''
        result = Interface().ask("Scissors:")
        self.assertEqual(True, ((result == "Rock: You lose!") or
                                (result == "Paper: You win!") or
                                (result == "Scissors: Tie!")))

    @job_stories('When I ask "What is the HTML color code for color?" I want'+
                 ' the system to respond with the HTML HEX value for that'+
                 ' color so that I don\'t have to look it up')
    def test_color_code(self):
        '''
        This function tests the interface for HTML color coding.
        '''
        result = Interface().ask("What is the HTML color code for Lime?")
        self.assertEqual(result, "#00FF00")

    @requirements(['#0030'])
    def test_no_color_found(self):
        '''
        This function tests the interface for unknown HTML color coding.
        '''
        result = Interface().ask("What is the HTML color code for nothing?")
        self.assertEqual(result, 'Color not found')

    @requirements(['#0100'])
    @mock.patch('source.main.is_file_in_repo')
    def test_is_file_in_repo_yes(self, mock_repofile):
        '''
        This function tests the interface for files in the git repo.
        '''
        mock_repofile.return_value = "Yes"
        result = Interface().ask("Is the thing.txt in the repo?")
        self.assertEqual(result, "Yes")

    @requirements(['#0100'])
    @mock.patch('source.main.is_file_in_repo')
    def test_is_file_in_repo_no(self, mock_repofile):
        '''
        This function tests the interface for file not in the git repo.
        '''
        mock_repofile.return_value = "No"
        result = Interface().ask("Is the thing.txt in the repo?")
        self.assertEqual(result, "No")

    @requirements(['#0101'])
    @mock.patch('source.main.get_git_file_info')
    def test_get_git_stat_up_to_date(self, mock_git_status):
        '''
        This function tests the interface for git status.
        '''
        mock_git_status.return_value = "some_file.txt is up to date"
        result = Interface().ask("What is the status of some_file.txt?")
        self.assertEqual(result, "some_file.txt is up to date")

    @requirements(['#0101'])
    @mock.patch('source.main.get_git_file_info')
    def test_get_git_stat_not_checked(self, mock_git_status):
        '''
        This function tests the interface for unchecked git repo.
        '''
        mock_git_status.return_value = "some_file.txt has not been checked in"
        result = Interface().ask("What is the status of some_file.txt?")
        self.assertEqual(result, "some_file.txt has not been checked in")

    @requirements(['#0101'])
    @mock.patch('source.main.get_git_file_info')
    def test_get_git_stat_dirty_repo(self, mock_git_status):
        '''
        This function tests the interface for dirty git repo.
        '''
        mock_git_status.return_value = "some_file.txt is a dirty repo"
        result = Interface().ask("What is the status of some_file.txt?")
        self.assertEqual(result, "some_file.txt is a dirty repo")

    @requirements(['#0101'])
    @mock.patch('source.main.get_git_file_info')
    def test_get_git_stat_mod_locally(self, mock_git_status):
        '''
        This function tests the interface for locally modified git status.
        '''
        mock_git_status.return_value = ("some_file.txt has been modified"+
                                        " locally")
        result = Interface().ask("What is the status of some_file.txt?")
        self.assertEqual(result, "some_file.txt has been modified locally")

    @requirements(['#0102'])
    @mock.patch('source.main.get_file_info')
    def test_git_info(self, mock_get_file_info):
        '''
        This function tests the interface for file status.
        '''
        mock_get_file_info.return_value = ("648b739741418f03e37d73d2a42b82ef"+
                                           "f94c4b4f,Tue Feb 16 05:05:17 201"+
                                           "6 -0800,Joseph Miller")
        result = Interface().ask("What is the deal with c:\\projects\\python"+
                                 "\\cst236\\jospehm\\cst236_lab7\\source\\"+
                                 "main.py?")
        self.assertEqual(result, "648b739741418f03e37d73d2a42b82eff94c4b4f,"+
                         "Tue Feb 16 05:05:17 2016 -0800,Joseph"+
                         " Miller")

    @requirements(['#0103'])
    @mock.patch('source.main.get_repo_branch')
    def test_ask_what_branch(self, mock_get_branch):
        '''
        This function tests the interface for branch name.
        '''
        mock_get_branch.return_value = "master"
        result = Interface().ask("What branch is \\source\\main.py?")
        self.assertEqual(result, "master")

    @requirements(['#0104'])
    @mock.patch('source.main.get_repo_url')
    def test_where_did_file_come_from(self, mock_get_url):
        '''
        This function tests the interface for git repo url.
        '''
        mock_get_url.return_value = "https://github.com/OregonTech/JospehM"
        result = Interface().ask("Where did c:\\projects\\python\\cst236\\"+
                                 "\\jospehm\\cst236_lab7\\source\\main.py"+
                                 " come from?")
        self.assertEqual(result, "https://github.com/OregonTech/JospehM")

    @requirements(['#0050', '#0051'])
    def test_log_file_output(self):
        '''
        This function tests the interface for QA log output.
        '''
        with Interface("checkoutput.txt") as interface:
            interface.ask("What is the 10 prime number?")
        with open("checkoutput.txt") as check_output:
            result = check_output.readline().strip()
            self.assertEqual(result, "What is the 10 prime number? : 29")

    @requirements(['#0050', '#0051', '#0052'])
    def test_log_file_output_time(self):
        '''
        This performance function tests the prime number output.
        '''
        start_result = time.clock()

        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            with Interface("checkoutput.txt") as interface:
                interface.ask("What is the 10 prime number?")

        end_result = time.clock()

        with open("checkoutput.txt") as check_output:
            result = check_output.readline().strip()
        self.assertTrue((result == "What is the 10 prime number? : 29") and
                        (((end_result - start_result)/100) < .05))

class TestJobStoriesPart3(TestCase):
    '''
    This class is used as a test for the QA interface.
    '''
    @requirements(['#0050', '#0051', '#0053'])
    def test_append_log_file_output(self):
        '''
        This function tests the log file append feature.
        '''
        with open("checkoutput.txt", "w") as check_output:
            check_output.close()
        with Interface("checkoutput.txt", True) as interface:
            interface.ask("What is the 10 prime number?")
        with Interface("checkoutput.txt", True) as interface:
            interface.ask("What is the 11 prime number?")
        with open("checkoutput.txt", "r") as check_output:
            check_output.readline()
            result = check_output.readline().strip()
        self.assertEqual(result, "What is the 11 prime number? : 31")

    @requirements(['#0054'])
    def test_throw_log_not_string(self):
        '''
        This function tests the interface fails for non-string filename
        '''
        with self.assertRaises(Exception):
            Interface(1, True).ask("What is the 11 prime number?")

    @requirements(['#0031'])
    def test_color_code_timing(self):
        '''
        This performance function tests for HTML color code timing.
        '''
        start_result = time.clock()
        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            result = Interface().ask("What is the HTML color code for White?")
        end_result = time.clock()
        self.assertTrue(((result == "#FFFFFF") and
                         (((end_result - start_result)/100) < .01)))

    @requirements(['#0032'])
    def test_fib_timing(self):
        '''
        This performance function tests for fibonacci output timing.
        '''
        start_result = time.clock()
        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            result = Interface().ask("What is the 100 digit of fibonacci?")
        end_result = time.clock()
        self.assertTrue(((result == 218922995834555169026) and
                         (((end_result - start_result)/100) < .02)))

    @requirements(['#0033'])
    def test_dice_roll_timing(self):
        '''
        This performance function tests for random roll timing.
        '''
        start_result = time.clock()
        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            result = Interface().ask("Roll a D6")
        end_result = time.clock()
        self.assertTrue((((result < 7) and (result > 0)) and
                         (((end_result - start_result)/100) < .01)))

    @requirements(['#0034'])
    def test_backwards_string_timing(self):
        '''
        This function tests the interface for backwards string timing.
        '''
        start_result = time.clock()
        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            result = Interface().ask("Backwards: 123456789012345678901234567"+
                                     "89012345678901234567890")
        end_result = time.clock()
        self.assertTrue(((result == "098765432109876543210987654321098765432"+
                          "10987654321") and
                         (((end_result - start_result)/100) < .01)))

    @requirements(['#0035'])
    def test_commonality_timing(self):
        '''
        This performance function tests for word commonality finding timing.
        '''
        start_result = time.clock()
        # count is necessary for syntax, though it is not used
        # pylint: disable=unused-variable
        for count in range(0, 100):
            result = Interface().ask("Word Commonality: dictate")
        end_result = time.clock()
        self.assertTrue(((result == 4341) and
                         (((end_result - start_result)/100) < .025)))
