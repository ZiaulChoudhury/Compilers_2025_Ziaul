class Parser:
    def __init__(self, input_data):
        self.input_data = iter(input_data)
        self.lookahead = next(self.input_data, None)
        self.output = []  # List to store the postfix result

    def expro(self):
        self.term()
        while True:
            if self.lookahead == '+':
                self.match('+')
                self.term()
                self.output.append('+')
            elif self.lookahead == '-':
                self.match('-')
                self.term()
                self.output.append('-')
            else:
                return ''.join(self.output)

    def term(self):
        if self.lookahead and self.lookahead.isdigit():
            self.output.append(self.lookahead)
            self.match(self.lookahead)
        else:
            raise SyntaxError("syntax error")

    def match(self, t):
        if self.lookahead == t:
            self.lookahead = next(self.input_data, None)
        else:
            raise SyntaxError("syntax error")

# Function to evaluate postfix expressions
def evaluate_postfix(postfix):
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        elif char in '+-':
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
    return stack[0]

# Function to evaluate infix expressions
def evaluate_infix(expression):
    return eval(expression)

# Check function to verify the parser
def check(expression):
    parser = Parser(expression)
    postfix_result = parser.expro()

    # Compute results for infix and postfix
    infix_value = evaluate_infix(expression)
    postfix_value = evaluate_postfix(postfix_result)

    print(f"Infix Expression: {expression}")
    print(f"Postfix Expression: {postfix_result}")
    print(f"Infix Value: {infix_value}, Postfix Value: {postfix_value}")

    # Compare results
    if infix_value == postfix_value:
        print("PASS")
    else:
        print("FAIL")

# Testing with the input "3+5-2+3-6"
input_expression = "3+5-2+3-6"
check(input_expression)

