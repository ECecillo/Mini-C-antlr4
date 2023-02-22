#! /usr/bin/env python3
import pytest
import glob
import sys
import os
from test_expect_pragma import TestExpectPragmas

ALL_FILES = glob.glob('./tests/*.txt')

if 'TEST_FILES' in os.environ:
    ALL_FILES = glob.glob(os.environ['TEST_FILES'], recursive=True)

ARIT_EVAL = 'arit.py'


class TestEVAL(TestExpectPragmas):
    def evaluate(self, file):
        return self.run_command(['python3', ARIT_EVAL, file])

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_expect(self, filename):
        expect = self.get_expect(filename)
        eval = self.evaluate(filename)
        assert expect == eval


if __name__ == '__main__':
    pytest.main(sys.argv)
