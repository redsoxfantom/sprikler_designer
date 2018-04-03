

def equals(o1, o2):
    if o1 != o2:
        raise Exception("%s != %s" % (o1, o2))


def notequals(o1, o2):
    if o1 == o2:
        raise Exception("%s == %s" % (o1, o1))


def istrue(o1):
    if not o1:
        raise Exception("istrue failed")


def isfalse(o1):
    if o1:
        raise Exception("isfalse failed")