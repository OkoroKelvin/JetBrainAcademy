from hstest.stage_test import *
from hstest.test_case import TestCase
import re

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TicTacToeTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply: str, attach: str) -> CheckResult:
        reply = re.sub("\\s+", "", reply)
        if len(reply) > 9:
            return CheckResult(False, "You need to output no more than 9 symbols")
        have_x = False
        have_o = False
        for c in reply:
            if c != 'X' and c != 'O':
                return CheckResult(False,
                       "You need to output X and O "
                       + "symbols only not counting spaces. Found: '" + c + "'")
            if c == 'X':
                have_x = True
            if c == 'O':
                have_o = True
        if not have_x:
            return CheckResult.wrong("You need to output at least one X")
        if not have_o:
            return CheckResult.wrong("You need to output at least one O")
        return CheckResult.correct()


if __name__ == '__main__':
    TicTacToeTest().run_tests()
