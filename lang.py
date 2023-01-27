"""Language for the LIT programming language"""


########################################
# TOKENS
########################################

class Token:
    def __init__(self, tok_name, tok_value=None):
        self.tok_name = tok_name
        self.tok_value = tok_value

    def __repr__(self):
        if not self.tok_value:
            return f"{self.tok_name}"
        else:
            return f"{self.tok_name}:{self.tok_value}"

class OPERATOR(Token):
    def __init__(self, val):
        super().__init__("OPERATOR", val)

class NUM(Token):
    def __init__(self, val):
        super().__init__("NUM", val)

########################################
# ERROR 
########################################

class Error:
    def __init__(self, error_type, error_message):
        self.error_message = error_message
        self.error_type = error_type
    def raise_error(self):
        print(f"{self.__class__.__name__}: {self.error_message}")

class LitSyntaxError(Error):
    def __init__(self, error_message):
        super().__init__("LitSyntaxError", error_message)
        super().raise_error()

class LitTokenError(Error):
    def __init__(self, error_message):
        super().__init__("LitTokenError", error_message)
        super().raise_error()



########################################
# LEXER 
########################################


class Lexer:
    def __init__(self):
        pass

    def create_tokens(self, text: str):
        tokens = []
        text = text.strip(" ")
        current_char = 0
        number_string = "0123456789"

        while current_char < len(text):
            char = text[current_char]
            if char in number_string:
                num = self.create_number(current_char, text)
                tokens.append(num[0])
                current_char = num[1]
                continue


            if char == "+":
                tokens.append(OPERATOR("PLUS"))
            elif char == "-":
                tokens.append(OPERATOR("MINUS"))
            elif char == "/":
                tokens.append(OPERATOR("DIVIDE"))
            elif char == "*":
                tokens.append(OPERATOR("MULTIPLY"))
            else:
                if char != " ":
                    LitTokenError("Unrecognised Token").raise_error()
                    current_char += 1
                    break
            

            current_char += 1

        return tokens
    def create_number(self, current_char, text):
        number_end = False
        number = ""
        while not number_end:
            number += text[current_char]
            current_char += 1
            try:
                if text[current_char] not in "0123456789":
                    number_end = True
            except:
                number_end = True
        return (NUM(number), current_char)

########################################
# Syntax Checker
########################################

class SyntaxChecker:
    def __init__(self):
        pass
    def check_syntax(self, tokens):
        if len(tokens) < 2:
            return
        else:
            last_tok = Token("NONETYPE", "NONE")
            for tok in tokens:
                if last_tok.tok_name == "NUM" and tok.tok_name == "NUM":
                    return LitSyntaxError(f"Invalid Syntax")
        




def start(code):
    lexer = Lexer()
    print(lexer.create_tokens(code))