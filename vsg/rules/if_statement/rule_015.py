
from vsg.rules.if_statement import if_rule

import re


class rule_015(if_rule):
    '''If rule 015 checks there is a single space between the "end" and "if" keywords.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Ensure only a single space exists between the "end" and "if" keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword:
                if re.match('^\s*end\s+if', oLine.line, re.IGNORECASE):
                    if not re.match('^\s*end\sif', oLine.line, re.IGNORECASE):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'end')
