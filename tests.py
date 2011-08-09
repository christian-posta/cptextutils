from sentence_case import convert_i
from sentence_case import put_back_punc
from sentence_case import split_on_punc
from sentence_case import find_all_punc
from sentence_case import mark_sentence_case

__author__ = 'ceposta'
import unittest
import re

class TestSplittingOnRegularExpression(unittest.TestCase):

    def test_split_on_punc(self):
        pattern = re.compile('[!?.]\s')
        test_input ="'this is the best! i can write unit tests now. Can you? I didn't think so."
        results = pattern.split(test_input)
        self.assertEqual(4, len(results))
        print results

        results = split_on_punc(test_input)
        self.assertEqual(4, len(results))


    def test_capitalize(self):
        test_input = ['this is a test', 'this is a test', 'this is a test']
        sentences = [x.capitalize() for x in test_input]

        for s in sentences:
            print s
            self.assertTrue(s[0].isupper())

        print sentences



    def test_join(self):
        test_input = ['this is a test', 'this is a test', 'this is a test']
        sentence = ' '.join(test_input)
        self.assertEqual(12, sentence.count(' ') + 1)
        print sentence


    def test_find_all_punc(self):
        test_input = 'Here it is!! We finally got it!? '
        all_punc = find_all_punc(test_input)

        expected_punc_exclaim = 11
        expected_punc_quest = 31

        self.assertEqual(expected_punc_exclaim, all_punc[0][0])
        self.assertEqual(expected_punc_quest, all_punc[1][0])


    def test_put_back_punc(self):
        test_input = 'here  it is got to go with the flow'
        sentence = put_back_punc(test_input, [(4, '!'),])
        self.assertEqual('here! it is got to go with the flow', sentence)

    def test_convert_i(self):
        data = 'this is what i want to talk to you about'
        expected_data = 'this is what I want to talk to you about'
        sentence_case = convert_i(data)
        self.assertEqual(expected_data, sentence_case)
        print sentence_case

        data = 'this is what i, want to talk to you about'
        expected_data = 'this is what I, want to talk to you about'
        sentence_case = convert_i(data)
        self.assertEqual(expected_data, sentence_case)
        print sentence_case

        data = 'this is what i. want to talk to you about'
        expected_data = 'this is what I. want to talk to you about'
        sentence_case = convert_i(data)
        self.assertEqual(expected_data, sentence_case)
        print sentence_case



    def test_mark_sentence_case(self):
        data = '''STRINGS IN ALL CAPS ARE HARD TO READ! SOME PEOPLE THINK
        THEY ARE LIKE SHOUTING!! WHAT DO YOU THINK ABOUT THAT?'''

        expected_data = '''Strings in all caps are hard to read! Some people think
        they are like shouting!! What do you think about that?'''

        sentence_case = mark_sentence_case(data)
        print len(sentence_case), len(data)
        print sentence_case

        self.assertEqual(expected_data, sentence_case)

    def test_smaller_string(self):
        data = '''this is my! test? no...'''
        expected_data = '''This is my! Test? No...'''
        sentence_case = mark_sentence_case(data)
        self.assertEqual(expected_data, sentence_case)


    def test_original_string(self):
        data = '''STRINGS IN ALL CAPS ARE HARD TO READ! SOME PEOPLE THINK THEY ARE LIKE SHOUTING. DO YOU THINK SO? I ONLY WRITE THEM WHEN I HAVE A CAPS-LOCK ACCIDENT. (OR WHEN CREATING TEST DATA.) THEY ARE NO FUN. (OK, ENOUGH NOW.)'''
        expected_data = '''Strings in all caps are hard to read! Some people think they are like shouting. Do you think so? I only write them when I have a caps-lock accident. (Or when creating test data.) They are no fun. (Ok, enough now.)'''

        sentence_case = mark_sentence_case(data)
        self.assertEqual(expected_data, sentence_case)


if __name__ == '__main__':
    unittest.main()