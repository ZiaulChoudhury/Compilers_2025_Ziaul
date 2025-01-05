# Correcting the Parser class for accurate postfix generation
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


# Testing with the input "3+5-2"
input_expression = "3+5-2+3-6"

parser = Parser(input_expression)
correct_postfix_result = parser.expro()
print(correct_postfix_result)
