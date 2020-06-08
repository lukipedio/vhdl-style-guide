import os

import unittest

from vsg.rules import process
from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests

oFile = vhdlFile.vhdlFile(utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'next_line_code_tag_test_input.vhd')))

class testCodeTags(unittest.TestCase):

    def test_rule_process_016(self):
        oRule = process.rule_016()

        dExpected = []
        dExpected.append(utils.add_violation(13))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_process_018(self):
        oRule = process.rule_018()

        dExpected = []
        dExpected.append(utils.add_violation(15))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_architecture_024(self):
        oRule = architecture.rule_024()

        dExpected = []
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
