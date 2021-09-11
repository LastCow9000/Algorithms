import sys

inp = sys.stdin.readline

while True:
    input_data = inp().rstrip()
    if input_data == ".":
        break
    stack = []
    for word in input_data:
        if word == "(" or word == "[":
            stack.append(word)
        elif word == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(word)
                break
        elif word == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(word)
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")