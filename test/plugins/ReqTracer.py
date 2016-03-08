'''
This file contains a requirements tracing plugin.
'''
import logging

from nose2.events import Plugin

LOG = logging.getLogger('nose2.plugins.ReqTracer')


class ReqTracer(Plugin):
    '''
    This plugin traces code requirements.
    '''
    configSection = 'reqtracer'
    commandLineSwitch = (None, 'reqtracer', 'reqtracer enabled')
    def __init__(self):
        '''
        This initializer does nothing.
        '''
        pass
    # the following function name is excused since nose2 requires it to look
    # like this. Also, event is not used, but is the standard function def.
    # pylint: disable=invalid-name, unused-argument, no-self-use
    def afterSummaryReport(self, event):
        '''
        This outputs the requirements and job stories to a log file.

        Arguments:
        event -- unused. Required for nose2 plugin hook.
        '''
        output_file = open('Lab7RequirementOutput.txt', 'w')
        output_file.write('Requirements\n------------\n\n')
        for key, item in sorted(code_requirements.items()):
            output_file.write(key)
            for func in item.func_name:
                output_file.write(' '+func+',')
            output_file.write('\n')
        output_file.write('\nJob Stories\n-----------\n\n')
        for item in code_job_stories:
            output_file.write('*'+item.req_text+'\n\tfunctions: (')
            for func in item.func_name:
                output_file.write(func+',')
            output_file.write(')\n')


# This class works as a helper class, so it doesn't need useless methods
# pylint: disable=too-few-public-methods
class Trace(object):
    '''
    This class is used for tracing code requirements and job stories.
    It holds the id and a list of corresponding functions for such.
    '''
    req_text = ""
    def __init__(self, text):
        '''
        The initializer for a Trace plugin object.

        Arguments:
        text -- This holds the job story/requirement ID
        '''
        self.req_text = text
        self.func_name = []

# despite what pylint thinks, these are not constants.
# pylint: disable=invalid-name
code_requirements = {}
# pylint: disable=invalid-name
code_job_stories = []


def requirements(req_list):
    '''
    This serves as a wrapper to record code requirements.
    '''
    def wrapper(func):
        '''
        The wrapper portion of this function.
        '''
        def add_req_and_call(*args, **kwargs):
            '''
            Associates code requirements from Requirements.
            '''
            for req in req_list:
                if req not in code_requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                code_requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def job_stories(jstory):
    '''
    This serves as a wrapper to record job story requirements.
    '''
    def wrapper(func):
        '''
        The wrapper portion of this function.
        '''
        def add_jstory_and_call(*args, **kwargs):
            '''
            Associates job stories from JobStories.
            '''
            found_story = False
            for story in code_job_stories:
                if story.req_text == jstory:
                    story.func_name.append(func.__name__)
                    found_story = True
                    break
            if not found_story:
                raise Exception('Job Story ({0}) not defined'.format(jstory))
            return func(*args, **kwargs)

        return add_jstory_and_call

    return wrapper


with open('lab7requirements.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            code_requirements[req_id] = Trace(desc)
        elif (len(line) > 1) and (line[0] == '*'):
            job_id = line[1:].strip()
            code_job_stories.append(Trace(job_id))
