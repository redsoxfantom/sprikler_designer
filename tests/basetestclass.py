import os
import traceback
import inspect


def test(func):
    func.is_test = True
    return func


class BaseTestClass:
    def __init__(self):
        self.testdata = {}
        self.testroot = os.path.dirname(os.path.realpath(__file__))

    def init_test(self):
        pass

    def run_tests(self):
        numpassed = 0
        testclass = self.__class__.__name__
        possibletests = inspect.getmembers(self,predicate=inspect.ismethod)
        listoftestmethods = []
        for possibletest in possibletests:
            if hasattr(possibletest[1],'is_test'):
                listoftestmethods.append(possibletest[1])
        nummethods = len(listoftestmethods)
        print("Running test class %s" % testclass)
        for method in listoftestmethods:
            try:
                print("Running %s.%s..." % (testclass, method.__name__))

                self.init_test()
                method()

                numpassed += 1
                print("Passed")
            except Exception as ex:
                tb = traceback.format_exc()
                print("Failed: %s: %s" % (ex, tb))

        print("%s: %s/%s passed" % (testclass, numpassed, nummethods))
        return numpassed, nummethods
