_*_ encoding=utf-8 _*_

""" 程序的作用为接收正则表达式作为输入，
输出一个最小化DFA"""

def re2nfa(re):
    return nfa

def nfa2dfa(nfa):
    return dfa

def minizeDfa(dfa):
    return mDfa

if __name__ == '__main__':
    lex_file_path = "F:/work/compling principle/lex model/lex.txt"
    with open(lex_file_path, 'r') as f:
        lex_content = []
        if(f.readline()):
            lex_content.append(f.readline())
    nfa = re2nfa(re)
    dfa = nfa2daf(nfa)
    mDfa = minizeDfa(dfa)

