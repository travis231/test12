


import unittest
from tests.test_utils import get_sample_pdf_with_labels, get_sample_pdf, get_sample_sdf, get_sample_pdf_with_extra_cols, get_sample_pdf_with_no_text_col ,get_sample_spark_dataframe
from nlu import *

class TestBertSentenceEmbeddings(unittest.TestCase):

    def test_bert_sentence_embeds(self):
        df = nlu.load('embed_sentence.bert',verbose=True).predict('Am I the muppet or are you the muppet?', output_level='sentence',drop_irrelevant_cols=False, metadata=True, )
        # df = nlu.load('en.classify.sarcasm',verbose=True).predict(sarcasm_df['text'])
        for c in df.columns: print(df[c])



        df = nlu.load('en.embed.bert.small_L4_128', verbose=True).predict("No you are the muppet!")
        for c in df.columns: print(df[c])



if __name__ == '__main__':
    unittest.main()

