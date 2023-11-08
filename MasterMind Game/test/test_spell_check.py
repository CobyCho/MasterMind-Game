import unittest
from unittest.mock import patch
from src.spell_check import spell_check, parse_text, get_response

class TextProcessingTests(unittest.TestCase):
    def test_get_response_takes_word_and_returns_response(self):
        response = get_response('word')

        self.assertGreater(len(response), 0)

    def test_parse_text_takes_true(self):
        self.assertTrue(parse_text('true'))

    def test_parse_text_takes_false(self):
        self.assertFalse(parse_text('false'))

    @patch('src.spell_check.get_response', return_value='true')
    @patch('src.spell_check.parse_text', return_value = True)
    def test_spell_check_calls_get_response_and_parse_text_returns_result(self, mock_parse_text, mock_get_response):
        result = spell_check('Word')

        mock_get_response.assert_called_with('Word')
        mock_parse_text.assert_called_with('true')

        self.assertTrue(result)

    @patch('src.spell_check.get_response', side_effect=Exception("Some exception message"))
    def test_spell_check_returns_error(self, mock_get_response):
        with self.assertRaisesRegex(Exception, "Some exception message"):
             spell_check('Word')
            
if __name__ == '__main__': 
  unittest.main()

#Feedback: since this is focused on code in spell_check.py, the file should be named test_spell_check.py
