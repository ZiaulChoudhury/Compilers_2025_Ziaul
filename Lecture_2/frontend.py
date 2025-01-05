import unittest

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
input_expression = "3+2-5"
check(input_expression)

# Unit tests
class TestParser(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(Parser("3+5").expro(), "35+")

    def test_simple_subtraction(self):
        self.assertEqual(Parser("8-4").expro(), "84-")

    def test_combined_operations(self):
        self.assertEqual(Parser("3+5-2").expro(), "35+2-")

    def test_multiple_operations(self):
        self.assertEqual(Parser("3+5-2+4").expro(), "35+2-4+")

    def test_leading_digit(self):
        self.assertEqual(Parser("9+1-3").expro(), "91+3-")

    def test_postfix_evaluation(self):
        self.assertEqual(evaluate_postfix("35+"), 8)

    def test_postfix_subtraction_evaluation(self):
        self.assertEqual(evaluate_postfix("84-"), 4)

    def test_infix_vs_postfix(self):
        expression = "3+5-2"
        postfix = Parser(expression).expro()
        self.assertEqual(evaluate_infix(expression), evaluate_postfix(postfix))

    def test_complex_expression(self):
        expression = "3+5-2+6-4"
        postfix = Parser(expression).expro()
        self.assertEqual(postfix, "35+2-6+4-")
        self.assertEqual(evaluate_infix(expression), evaluate_postfix(postfix))

    def test_invalid_syntax(self):
        with self.assertRaises(SyntaxError):
            Parser("3++5").expro()

if __name__ == "__main__":
    unittest.main()

