#终结符
T = ['(', ')', 'i', '+', '-', '*', '/', '$']

#非终结符
NT = ['S', 'A', 'B', 'C', 'D']

#产生式
P = [('S', "AB"),
     ('B', '+AB'),
     ('B', '-AB'),
     ('B', ''),
     ('A', 'CD'),
     ('D', '*CD'),
     ('D', '/CD'),
     ('D', ''),
     ('C', '(S)'),
     ('C', 'i')]

#分析表
table = { ('S', '('): 1,
          ('S', 'i'): 1,
          ('A', '('): 5,
          ('A', 'i'): 5,
          ('B', ')'): 4,
          ('B', '+'): 2,
          ('B', '-'): 3,
          ('B', '$'): 4,
          ('C', '('): 9,
          ('C', 'i'): 10,
          ('D', '+'): 8,
          ('D', '-'): 8,
          ('D', '*'): 6,
          ('D', '/'): 7,
          ('D', '$'): 8}

#栈
class Stack(object):
    # 初始化栈
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()

#主程序
def parser(w):
        run_s = []
        i = 0 #下标
        S = Stack()

        #初始添加终结符与起始符
        S.push('$')
        S.push('S')
        x = S.peek()

        if(w[-1] != '$'):
                print('invalid input')
                return

        #核心算法
        while(x != '$'):
                if(x == w[i]):
                        S.pop()
                        i += 1
                elif(x in T):
                        print("Error")
                        break
                elif(-1 == table.get((x, w[i]), -1)):
                        print("Error")
                        break
                elif(table.get((x, w[i]))):
                        p_num = table.get((x, w[i]))
                        run_s.append((P[p_num-1][0], '-->', P[p_num-1][1]))
                        d_p = P[p_num-1][1]
                        S.pop()
                        temp_s = Stack()
                        for s in d_p:
                                temp_s.push(s)
                        while not temp_s.is_empty():
                                S.push(temp_s.pop())
                x = S.peek()
        
        #匹配成功则返回运行栈
        if S.peek() == '$':
                print("Success")
                for i in run_s:
                        if i[2] == '':
                                print(i[0], i[1], 'null')
                        else:
                                print(i[0], i[1], i[2])

#测试
#字符串应带有$
w = 'i*i+i+i+i+i+i$'
parser(w)
