'''
Created on Jun 23, 2013

@author: mohanr
'''
import random
import string
import sys

import nose

from vending_machine import vend_pop, POP_VENDING_MACHINE


def _get_random_string(chars=string.letters, length=10):
    ''' Generate a random string with given chars and of given length. '''
    chars_len = len(chars) - 1
    random_string = ''.join([chars[random.randint(0, chars_len)] 
                             for _ in range(length)])
    return random_string


def _get_valid_random_pop(POP=POP_VENDING_MACHINE):
    ''' Get the name of a pop randomly from available pops. '''
    return POP.keys()[random.randint(0, len(POP)-1)]


def _get_cost_of_pop(pop):
    ''' Get cost of a given pop.''' 
    return POP_VENDING_MACHINE[pop]


def _invalid_input(test_data):
    try:
        vend_pop(**test_data['inputs'])
    except test_data['error'] as exception:
        expected_error_msg = test_data.get('error_msg')
        if expected_error_msg:
            assert expected_error_msg in str(exception), 'Expected error message "{}" not found in exception {}'.format(expected_error_msg, exception)
    else:
        assert False, test_data['assert_msg']            
        

class TestVendingMachine(object):
    ''' Tests for the vending machine. '''
    
    def __init__(self):
        # data structure from which tests will be generated 
        self.invalid_input_tests = {
                                    'no_input': {
                                                 'test_name': 'Test without giving any input. The program takes non-optional arguments and hence should fail.',
                                                 'inputs': {},
                                                 'error': TypeError,
                                                 'error_msg': None,
                                                 'assert_msg': 'Vending pop without input did not give expected error.',
                                                 },
                                    
                                    'null_input': {
                                                    'test_name': 'Test with Null inputs.',
                                                    'inputs': {
                                                                'pop_selection': None,
                                                                'money_amount_paid': None,
                                                                },
                                                    'error': TypeError,
                                                    'error_msg': None,
                                                    'assert_msg': 'Vending pop with null inputs did not give expected error.',
                                                    },
                                    
                                    'non_existing_pop_selection': {
                                                                   'test_name': 'Test by asking for a non-existing pop selection.',
                                                                   'inputs': {
                                                                              'pop_selection': _get_random_string(),
                                                                              'money_amount_paid': 1,
                                                                              },
                                                                   'error': ValueError,
                                                                   'error_msg': 'Invalid selection',
                                                                   'assert_msg': 'Vending pop with a non-existing selection did not give expected error.'
                                                                   },
                                    'zero_amount_paid': {
                                                         'test_name': 'Test with zero amount paid for a valid pop selection.',
                                                         'inputs': {
                                                                    'pop_selection': _get_valid_random_pop(),
                                                                    'money_amount_paid': 0,
                                                                    },
                                                         'error': ValueError,
                                                         'error_msg': 'Please insert coins',
                                                         'assert_msg': 'Vending pop with no money did not give expected error.'
                                                         },
                                    
                                    'negative_amount_paid': {
                                                             'test_name': 'Test with negative amount paid for a valid pop selection.',
                                                             'inputs': {
                                                                        'pop_selection': _get_valid_random_pop(),
                                                                        'money_amount_paid': -1,
                                                                        },
                                                             'error': ValueError,
                                                             'error_msg': 'Please insert coins',
                                                             'assert_msg': 'Vending pop with negative money did not give expected error.'
                                                             },
                                    
                                    }
        

    def test_invalid_inputs(self):
        ''' Test generator to test different combinations of invalid inputs. '''
        for test_name, test_data in self.invalid_input_tests.items():
            _invalid_input.description = test_data.get('test_name', test_name)
            yield _invalid_input, test_data


    def test_insufficient_amount(self):
        ''' Test by trying to get a pop with insufficient amount. '''
        pop = _get_valid_random_pop()
        cost = _get_cost_of_pop(pop)
        test_amount = cost - 1 
        try:
            vend_pop(pop_selection=pop, money_amount_paid=test_amount)
        except ValueError as exception:
            assert 'Not enough coins' in str(exception), 'Expected error message not in exception.'
        else:
            assert False, 'Trying to purchase {} that costs {} with an insufficient amount of {} did not give expected error.'.format(pop, cost, test_amount)


    def test_change_returned(self):
        ''' Test if correct change is returned after a valid vending operation. '''
        pop = _get_valid_random_pop()
        cost = _get_cost_of_pop(pop)
        test_amount = cost + 1
        expected_change = test_amount - cost
        change_returned = vend_pop(pop_selection=pop, money_amount_paid=test_amount)
        assert change_returned == expected_change, 'Trying to purchase {} that costs {} with a amount of {} returned a change of {} instead of the expected change of {}'.format(pop, cost, test_amount, change_returned, expected_change)        
                

if __name__ == "__main__":
    argv = sys.argv[:]
    argv.extend(['--verbose', '--with-coverage', '--cover-html', '--cover-package={}'.format('vending_machine')])    
    nose.main(argv=argv)