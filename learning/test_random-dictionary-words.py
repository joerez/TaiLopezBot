import pytest
from random_dictionary_words import *

def setup_test():
    x = {}
    x['one'] = 1
    x['fish'] = 4
    x['two'] = 1
    x['red'] = 1
    x['blue'] = 1
    return x

def test_count_tokens():
    hist = setup_test()
    assert count_tokens(hist) == 8

# def test_show_all_types():
#     hist = setup_test()
#     types = show_all_types(hist)
#     assert types == ['one', 'fish', 'two', 'red', 'blue']
