import string
import time
from datetime import datetime

#保留字表
_reserveWords = ['void', 'int', 'long', 'unsigned', 'short', 'float',
                'double', 'if', 'else', 'do', 'while', 'for', 'break',
                'continue', 'char', 'return']
_code = '' #程序源码
_i = 0 #下标
_token = '' #存放已经分析出的单词
_line = 1 #行数
_state = 0 #token的状态
_syn = '' #单词种类
_table = [] # token表

#预处理(只去除注释)
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

                #我也搞不懂为什么要在这里减去注释的长度，但是如果不加这句预处理就会出错
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

#获取程序
def getCode():
    global _code
    fPath = 'test.c'
    with open(fPath, 'r') as f:
        for l in f.readlines():
            if l != '\n':
                _code = _code + l.lstrip()
            else:
                _code = _code + l

#将token存入token table中
def store(token, syn):
    global _table
    if token not in _table:
        _table.append((syn, token))   

#分析器
def scanner(str):
    global _i, _token, _syn, _mstate, _cstate, _dstate, _line

    #获取字符 每次分析前先将token清空
    _token = ''
    c = str[_i]
    _i += 1

    #去除空格与换行
    while c=='' or c=='\n':
        c = str[_i]
        _i += 1

    #判断token是保留字还是标识符
    if c in string.ascii_letters or c =='_':
        while c in string.ascii_letters or c in string.digits or c=='_':
            _token += c
            c = str[_i]
            _i += 1
        
        _i -= 1

        if _token in _reserveWords:
            _syn = 'ID'
        
        if _syn == 'ID':
            store(_syn, _token)
    
    #判断是否为字符串
    elif c == '\"':
        _state = 0
        while c in string.ascii_letters or c in '\" ,;' or c in string.digits:
            _token += c
            if _state == 0:
                if c == '\"':
                    _state = 1
            
            if _state == 1:
                if c == '\"':
                    _state = 2

            c = str[_i]
            _i += 1
        
        if _state == 1:
            _syn = '-1' #字符串未封闭

        elif _state == 2:
            _syn = "String"
            store(_syn, _token)
        
        _i -= 1

    #判断是否为数字
    elif c in string.digits:
        _state = 0
        while c in string.digits or c == '.':
            _token += c
            if _state == 0:
                if c == 0:
                    _state = 4
                else:
                    _state = 1
            
            elif _state == 1:
                if c in string.digits:
                    _state = 1
                elif c == '.':
                    _state = 2
            
            elif _state == 4:
                if c == '.':
                    _state = 2
            
            elif _state == 2:
                if c in string.digits:
                    _state = 3
            
            elif _state == 3:
                if c in string.digits:
                    _state = 3
            
            c = str[_i]
            _i += 1

            if _state == 1 or _state == 5:
                _syn = "Digit"
                store(_syn, _token)
            else:
                _syn = '-2' #数字出错
            
        _i -= 1

    #以下部分全部为逻辑运算符与界符
    elif c == '<': 
        _token = c
        c = str[_i]
        
        if c == '=':          
            _token += c
            _i += 1
            _syn = '<='
        else:                 
            _syn = '<'
        store(_syn, _token)
        
    elif c == '>': 
        _token = c
        c = str[_i]
        
        if c == '=':         
            _token += c
            _i += 1
            _syn = '>='
        else:                
            _syn = '>'
        store(_syn, _token)
            
    elif c == '!': 
        _token = c
        c = str[_i]
        
        if c == '=':         
            _token += c
            _i += 1
            _syn = '!='
        else:                
            _syn = '!'
        store(_syn, _token)
                
    elif c == '+': 
        _token = c
        c = str[_i]
        
        if c =='+':          
            _token += c
            _i += 1
            _syn = '++'
        else :               
            _syn = '+'
        store(_syn, _token)
        
    elif c == '-': 
        _token = c
        c = str[_i]
        
        if c =='-':          
            _token += c
            _i += 1
            _syn = '--'
        else :               
            _syn = '-'
        store(_syn, _token)
            
    elif c == '=':  
        _token = c
        c = str[_i]
        
        if c =='=':          
            _token += c
            _i += 1
            _syn = '=='
        else :               
            _syn = '='
        store(_syn, _token)
    
    elif c == '&':
        _token = c 
        c = str[_i]
        
        if c == '&':         
            _token += c
            _i += 1
            _syn = '&&'
        else:                
            _syn = '&'
        store(_syn, _token)
            
    elif c == '|':
        _token = c
        c = str[_i]
        
        if c == '|':                
            _token += c
            _i += 1
            _syn = '||'
        else:                
            _syn = '|'
        store(_syn, _token)
            
    elif c == '*':          
        _token = c
        _syn = '*'
        store(_syn, _token)
        
    elif c == '/':          
        _token = c
        _syn = '/'
        store(_syn, _token)
        
    elif c ==';':           
        _token = c
        _syn = ';'
        store(_syn, _token)
        
    elif c == '(':           
        _token = c
        _syn = '('
        store(_syn, _token)
        
    elif c == ')':          
        _token = c
        _syn = ')'
        store(_syn, _token)
        
    elif c == '{':          
        _token = c
        _syn = '{'
        store(_syn, _token)
        
    elif c == '}':              
        _token = c
        _syn = '}'    
        store(_syn, _token)   
        
    elif c == '[':              
        _token = c
        _syn = '['   
        store(_syn, _token)
        
    elif c == ']':              
        _token = c
        _syn = ']'  
        store(_syn, _token)
        
    elif c == ',':              
        _token = c
        _syn = ','  
        store(_syn, _token)

    elif c == '\n':
        _syn = '1' 
        store(_syn, _token)

#主程序
if __name__ == "__main__":
    getCode()
    preProcessing()

    while _i != len(_code):
        scanner(_code)
        if _syn == '1':
            _line += 1
        if _syn == '-1':
            print( 'Error in line', str(_line), ':string', _token)
        if _syn == '-2':
            print('Error in line', str(_line), ':digit', _token,)
    
    p = 'out.txt'
    for i in _table:
        print(i)
        with open(p, 'a') as f:
            f.write(str(i[0]) + ':' + str(i[1]) + '\n')


