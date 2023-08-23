from oxford_comma import (
    oxford_comma
)

class TestOxfordComma:
    '''Module oxford_comma.py'''

def oxford_comma(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        return ', '.join(elements[:-1]) + ', and ' + elements[-1]