import string 

# Alphabet
atoms = list(string.ascii_lowercase)
operatores = ['#', '>', '&', '-'] 
delimiters = ['(', ')']


class Analyzer:
    # Removing blank spaces
    def format(self, formula) -> str:
        return formula.replace(" ", "")

    # Looking for minors issues
    def lexerAnalyzer(self, formula) -> bool:
        open = close = 0

        if len(formula) == 1 and formula[0] in operatores:
            return False
        elif len(formula) == 1 and formula[0] in delimiters:
            return False

        tokens = []

        for i in formula:
            if i == '(':
                open += 1
            if i == ')':
                close += 1
            tokens.append(i)

        if open != close:
            return False
    
        flag = False # flag is a var to check if there's an atoms in formula
        for token in tokens:
            if token in atoms:
                flag = True

            if not token in atoms and not token in operatores and not token in delimiters:
                return False
        return (True and flag)

    # Check majors issues
    def Verify(self, curr, next, prev = '-'):
        if curr == '-':
            if prev in atoms:
                return False

            if not (next in atoms or next == '-' or next == '('):
                return False

        elif curr == '(':
            if not (next in atoms or next == '(' or next == '-'):
               return False  
        elif curr in atoms:
            if not (next in operatores or next == ')'):
                return False
        elif curr in operatores:
            if not (next in atoms or next == '(' or next == '-'):
                return False
        else:
            if not (next == ')' or next in operatores):
                return False
        return True


    def semanticAnalyzer(self, formula) -> bool:
        formula = self.format(formula)
        response = self.lexerAnalyzer(formula)
        state = True

        if response:
            if formula[-1] in operatores: # if there's an operator in last position
                return False

            if formula[0] == '(':
                if formula[-1] != ')':
                    return False
            else:
                if formula[-1] == ')':
                    return False

     
            for i in range(0, len(formula) - 1):
                if i == 0:
                    state = self.Verify(formula[i], formula[i+1])
                else:
                    state = self.Verify(formula[i], formula[i+1], formula[i-1])

                if state == False:
                    break
            return state
        else:
            return False

    def isFormula(self, formula) -> bool:
        return self.semanticAnalyzer(formula)
