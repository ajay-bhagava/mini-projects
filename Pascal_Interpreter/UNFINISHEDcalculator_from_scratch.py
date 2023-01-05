INTEGER, PLUS, MINUS, EOF = "INTEGER", "+", "-", "NONE"

class Token(object):
    def __init__(self, type, value) -> None:
         self.type = type
         self.value = value

class Interpreter(object):
    def __init__(self, text) -> None:
          self.pos = 0
          self.text = text
          self.currentToken = None
          self.currentChar = self.text[self.pos]
    
    def shiftForward(self):
        self.pos += 1
        if self.pos > len(self.text):
            self.currentChar = None
        else:
            self.currentChar = self.text[self.pos]
    
    #only going to be called when the first char of token is an int 
    def tokenInt(self):
        result = self.currentChar
        self.shiftForward()
        while self.currentChar.isdigit():
            result += self.currentChar
            self.shiftForward()
        return Token(INTEGER, int(result))

    def tokenOperator(self):
        result = self.currentChar
        self.shiftForward()
        if result == "+":
            return Token(PLUS, result)
        elif result == "-":
            return Token(MINUS, result)  
        
        print("This shouldnt be reached")
    
    def skipWhiteSpace(self):
        while self.currentChar == " ":
            self.shiftForward()
    
    def grabTokenAndShift(self):
        if self.currentChar is not None:
            if self.currentChar == " ":
                self.skipWhiteSpace()
            
            if self.currentChar.isdigit() and self.currentChar is not None:
                self.tokenInt()

            if self.currentChar in (PLUS, MINUS):
                self.tokenOperator()
            

        return Token(EOF, "None")
    
    def exec(self):
        token = self.grabTokenAndShift()
        if token.value.isdigit():
            result = token.value
        else:
            raise Exception("First input must be a number")
        
        while token.type is not EOF:
            token = self.grabTokenAndShift()
            
            if token.type == PLUS:
                token = self.grabTokenAndShift()
                result += token.value
            elif token.type == MINUS:
                token = self.grabTokenAndShift()
                result -= token.value
        
        return result

while True: 
    text = input("calc> ")
    interp = Interpreter(text)
    print(interp.exec())
