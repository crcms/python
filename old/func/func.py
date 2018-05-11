def normal():
    return 'test'


def param(param1, param2):
    return param1 + param2


def defaultParam(param1, param2='is Param2'):
    return param1 + param2


def defaultParamNone(param1, param2='', param3=None):
    if param2 and param3:
        return param1 + param2 + param3
    elif param2:
        return param1 + param2
    elif param3:
        return param1 + param3
    return param1


def listParam(*param1):
    string = ''
    for param1 in item:
        string += item + '===='
    return string


def tupleParam(**param1):
    for param1 in key, value:
        print key + '===' + value
    return None
