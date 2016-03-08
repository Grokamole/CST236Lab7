'''
This file holds the QA class for a question and answer pair.

The following warning is disabled, because this ain't my code and I don't
know what I would add to this.
'''
# pylint: disable=too-few-public-methods
class QA(object):
    '''
    This class is used to hold a question string and either an answer value
    or an answer function.
    '''
    def __init__(self, question, answer):
        '''
        This sets up the QA object with a question and an answer.

        Arguments:
        question -- The question string to respond to an answer with.
        answer -- The answer that corresponds with the question as either
                  a value or a function.
        '''
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
