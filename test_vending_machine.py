'''
Created on Jun 23, 2013

@author: mohanr
'''
import random
import string
import unittest

from vending_machine import vend_pop


class Test(unittest.TestCase):
    
    @staticmethod
    def _generate_random_string(chars=string.letters, length=10):
        ''' Generate a random string with given chars and of given length. '''
        chars_len = len(chars) - 1
        random_string = ''.join([chars[random.randint(0, chars_len)] 
                                 for _ in range(length)])
        return random_string


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_invalid_input_no_input(self):
        ''' Test without giving any input. The program takes non-optional arguments and hence should fail. '''
        try:
            vend_pop()
        except TypeError:
            pass
        else:
            assert 'Vending pop without input did not yield expected error.'
   
    
    def test_invalid_input_null_inputs(self):
        ''' Test with Null inputs.  '''
        try:
            vend_pop(pop_selection=None, money_amount_paid=None)
        except TypeError:
            pass
        else:
            assert 'Vending pop with null inputs did not yield expected error.'


    def test_non_existing_pop_selection(self):
        ''' Test by asking for a non-existing pop selection. '''
        try:
            vend_pop(pop_selection=self._generate_random_string(), money_amount_paid=10)
        except ValueError:
            pass
        else:
            assert 'Vending pop with a random string did not yield expected error.'


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()