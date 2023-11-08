import unittest
import textwrap
from textwrap import dedent
from unittest.mock import Mock
from src.text_processing import process_text

def raise_exception(message = 'The server has run into an error'):
   raise Exception(message)

class SpellCheckerTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
    
    def test_process_text_takes_empty_string(self):
        check_spelling = Mock(return_value=True)

        self.assertEqual('', process_text('', check_spelling))
        
    def test_process_text_takes_hello(self):
        check_spelling = Mock(return_value=True)

        self.assertEqual('hello', process_text('hello', check_spelling)) 
    
    def test_process_text_takes_incorrectly_spelled_word(self):
        check_spelling = Mock(return_value=False)

        self.assertEqual('[blah]', process_text('blah', check_spelling))

    def test_process_text_takes_two_correct_words(self):
        check_spelling = Mock(return_value=True)

        self.assertEqual('hello there', process_text('hello there', check_spelling))

    def test_process_text_takes_first_correct_second_incorrect(self):
        check_spelling = Mock(side_effect=[True, False])

        self.assertEqual('hello [tyop]', process_text('hello tyop', check_spelling))

    def test_process_text_takes_first_incorrect_second_correct(self):
        check_spelling = Mock(side_effect=[False, True])

        self.assertEqual('[misp] hello', process_text('misp hello', check_spelling))
        
    def test_process_text_takes_mixed_correct_and_incorrect(self):
        check_spelling = Mock(side_effect=(lambda word: word not in ['tyop', 'misp']))
        
        self.assertEqual('hello [tyop] there [misp]', process_text('hello tyop there misp', check_spelling))
    
    def test_process_text_takes_and_returns_two_lines(self):
        check_spelling = Mock(return_value=[True])

        input_text = textwrap.dedent("""\
            This is the first line
            This is the second line""")
        
        expected_output = textwrap.dedent("""\
            This is the first line
            This is the second line""")

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

    def test_process_text_takes_correct_and_incorrect_two_lines(self):
        check_spelling = Mock(side_effect=(lambda word: word not in ['teh', 'Thiss', 'tyop']))

        input_text = textwrap.dedent("""\
            This is teh first line
            Thiss is tyop second line""")
        
        expected_output = textwrap.dedent("""\
            This is [teh] first line
            [Thiss] is [tyop] second line""")

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

    def test_process_text_takes_and_returns_three_lines(self):
        check_spelling = Mock(return_value=[True])
        input_text = textwrap.dedent("""\
            This is the first line
            This is the second line
            This is the third line""")
        
        expected_output = textwrap.dedent("""\
            This is the first line
            This is the second line
            This is the third line""")

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

    def test_process_text_takes_correct_and_incorrect_three_lines(self):
        check_spelling = Mock(side_effect=lambda word: word not in ['teh', 'Thiss', 'tyop'])
        input_text = textwrap.dedent("""\
            This is teh first line
            Thiss is the second line
            This is tyop third line""")
        
        expected_output = textwrap.dedent("""\
            This is [teh] first line
            [Thiss] is the second line
            This is [tyop] third line""")

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

    def test_process_text_takes_exception(self):
        check_spelling = Mock(side_effect=lambda word: raise_exception() if word == 'there' else word != 'aare')
        
        input_text = 'hello there how aare you'
        expected_output = 'hello ?there? how [aare] you'

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

    def test_process_text_takes_three_exceptions_and_three_mispelling_three_lines(self):
        check_spelling = Mock(side_effect=lambda word: raise_exception() if word in ['This', 'second'] else word not in ['Thiss','tyop', 'teh'])
        
        input_text = textwrap.dedent("""\
            This is teh first line
            Thiss is the second line
            This is tyop third line""")
        
        expected_output = textwrap.dedent("""\
            ?This? is [teh] first line
            [Thiss] is the ?second? line
            ?This? is [tyop] third line""")

        self.assertEqual(expected_output, process_text(input_text, check_spelling))

if __name__ == '__main__': 
  unittest.main()


#Feedback: since this is focused on code in text_processing.py, the file should be named test_text_processing.py
