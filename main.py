_*_ encoding=utf-8 _*_
        
class MGraph():
    def __init__(self, trans, s):
        self.trans = trans 
        self.state = s

    def getState(self, i):
        return self.state[i]

def scaningRE(s):
    return

def scanningNFA(t):
    return

def scanningDFA(g):
    return

def main():
    s = input("Please input your start symbols: ")
    symbols = s.split(' ')
    RE = []
    judgeRE = 'y'
    while(judgeRE == 'y'):
        RE.append(input("Please input RE: "))
        judgeRE = input("Is there any other RE? (y/n): ")

    NFA = scaningRE(RE)
    DFA = scanningNFA(NFA)
    mDFA = scanningDFA(DFA)
    
    print(s)
    print(RE)

main()

