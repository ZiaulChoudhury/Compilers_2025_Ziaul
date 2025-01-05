def postfix_to_assembly(postfix):
    stack = []
    assembly = []

    for char in postfix:
        if char.isdigit():  # If the character is a digit
            stack.append(int(char))
            assembly.append(f"PUSH {char}")
        elif char in '+-':  # If the character is an operator
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")

            b = stack.pop()
            a = stack.pop()

            if char == '+':
                result = a + b
                assembly.append("ADD")
            elif char == '-':
                result = a - b
                assembly.append("SUB")

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return assembly, stack[0]

def evaluate_infix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        elif char in '+-':
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")

            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack[0]

def main():
    postfix = "32+5-6-"
    print(f"Postfix expression: {postfix}")

    # Generate assembly code and compute result
    assembly, computed_value = postfix_to_assembly(postfix)
    print("Assembly sequence:")
    for instr in assembly:
        print(instr)

    # Evaluate the infix expression value
    correct_value = evaluate_infix(postfix)

    print(f"Computed value: {computed_value}")
    print(f"Correct value: {correct_value}")

    # Validation
    assert computed_value == correct_value, "Computed value does not match the correct value"
    print("Validation passed: The assembly sequence computes to the correct value.")

if __name__ == "__main__":
    main()

