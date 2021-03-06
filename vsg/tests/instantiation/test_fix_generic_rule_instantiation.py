import os

import unittest

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg.tests import utils

lFileGeneric = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'instantiation_generic_test_input.vhd'))

class testFixRuleInstantiationMethods(unittest.TestCase):

    def setUp(self):
        self.oFileGeneric = vhdlFile.vhdlFile(lFileGeneric)

    def test_fix_rule_012(self):
        oRule = instantiation.rule_012()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = instantiation.rule_013()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = instantiation.rule_014()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFileGeneric.lines[46].line, '     GENERic_2 => generic_2')
        self.assertFalse(self.oFileGeneric.lines[46].isInstantiationGenericEnd)
        self.assertEqual(self.oFileGeneric.lines[47].line, '  )')
        self.assertTrue(self.oFileGeneric.lines[47].isInstantiationGenericEnd)
        self.assertEqual(self.oFileGeneric.lines[66].line, '      GENERIC_2 =>   generic_2')
        self.assertFalse(self.oFileGeneric.lines[66].isInstantiationGenericEnd)
        self.assertEqual(self.oFileGeneric.lines[67].line, '  )')
        self.assertTrue(self.oFileGeneric.lines[67].isInstantiationGenericEnd)
        self.assertEqual(self.oFileGeneric.lines[101].line, '      GENERIC_4 => (2*generic_2)')
        self.assertFalse(self.oFileGeneric.lines[101].isInstantiationGenericEnd)
        self.assertEqual(self.oFileGeneric.lines[102].line, '  )')
        self.assertTrue(self.oFileGeneric.lines[102].isInstantiationGenericEnd)

    def test_fix_rule_016(self):
        oRule = instantiation.rule_016()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = instantiation.rule_017()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_001_generics(self):
        oRule = instantiation.rule_001()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = instantiation.rule_018()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_fule_025(self):
        oRule = instantiation.rule_025()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFileGeneric.lines[81].line, '    generic map (')
        self.assertEqual(self.oFileGeneric.lines[82].line, '      GENERIC_1 =>   generic_1,')

    def test_fix_fule_026(self):
        oRule = instantiation.rule_026()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFileGeneric.lines[86].line, '    port map (')
        self.assertEqual(self.oFileGeneric.lines[87].line, '      PORT_1 => w_port_1,')

    def test_fix_fule_030(self):
        oRule = instantiation.rule_030()
        oRule.fix(self.oFileGeneric)
        oRule.analyze(self.oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFileGeneric.lines[65].line, '      GENERIC_2 => generic_2)')
        self.assertEqual(self.oFileGeneric.lines[83].line, '      GENERIC_1 => generic_1,')
