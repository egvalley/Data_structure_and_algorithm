class Stack():
   def __init__(self):
       self.stack=[]

   def push(self,element):
       self.stack.append(element)

   def pop(self):
       return self.stack.pop()

   def get_top(self):
       if len(self.stack)>0:
           return self.stack[-1]
       else:
           return None

   def is_empty(self):
       return len(self.stack)==0





def brace_match(li):
    stack = Stack()
    dic={'}':'{',']':'[',')':'('}
    for ch in li:
        if ch in {'{','[','('}:
            stack.push(ch)
        else:
            if stack.get_top()==dic[ch]:
                stack.pop()
            elif stack.is_empty():
                return False
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('{{}}'))


