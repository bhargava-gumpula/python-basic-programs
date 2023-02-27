# Program that checks if parentheses are correct


def parenthesesCheck(string="()"):
        correct = False
        x = 0
        if len(string) % 2 != 0:
	        return correct
        while x <= len(string)//2 + 1:
            
                if string[x] == "(":
                        if string[x+1] == ")":
                                correct = True
                        else:
                            correct = False
                            return correct
                elif string[x] == "[":
                        if string[x+1] == "]":
                                correct = True
                        else:
                            correct = False
                            return correct
                elif string[x] == "{":
                        if string[x+1] == "}":
                                correct = True
                        else:
                            correct = False
                            return correct
                else:
                        correct = False
                        return correct
                
                x = x + 2
        return correct

string = input("Enter your parentheses : ")
string = parenthesesCheck(string)
print(string)
