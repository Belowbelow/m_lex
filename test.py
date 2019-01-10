_code = '''sssssss
//helloaaaaa
aaaaa 
/*a aaaaaaaaaaaaa*/ 
new line'''

def preProcessing():
    global _code
    state = 0
    index = -1

    for c in _code:
        index = index + 1

        if state == 0:
            if c == '/':
                state = 1
                start = index

        elif state == 1:
            if c == '/':
                end = start + _code[start:].find('\n') + 1

                _code = _code.replace(_code[start: end], '')
                index = start - len(_code[start: end]) + 1
                state = 0
            elif c == '*':
                state = 3
            else:
                state = 0
        
        elif state == 3:
            if c == '*':
                state = 4
            else:
                pass
        
        elif state == 4:
            if c == '/':
                end = index + 1

                _code = _code.replace(_code[start:end], '')
                index = start - 1
                print(_code)
                state = 0
            else:
                state = 3
        
#preProcessing()
import string

c = 'a'
print(string.digits)