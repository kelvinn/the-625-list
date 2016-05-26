#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" These are some basic tests for the-625-list app """

__author__ = 'kelvinn'
__email__ = 'kelvin@kelvinism.com'

import os
import sys
import unittest
from go import *


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.client_id = getenv('MS_TRANSLATOR_CLIENT_ID', None)
        self.api_key = getenv('MS_TRANSLATOR_API_KEY', None)

    def test_read_files(self):
        en_word_list = read_word_list()
        self.assertEqual(len(en_word_list), 612)
        self.assertEqual(en_word_list[0], 'one')

    def test_get_translated_text(self):
        en_word_list = read_word_list()
        result = get_translated_text(en_word_list, 'fr', self.client_id, self.api_key)
        self.assertEqual(len(result), 613)
        self.assertEqual(result[1], 'un')


if __name__ == '__main__':
    unittest.main()