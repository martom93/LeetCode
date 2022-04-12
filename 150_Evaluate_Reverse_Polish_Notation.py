class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #Creating stack to put all numbers and operators
        stack = []
        
        #Checking if element is a number
        def isnum(s):
            try:
                int(s)
                return True
            except:
                return False
        
        #Loop for all elements from the list
        for t in tokens:
            
            #If element is a number, add this to stack
            if isnum(t):
                stack.append(t)
            else:
                
                #If element is an operator, put the result of the proper operation on the stack
                a = int(stack.pop())
                b = int(stack.pop())
                if t== "+":
                    c=b+a
                elif t== "-":
                    c=b-a
                elif t== "*":
                    c=b*a
                elif t== "/":
                    c=int(b/a)
                stack.append(c)
        
        #returning the final value.
        return stack[0]
