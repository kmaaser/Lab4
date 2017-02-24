#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/08/2009
#----------------------------------------------------------------------

from Stack import Stack

def inToPost(infixExpression):

    stack = Stack()
    postfixExpression = list()
    operator = ["*", "/", "+", "-"]

    newExpression = infixExpression.split(" ")

    for token in newExpression:
        #if type(float(token)) is float:
        try:
            value = float(token)
            postfixExpression.append(str(value))
        except ValueError:
            if token in ["(", "[", "{"]:
                pass
            elif token in operator:
                while stack.size() != 0 and stack.top() in operator and (stack.top() in "*/" or token in "+-"):
                    if stack.top() in "*/":
                        item = stack.pop()
                        postfixExpression.append(item)
                    elif token in "+-":
                        item = stack.pop()
                        postfixExpression.append(item)
                stack.push(token)
            else:
                topOfStack = stack.top()
                if stack.size() > 0 and token in [")", "]", "}"]:
                    item = stack.pop(topOfStack)
                    postfixExpression.append(item)
                stack.pop(topOfStack)
    while stack.size() != 0:
        item = stack.pop()
        postfixExpression.append(item)
    returnValue = str()
    for i in postfixExpression:
        returnValue += (i + " ")
        returnValue.strip()
    ' '.join(returnValue)
    returnValue.rstrip()
    return returnValue


def evalPostfix(postfixExpression):

   """ numStack = Stack
    answer = 0

    for token in postfixExpression:
        if token == "+" and numStack.size() > 0:
            item1 = numStack.pop()
            item2 = numStack.pop()
            answer = answer + (item1 + item2)

        elif token == "-" and numStack.size() > 0:
            item1 = numStack.pop()
            item2 = numStack.pop()
            answer = answer + (item2 - item1)

        elif token == "*" and numStack.size() > 0:
            item1 = numStack.pop()
            item2 = numStack.pop()
            answer = answer + (item1 * item2)

        elif token == "/" and numStack.size() > 0:
            item1 = numStack.pop()
            item2 = numStack.pop()
            answer = answer (item2 / item1)
        else:
            numStack.push(token)
    return answer"""
   pass