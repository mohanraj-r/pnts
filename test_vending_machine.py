'''
Created on Jun 23, 2013

@author: mohanr
'''
import random
import string

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
#     invalid_input.description = None
    try:
        vend_pop(**test_data['inputs'])
    except test_data['error'] as exception:
        pass
    else:
        assert test_data['assert_msg']            


class TestVendingMachine(object):
    '''
    Tests for the vending machine.
    
    TODO:
    * Figure out a way to generate repetitive tests (e.g. invalid input) 
        - either using nose (which I already have experience in)
        - or unittest (ref: http://stackoverflow.com/questions/32899/how-to-generate-dynamic-parametrized-unit-tests-in-python)
    '''
    
    def __init__(self):
        self.invalid_input_tests = {
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
                                    
                                    'non_existing_pop_selection':{
                                                                  'test_name': 'Test by asking for a non-existing pop selection.',
                                                                  'inputs': {
                                                                             'pop_selection': _get_random_string(),
                                                                             'money_amount_paid': 1,
                                                                             },
                                                                  'error': ValueError,
                                                                  'error_msg': None,
                                                                  'assert_msg': 'Vending pop with a random string did not give expected error.'
                                                                  }
                                    }
        

    def test_invalid_inputs(self):
        ''' Test generator to test different combinations of invalid inputs. '''
        for test_name, test_data in self.invalid_input_tests.items():
            _invalid_input.description = test_data.get('test_name', test_name)
            yield _invalid_input, test_data


    def test_invalid_input_no_input(self):
        ''' Test without giving any input. The program takes non-optional arguments and hence should fail. '''
        try:
            vend_pop()
        except TypeError:
            pass
        else:
            assert 'Vending pop without input did not give expected error.'
   

    def test_invalid_input_zero_amount_paid(self):
        ''' Test with zero amount paid. '''
        try:
            vend_pop(pop_selection=_get_valid_random_pop(), money_amount_paid=0)
        except ValueError:
            pass
        else:
            assert 'Vending pop with no money did not give expected error.'


    def test_insufficient_amount(self):
        ''' Test by trying to get a pop with insufficient amount. '''
        pop = _get_valid_random_pop()
        cost = _get_cost_of_pop(pop)
        test_amount = cost - 1 
        try:
            vend_pop(pop_selection=pop, money_amount_paid=test_amount)
        except ValueError:
            pass
        else:
            assert 'Trying to purchase {} that costs {} with an insufficient amount of {} did not give expected error.'.format(pop, cost, test_amount)


    def test_change_returned(self):
        ''' Test if correct change is returned after a valid vending operation. '''
        pop = _get_valid_random_pop()
        cost = _get_cost_of_pop(pop)
        test_amount = cost + 1
        expected_change = test_amount - cost
        change_returned = vend_pop(pop_selection=pop, money_amount_paid=test_amount)
        assert change_returned == expected_change, 'Trying to purchase {} that costs {} with a amount of {} returned a change of {} instead of the expected change of {}'.format(pop, cost, test_amount, change_returned, expected_change)        
                

if __name__ == "__main__":
    nose.main()