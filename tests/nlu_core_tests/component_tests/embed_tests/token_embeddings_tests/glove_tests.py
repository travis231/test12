


import unittest
from tests.test_utils import get_sample_pdf_with_labels, get_sample_pdf, get_sample_sdf, get_sample_pdf_with_extra_cols, get_sample_pdf_with_no_text_col ,get_sample_spark_dataframe
from nlu import *

class TestGloveTokenEmbeddings(unittest.TestCase):

    def test_glove_model(self):
        df = nlu.load('glove',verbose=True).predict('Am I the muppet or are you the muppet?', output_level='token')
        for c in df.columns: print(df[c])





if __name__ == '__main__':
    unittest.main()

