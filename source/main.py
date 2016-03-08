'''
This is the main.py file that is used for a question and answer interface.
'''
import datetime
import os
import difflib
import random
from decimal import Decimal, getcontext
from source.question_answer import QA
from source.source1.shape_checker import get_triangle_type, get_quadrilateral_type
from utils.git_utils import get_git_file_info, get_file_info, get_repo_url, \
                            is_file_in_repo, get_repo_branch

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


MEASURE_TYPES = {"nano":1000000000, "micro":1000000, "milli":1000,
                 "centi":100, "deci":10, "":1, "deca":.1, "hecto":.01,
                 "kilo":.001, "mega":.000001, "giga":.000000001}


'''
The following pylint warning is disabled because I want a billion if and
return statements. It works just fine, darnit.
'''
# pylint: disable=too-many-return-statements,too-many-branches
def extended_ask(question=""):
    '''
    This is the extended version of an ask function for extended
    functionality.

    Arguments:
    question -- This string is a question to ask. If this question is not
                part of the extended functionality, this function will
                return None
                Default: ""
    '''
    if question[:5].lower() == "Rock:".lower():
        return rock_paper_scissors("rock")
    if question[:6].lower() == "Paper:".lower():
        return rock_paper_scissors("paper")
    if ((question[:7].lower() == "Is the ".lower()) and
            (question[-12:].lower() == " in the repo".lower())):
        filename = get_full_path(question[7:(len(question)-12)])
        return is_file_in_repo(filename)
    if question[:7].lower() == "Count: ".lower():
        alpha_num_count = 0
        for char in question[7:]:
            if not char.isspace():
                alpha_num_count += 1
        return alpha_num_count
    if question[:8].lower() == "Convert ".lower():
        q_args = question.split(' ')
        if len(q_args) == 5:
            try:
                float(q_args[1])
            except StandardError as exc:
                return str(exc)
            return convert_measure(float(q_args[1]),
                                   q_args[2].lower(), q_args[4].lower())
        else:
            return 'Argument count incorrect for conversion'
    if question[:9].lower() == "Scissors:".lower():
        return rock_paper_scissors("scissors")
    if ((question[:10].lower() == "Where did ".lower()) and
            (question[-10:].lower() == " come from".lower())):
        return get_repo_url(question[10:(len(question)-10)])
    if question[:11].lower() == "Backwards: ".lower():
        retstr = ""
        for char in reversed(question[11:]):
            retstr += char
        return retstr
    if question[:15].lower() == "What branch is ".lower():
        return get_repo_branch(get_full_path(question[15:]))
    if question[:18].lower() == "Word Commonality: ".lower():
        value = 0
        wordlist = open('4000CommonEnglishWords.txt', 'r')
        for line in wordlist:
            strcomp = line
            if strcomp.lower() == question[18:].lower()+'\n':
                return value
            value += 1
        return "Word not found in common words list: "+question[18:]
    if question[:22].lower() == "What is the status of ".lower():
        return get_git_file_info(get_full_path(question[22:]))
    if question[:22].lower() == "What is the deal with ".lower():
        return get_file_info(get_full_path(question[22:]))
    if question[:32].lower() == ("What is the HTML color code"+
                                 " for ").lower():
        check_color = ""
        for char in question[32:].lower():
            if char.isalpha():
                check_color += char
        colorlist = open('HTMLColorTable.txt', 'r')
        for line in colorlist:
            strcomp = line
            if strcomp.lower().split(' ')[0] == check_color:
                return strcomp.lower().split(' ')[1].upper().strip()
        return "Color not found"
    return None


def rock_paper_scissors(hand):
    '''
    This works as the AI for a rock, paper, scissors game.

    Arguments:
    hand -- This is a string for the player's choice of "rock", "paper",
            or "scissors"
    '''
    if hand == "rock":
        return ROCK_RET[random.randint(1, 3)]
    elif hand == "paper":
        return PAPER_RET[random.randint(1, 3)]
    elif hand == "scissors":
        return SCISSOR_RET[random.randint(1, 3)]


def random_d6_roll():
    '''
    Returns a random number from 1 to 6, as per a d6 dice roll
    '''
    return random.randint(1, 6)


def convert_measure_amount(amount, fromtype, totype):
    '''
    This converts numbers from one metric type to another metric type.

    Arguments:
    amount -- The float amount to convert
    fromtype -- The string type in metric, w/o "meter" to convert from
    totype -- The string type in metric, w/o "meter" to convert to
    '''
    if (fromtype not in MEASURE_TYPES) or (totype not in MEASURE_TYPES):
        return "Sorry, I can't convert that."
    total = (amount / MEASURE_TYPES[fromtype]) * MEASURE_TYPES[totype]
    if Decimal(total) == Decimal(1.0):
        return "1 "+totype+"meter"
    return str(float(total))+" "+totype+"meters"


def convert_measure(amount, fromtype, totype):
    '''
    This converts numbers from one metric type to another metric type.

    Arguments:
    amount -- The float amount to convert
    fromtype -- The string type in metric to convert from
    totype -- The string type in metric to convert to
    '''
    if ("meter" not in fromtype) or ("meter" not in totype):
        return "Sorry, I can't convert that."
    fromtype = fromtype.replace("meters", "")
    fromtype = fromtype.replace("meter", "")
    totype = totype.replace("meters", "")
    totype = totype.replace("meter", "")
    return convert_measure_amount(amount, fromtype, totype)


def get_full_path(filename):
    '''
    This retrieves the full path for a local file.

    Arguments:
    filename -- A string representing the local filename to append the full
                path to.
    '''
    if filename[1] != ':':
        if filename[0] != '\\':
            return os.getcwd()+'\\'+filename
        else:
            return os.getcwd()+filename
    else:
        return filename


def get_fibonacci_digit(digit):
    '''
    This retrieves the nth fibonacci number.

    Arguments:
    digit -- An integer for the nth fibonacci number.
    '''
    last_num = 0
    if digit > 1:
        num = 1
        count = 1
        while count < digit:
            temp_num = num
            num = last_num + temp_num
            last_num = temp_num
            count += 1
    return last_num


def get_pi_digit(digit):
    '''
    This returns the requested digit from pi as an int
    It uses the BBP digit extraction spigot algorithm by Simon Plouffe

    Arguments:
    digit -- An integer representing the nth pi digit to get
    '''
    if digit < 1:
        raise Exception("Error in get_pi_digit(): digit < 1")
    getcontext().prec = int(digit*2)
    last_calc = Decimal(0.0)
    for k in range(int(digit*2)):
        last_calc += Decimal(Decimal(1)/Decimal(16)**Decimal(k) *
                             (Decimal(4)/(Decimal(8)*Decimal(k)+Decimal(1)) -
                              Decimal(2)/(Decimal(8)*Decimal(k)+Decimal(4)) -
                              Decimal(1)/(Decimal(8)*Decimal(k)+Decimal(5)) -
                              Decimal(1)/(Decimal(8)*Decimal(k)+Decimal(6))))
    return int(str(Decimal(last_calc)/Decimal(10))[int(digit+1)])


def is_prime(number):
    '''
    This is used to determine if a given integer is a prime number.

    Arguments:
    number -- An integer to check for "primeness"
    '''
    for check_num in range(2, int(number)):
        if (int(number) % check_num) == 0:
            return False
    return True


def get_prime_number(place):
    '''
    This is used to get the nth prime number starting at 2

    Arguments:
    place -- An integer for the nth placed prime number.
    '''
    if place < 1:
        raise Exception("Error in get_prime_number(): place < 1")

    if place == 1:
        last_prime_num = 2
    else:
        last_prime_num = 3

    num_found = 2
    check_num = last_prime_num

    while num_found < place:
        check_num += 2
        if is_prime(check_num):
            last_prime_num = check_num
            num_found += 1
    return last_prime_num


ROCK_RET = {1:"Rock: Tie!", 2:"Paper: You lose!",
            3: "Scissors: You win!"}
PAPER_RET = {1:"Rock: You win!", 2:"Paper: Tie!",
             3: "Scissors: You lose!"}
SCISSOR_RET = {1:"Rock: You lose!", 2:"Paper: You win!",
               3:"Scissors: Tie!"}


class Interface(object):
    '''
    This class is used as an interface for asking questions and retrieving
    answers, allowing the user to set answers to their own questions.
    '''

    def __init__(self, filename="interface_output.txt", should_append=False):
        '''
        This is the init function for an Interface.

        Arguments:
        filename -- This string is the filename to use for log output
                    Default: "interface_output.txt"
        should_append -- This bool allows you to choose whether the output log
                         is appended to(True), or overwritten(False)
                         Default: False
        '''
        self.keywords = ['How', 'What', 'Where', 'Who', 'Why', 'Open', 'Roll']
        self.question_mark = chr(0x3F)
        self.user_name = ""

        self.question_answers = {
            'What type of triangle is ':
                QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ':
                QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it':
                QA('What time is it', datetime.datetime.now().isoformat()),
            'What is the digit of fibonacci':
                QA('What is the digit of fibonacci', get_fibonacci_digit),
            'What is the digit of pi':
                QA('What is the digit of pi', get_pi_digit),
            'Open the door hal':
                QA('Open the door hal', self.pod_bay),
            'What is the prime number':
                QA('What is the prime number', get_prime_number),
            'What directory is this using':
                QA('What directory is this using', os.getcwd),
            'Roll a D6':
                QA('Roll a D6', random_d6_roll)
        }
        self.last_question = None
        self.file_name = filename
        if isinstance(self.file_name, str) and (len(self.file_name) > 0):
            if should_append:
                self.open_file = open(filename, "a")
            else:
                self.open_file = open(filename, "w").close()
                self.open_file = open(filename, "w")
        else:
            raise Exception("Could not open log file for interface output.")


    def __enter__(self):
        '''
        __enter__ does nothing but return self.
        '''
        return self


    def __exit__(self, exception_type, exception_value, traceback):
        '''
        __exit__ closes the open log file.
        '''
        self.open_file.close()


    def pod_bay(self):
        '''
        This returns "I'm afraid I can't do that " followed by the user_name
        '''
        return "I'm afraid I can't do that "+self.user_name


    def ask(self, question=""):
        '''
        This function is used to ask the Interface a question.

        Arguments:
        question -- This string is a question to ask the interface.
                    Default: ""
        '''
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not a String!')
        self.open_file.write(question + " : ")
        if question[-1] == self.question_mark:
            extended_use = extended_ask(question[:len(question)-1])
        else:
            extended_use = extended_ask(question)
        if extended_use != None:
            self.open_file.write(str(extended_use)+"\n")
            return extended_use
        if (question.lower() not in (keyword.lower() for keyword in \
                                     self.question_answers.keys())) and \
                ((question[-1] != self.question_mark) or \
                (question.split(' ')[0].lower() not in (keyword.lower() for \
                                                keyword in self.keywords))):
            self.last_question = None
            self.open_file.write(NOT_A_QUESTION_RETURN+"\n")
            return NOT_A_QUESTION_RETURN
        parsed_question = ""
        args = []
        for keyword in question[:-1].split(' '):
            try:
                args.append(float(keyword))
            except StandardError as exc:
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question
        for answer in self.question_answers.values():
            if difflib.SequenceMatcher(a=answer.question.lower(),
                                       b=parsed_question.lower()).ratio() \
                                       >= .90:
                if answer.function is None:
                    self.open_file.write(str(answer.value)+"\n")
                    return answer.value
                else:
                    try:
                        self.open_file.write(str(answer.function(*args))+"\n")
                        return answer.function(*args)
                    except Exception as exc:
                        raise Exception("Error: "+str(exc))
        self.open_file.write(UNKNOWN_QUESTION+"\n")
        return UNKNOWN_QUESTION


    def teach(self, answer=""):
        '''
        This is used to teach the interface an answer to a previously asked
        question.

        Arguments:
        answer -- What you wish the answer to be to the question you just
                  asked.
        '''
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)


    def correct(self, answer=""):
        '''
        This is used to correct an answer to a previously asked question.

        Arguments:
        answer -- This is the answer you wish to change the previously
                  asked question to.
                  Default: ""
        '''
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)


    def __add_answer(self, answer):
        '''
        This is used to add an answer to the internal question and answer list.

        Arguments:
        answer -- The answer to change the question to.
        '''
        self.question_answers[self.last_question] = \
                QA(self.last_question, answer)


    def clear(self):
        '''
        This is used to clear out the questions and answers to the interface
        and reset back to default.
        '''
        self.question_answers = None
        self.__init__()


    def set_user(self, username):
        '''
        This sets the username.

        Arguments:
        username -- A string used for a username.
        '''
        self.user_name = username
        return "Hello, "+username+"."
