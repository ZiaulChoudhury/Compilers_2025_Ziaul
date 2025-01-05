def execute_assembly(file_path):
    """
    Simulates the CPU by processing the assembly instructions one at a time.
    
    Args:
        file_path (str): Path to the .asm file containing assembly instructions.

    Returns:
        int: Final computed value after processing all instructions.
    """
    stack = []

    with open(file_path, 'r') as asm_file:
        instructions = asm_file.readlines()

    for instruction in instructions:
        instruction = instruction.strip()

        if instruction.startswith("PUSH"):
            _, value = instruction.split()
            stack.append(int(value))
        elif instruction == "POP":
            if not stack:
                raise ValueError("Stack underflow: No values to pop.")
            stack.pop()
        elif instruction == "ADD":
            if len(stack) < 2:
                raise ValueError("Stack underflow: Not enough values to add.")
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif instruction == "SUB":
            if len(stack) < 2:
                raise ValueError("Stack underflow: Not enough values to subtract.")
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        else:
            raise ValueError(f"Unknown instruction: {instruction}")

    if len(stack) != 1:
        raise ValueError("Invalid final state: Stack should contain exactly one value.")

    return stack[0]

def main():
    file_path = "program.asm"

    try:
        final_value = execute_assembly(file_path)
        print(f"Final computed value: {final_value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

