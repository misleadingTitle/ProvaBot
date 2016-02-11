import re
keywords = ['cazzo']

def containsKeyword(inputString):
    if re.match(r'.*?\bcazzo\b.*?', inputString):
        return True
    else:
        return False


