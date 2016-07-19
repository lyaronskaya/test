#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


ALPHA_TOKEN_REGEX = r'[^\W\d_]+'
DIGIT_TOKEN_REGEX = r'\d+'


def getopt(s, options):
    '''
        The function parses command line options.
        
        Input:
        s : String, the string to parse.
        options : list of dictionaries {'name': String, 'has_arg': Bool, 'is_required': Bool}
        Output:
        Parsed parameters in the form of list of pairs (param_name, param_value).
    '''

    options_regex_list = []
    required_args_regex_list = []
    required_args_names = []
    param_value_regex = r'|'.join([ALPHA_TOKEN_REGEX, DIGIT_TOKEN_REGEX])
    for option in options:
        name = option['name']
        has_arg = option['has_arg']
        is_required = option['is_required']
        if has_arg:
            regex = re.compile('({0})[=,\s]({1})\s*'.format(name, param_value_regex), re.UNICODE)
        else:
            regex = re.compile('({0})\s*'.format(name), re.UNICODE)
        if is_required:
            required_args_regex_list.append(regex)
            required_args_names.append(name)
        else:
            options_regex_list.append(regex)
    str_params = s.split('--')
    parsed_params = []
    for i, regex in enumerate(required_args_regex_list):
        included = False
        for str_param in str_params:
            m = regex.match(str_param)
            if m:
                included = True
                param_name = m.group(1)
                param_value = None
                if len(m.groups()) == 2:
                    param_value = m.group(2)
                parsed_params.append((param_name, param_value))
        if not included:
            raise ValueError("Cann't find argument {}".format(required_args_names[i]))
    for regex in options_regex_list:
        for str_param in str_params:
            m = regex.match(str_param)
            if m:
                param_name = m.group(1)
                param_value = None
                if len(m.groups()) == 2:
                    param_value = m.group(2)
                parsed_params.append((param_name, param_value))
    return parsed_params
