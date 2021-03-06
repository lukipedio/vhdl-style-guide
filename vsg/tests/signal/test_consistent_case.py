import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils


class testGeneralRule(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_014(self):
        oRule = signal.rule_014()
        self.maxDiff = None
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '014')
        lExpected = []

        dViolation = utils.add_violation(22)
        dViolation['signal'] = 'siG2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(25)
        dViolation['signal'] = 'siG1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(27)
        dViolation['signal'] = 'SIG2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['signal'] = 'sIg1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(29)
        dViolation['signal'] = 'SiG2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['signal'] = 'SIg1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(38)
        dViolation['signal'] = 'Sig1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(39)
        dViolation['signal'] = 'SIg2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(46)
        dViolation['signal'] = 'Sig3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(48)
        dViolation['signal'] = 'siG5'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(54)
        dViolation['signal'] = 'siG6'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(58)
        dViolation['signal'] = 'Sig1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(60)
        dViolation['signal'] = 'Sig2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(62)
        dViolation['signal'] = 'Sig3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(63)
        dViolation['signal'] = 'SIG1'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(63)
        dViolation['signal'] = 'SIG2'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(63)
        dViolation['signal'] = 'SIG3'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(64)
        dViolation['signal'] = 'SIG1'
        lExpected.append(dViolation)


        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
        self.assertEqual(oRule._get_solution(22), 'Inconsistent capitalization of signal: siG2')
        self.assertEqual(oRule._get_solution(25), 'Inconsistent capitalization of signal: siG1')
        self.assertEqual(oRule._get_solution(27), 'Inconsistent capitalization of signal: SIG2')
        self.assertEqual(oRule._get_solution(28), 'Inconsistent capitalization of signal: sIg1')
        self.assertEqual(oRule._get_solution(29), 'Inconsistent capitalization of signal: SiG2')
        self.assertEqual(oRule._get_solution(30), 'Inconsistent capitalization of signal: SIg1')
        self.assertEqual(oRule._get_solution(38), 'Inconsistent capitalization of signal: Sig1')
        self.assertEqual(oRule._get_solution(39), 'Inconsistent capitalization of signal: SIg2')
        self.assertEqual(oRule._get_solution(46), 'Inconsistent capitalization of signal: Sig3')
        self.assertEqual(oRule._get_solution(48), 'Inconsistent capitalization of signal: siG5')
        self.assertEqual(oRule._get_solution(54), 'Inconsistent capitalization of signal: siG6')
        self.assertEqual(oRule._get_solution(58), 'Inconsistent capitalization of signal: Sig1')
        self.assertEqual(oRule._get_solution(60), 'Inconsistent capitalization of signal: Sig2')
        self.assertEqual(oRule._get_solution(62), 'Inconsistent capitalization of signal: Sig3')
        self.assertEqual(oRule._get_solution(63), 'Inconsistent capitalization of signals: SIG1, SIG2, SIG3')
        self.assertEqual(oRule._get_solution(64), 'Inconsistent capitalization of signal: SIG1')

    def test_fix_rule_014(self):
        oRule = signal.rule_014()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[22].line, '  PROC_NAME : process (sig2) is')
        self.assertEqual(self.oFile.lines[25].line, '    sig1 <= \'0\';')
        self.assertEqual(self.oFile.lines[27].line, '    if (sig2 = \'0\') then')
        self.assertEqual(self.oFile.lines[28].line, '      sig1 <= \'1\';')
        self.assertEqual(self.oFile.lines[29].line, '    elsif (sig2 = \'1\') then')
        self.assertEqual(self.oFile.lines[30].line, '      sig1 <= \'0\';')
        self.assertEqual(self.oFile.lines[38].line, '    SIG1 => sig1,')
        self.assertEqual(self.oFile.lines[39].line, '    SIG2 => sig2,')
        self.assertEqual(self.oFile.lines[40].line, '    SIG3 => sig3')
        self.assertEqual(self.oFile.lines[46].line, '    SIG3 => sig3,')
        self.assertEqual(self.oFile.lines[47].line, '    SIG4 => sig4,')
        self.assertEqual(self.oFile.lines[48].line, '    SIG5 => sig5')
        self.assertEqual(self.oFile.lines[54].line, '    SIG6 => sig6,')
        self.assertEqual(self.oFile.lines[55].line, '    SIG7 => sig7')
        self.assertEqual(self.oFile.lines[58].line, '  sig1 <= \'0\';')
        self.assertEqual(self.oFile.lines[59].line, '  sig1 <= sig2 and sig3;')
        self.assertEqual(self.oFile.lines[60].line, '  sig1 <= sig2 and sig3;')
        self.assertEqual(self.oFile.lines[61].line, '  sig1 <= sig2 and')
        self.assertEqual(self.oFile.lines[62].line, '          sig3;')
        self.assertEqual(self.oFile.lines[63].line, '  sig1 <= sig2 and sig3;')
        self.assertEqual(self.oFile.lines[64].line, '  sig1 <= sig1 or sig1;')

        self.assertEqual(oRule.violations, [])
