import unittest
from ..data_store import DataStore
from ..token_items import TokenArg

class TestDataSore(unittest.TestCase):
    def setUp(self):
        dico = {
            'AA' : '1',  # check tokeniser if argument contains number like PARAM_01
            'BB' : '2',
            'CCC' : '3'
        }
        DataStore(dico)

    def test_value_exists(self):
        val = DataStore.get_argument_value(TokenArg('BB'))
        self.assertEqual('2', val)

    def test_value_doesnot_exist(self):
        with self.assertRaises(NameError) as cm:
           DataStore.get_argument_value(TokenArg('STUFF'))
        ex = cm.exception
        self.assertEqual("Parameter STUFF doesn't exist", ex.message)
