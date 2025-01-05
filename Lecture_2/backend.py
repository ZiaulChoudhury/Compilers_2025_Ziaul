def generate_code(postfix_expression):
    """
    Generates assembly code for a hypothetical CPU with two general-purpose registers (R1 and R2)
    and instructions ADD and SUB.

    Parameters:
        postfix_expression (str): The postfix expression to be compiled.

    Returns:
        List[str]: A list of assembly instructions.
    """
    stack = []  # Stack to simulate intermediate register results
    instructions = []  # List to hold generated instructions

    # Iterate over each character in the postfix expression
    for char in postfix_expression:
        if char.isdigit():
            # If it's a number, push it onto the stack
            stack.append(int(char))
        elif char in ('+', '-'):  # Handle operators
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression: insufficient operands.")

            # Pop the last two values from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Load operand1 into R1 and operand2 into R2
            instructions.append(f"LOAD R1, {operand1}")
            instructions.append(f"LOAD R2, {operand2}")

            if char == '+':
                # Perform addition and push the result onto the stack
                instructions.append("ADD R2, R2, R1")
            elif char == '-':
                # Perform subtraction and push the result onto the stack
                instructions.append("SUB R2, R2, R1")

            # Push the result (R2) back onto the stack
            result = operand2 + operand1 if char == '+' else operand2 - operand1
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression: remaining operands on stack.")

    return instructions

# Example usage
postfix_expr = "35+2-3+6-"
instructions = generate_code(postfix_expr)
print("Generated Assembly Instructions:")
for instr in instructions:
    print(instr)
