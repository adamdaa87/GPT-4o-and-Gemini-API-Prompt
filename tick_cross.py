# tick_cross.py
import unittest

class CustomTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)  # Ensure this line is present to register the test start
        pass

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln(f'✔ {self.getDescription(test)}')
        self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.writeln(f'✘ {self.getDescription(test)}')
        self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.writeln(f'✘ {self.getDescription(test)}')
        self.stream.flush()


class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)