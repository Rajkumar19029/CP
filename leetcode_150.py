class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for element in tokens:
            match (element):
                case '+':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1+op2
                    stack.append(res)
                case '-':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1-op2
                    stack.append(res)
                case '*':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1*op2
                    stack.append(res)
                case '/':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1/op2
                    stack.append(res)
                case _:
                    stack.append(element)
        return int(stack.pop())

        
        