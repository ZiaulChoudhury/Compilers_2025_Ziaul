class HypotheticalCPU:
    def __init__(self, memory_size=1024):
        """
        Initializes the CPU with memory and registers.

        Parameters:
            memory_size (int): Size of the memory array.
        """
        self.memory = [0] * memory_size  # Memory array
        self.R1 = 0  # General-purpose register 1
        self.R2 = 0  # General-purpose register 2
        self.result = 0  # Result register

    def load_to_memory(self, address, value):
        """
        Loads a value into a specified memory address.

        Parameters:
            address (int): Memory address.
            value (int): Value to load.
        """
        if address < 0 or address >= len(self.memory):
            raise ValueError("Invalid memory address.")
        self.memory[address] = value

    def execute_program(self, program):
        """
        Executes an assembly program.

        Parameters:
            program (List[str]): List of assembly instructions.
        """
        for instruction in program:
            print(f"Processing instruction: {instruction}")  # Debug logging
            self.decode_and_execute(instruction)

    def decode_and_execute(self, instruction):
        """
        Decodes and executes a single instruction.

        Parameters:
            instruction (str): The assembly instruction.
        """
        # Preprocess instruction to remove commas and unnecessary whitespace
        instruction = instruction.replace(",", "").strip()
        parts = instruction.split()
        if len(parts) < 2:
            raise ValueError(f"Invalid instruction format: {instruction}")

        operation = parts[0]
        if operation == "LOAD":
            register, value = parts[1], int(parts[2])
            self.memory_read(register, value)
        elif operation in ("ADD", "SUB"):
            self.execute(operation)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    def memory_read(self, register, value):
        """
        Simulates the memory read stage.

        Parameters:
            register (str): The register to load into (R1 or R2).
            value (int): The value to load.
        """
        if register == "R1":
            self.R1 = value
        elif register == "R2":
            self.R2 = value
        else:
            raise ValueError(f"Unknown register: {register}")

    def execute(self, operation):
        """
        Simulates the execute stage.

        Parameters:
            operation (str): The operation to perform (ADD or SUB).
        """
        if operation == "ADD":
            self.result = self.R2 + self.R1
        elif operation == "SUB":
            self.result = self.R2 - self.R1
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        # Simulate write-back stage
        self.write_back()

    def write_back(self):
        """
        Simulates the write-back stage by updating R2 with the result.
        """
        self.R2 = self.result

    def get_final_result(self):
        """
        Returns the final result stored in R2.

        Returns:
            int: Final result in R2.
        """
        return self.R2

# Load and execute assembly program from a file
cpu = HypotheticalCPU()

print("Executing Assembly Program from file 'program.asm':")
with open('program.asm', 'r') as file:
    program = [line.strip() for line in file if line.strip()]
    for instr in program:
        print(instr)
    try:
        cpu.execute_program(program)
    except ValueError as e:
        print(f"Error: {e}")

print("\nFinal Result:", cpu.get_final_result())
