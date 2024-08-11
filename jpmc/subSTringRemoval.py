def getminlength(seq):
    stack = []
    for char in seq:
        if char == "A" or char == "B":
            if stack and stack[-1] == "A" and char == "B":
                stack.pop()
            elif stack and stack[-1] == "B" and char == "B":
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    return len(stack)


# Example usage:
sequence = "ABBAAB"
print(getminlength(sequence))  # Output: 2
