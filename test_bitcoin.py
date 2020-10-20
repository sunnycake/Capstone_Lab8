import unittest 
from unittest import TestCase 
from unittest.mock import patch

import bitcoin


class TestBitCoin(TestCase):

    @patch('bitcoin.request_rate')
    def test_convert(self, mock_rate):
        mock_rate_float = 1234.56
        example_api_response = {'bpi': 'USD', 'rate_float': mock_rate_float}
        mock_rate.side_effect = [example_api_response]
        converted = bitcoin.convert(100, mock_rate_float) 
        self.assertEqual(123456, converted)


if __name__ == '__main__':
    unittest.main()