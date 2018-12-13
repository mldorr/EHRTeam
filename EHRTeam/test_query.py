"""
This test file is used to test function in query.py in EHRTeam
"""
import unittest
import os
import pandas as pd
from query import query, query_single, filter_query as f, narms_query
#%%
DF = pd.read_csv('../Data/test_file.csv')
#%%
class TestFunctions(unittest.TestCase):
    """
    Unittest class
    """
    def test_query(self):
        """
        This function test whether the "query" function extract correct row and attributes.
        """
        data_extract = query(DF, ['subject_id'], ['hadm_id'], ['subject_id'])
        self.assertEqual(data_extract.shape, (3, 2))
        self.assertEqual(list(data_extract.columns.values), ['subject_id', 'hadm_id'])

    def test_query_single(self):
        """
        This function test whether the "querySingle" function extract correct row and attributes.
        """
        data_extract = query_single(DF, 'subject_id', 61, ["subject_id"],
                                    ["insurance", "age"], "subject_id")
        incorrect_data_extract = query_single(DF, 'subject_id', 300, ["subject_id"],
                                              ["insurance"], "subject_id")
        self.assertEqual(data_extract.shape, (1, 3))
        self.assertEqual(incorrect_data_extract.shape, (0, 2))
        self.assertTrue(len(data_extract['insurance'][0]) == len(data_extract['age'][0]))

    def test_filter(self):
        """
        This function test "filter" function, to see if it can successfully filter the data
        from extracted data by "querySingle" function.
        """
        data_extract = query_single(DF, 'subject_id', 61, ["subject_id"], \
                                   ["insurance", "age"], "subject_id")
        filtered_data = f(data_extract, 'subject_id', 66, '>')
        self.assertTrue(filtered_data.shape[0] == 0)
        filtered_data = f(data_extract, 'subject_id', 66, '<')
        self.assertTrue(filtered_data.shape[0] == data_extract.shape[0])

    def test_narms_query(self):
        """
        This function test "narms_query" function, so see if it can successfully
        query data from a file named "narm's processed.csv" and create a new file
        named "narms_out.csv" after that. The input and output files should be in
        the same directory.
        """
        #filename = "narm's processed.csv"
        output_filename = 'narms_out.csv'
        extract_narm = narms_query("../Data/narms_processed.csv", 1996, '0-4')
        self.assertTrue(os.path.isfile(output_filename))
        load_file = pd.read_csv(output_filename)
        self.assertEqual(load_file.shape, (1, 35))
        self.assertEqual(extract_narm.shape, load_file.shape)
        self.assertEqual(list(extract_narm.columns.values), list(load_file.columns.values))


if __name__ == '__main__':
    unittest.main()
