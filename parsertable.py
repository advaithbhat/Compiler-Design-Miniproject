# This file contains the tokens,grammar productions and parsing table in a class called Compiler.

class Compiler(object):

    # Dictionary which contains the various tokens.
    tokens = {'int': 'a',' ': 'b','main': 'c','(': 'd',')': 'e','\n': 'f','begin': 'g','var': 'm','=': 'i',
              'print': 'j','end': 'k',';': 'l',',': 'n','float': 'o','+': 'p','-': 'q','*': 'r','/': 's','%': 't',
              'num': 'u'}


    # Grammar productions
    productions = [
        ['S-', 'S'],
        ['S', 'abcdefgfAfgfmbibBfjdmefkfk'],
        ['A', 'CbDl'],
        ['D', 'mnD'],
        ['D', 'mnbD'],
        ['D', 'm'],
        ['C', 'a'],
        ['C', 'o'],
        ['B', 'El'],
        ['E', 'EpT'],
        ['E', 'EqT'],
        ['E', 'T'],
        ['T', 'TrF'],
        ['T', 'TsF'],
        ['T', 'TtF'],
        ['T', 'F'],
        ['F', 'dEe'],
        ['F', 'm'],
        ['F', 'u'],
    ]



    # Parsing Table which is obtained from the itemset
    parse_table = {
        '0': {'a': 'S2', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': '1'},
        '1': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'A', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '2': {'a': 'E', 'b': 'S3', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '3': {'a': 'E', 'b': 'E', 'c': 'S4', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '4': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S5', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '5': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'S6', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '6': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S7', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '7': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'S8', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '8': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S9', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '9': {'a': 'S12', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'S13', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': '10', 'B': 'E', 'C': '11', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '10': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S14', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '11': {'a': 'E', 'b': 'S15', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '12': {'a': 'E', 'b': 'R6', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '13': {'a': 'E', 'b': 'R7', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '14': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'S16', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '15': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S18', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': '17', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '16': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S19', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '17': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'S20', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '18': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R5', 'm': 'E', 'n': 'S21', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '19': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S22', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '20': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'R2', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '21': {'a': 'E', 'b': 'S24', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S18', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': '23', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '22': {'a': 'E', 'b': 'S25', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '23': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R3', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '24': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S18', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': '26', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '25': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'S27', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '26': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R4', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '27': {'a': 'E', 'b': 'S28', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '28': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': '29', 'C': 'E', 'D': 'E', 'E': '30', 'T': '31', 'F': '32', 'S': 'E'},
        '29': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S36', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '30': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'S37', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'S38', 'q': 'S39', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '31': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R11', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R11', 'q': 'R11', 'r': 'S40', 's': 'S41', 't': 'S42', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '32': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R15', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R15', 'q': 'R15', 'r': 'R15', 's': 'R15', 't': 'R15', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '33': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': '43', 'T': '44', 'F': '45', 'S': 'E'},
        '34': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R17', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R17', 'q': 'R17', 'r': 'R17', 's': 'R17', 't': 'R17', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '35': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R18', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R18', 'q': 'R18', 'r': 'R18', 's': 'R18', 't': 'R18', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '36': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'S49', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '37': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'R8', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '38': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': '50', 'F': '32', 'S': 'E'},
        '39': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': '51', 'F': '32', 'S': 'E'},
        '40': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '52', 'S': 'E'},
        '41': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '53', 'S': 'E'},
        '42': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S33', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S34', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S35', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '54', 'S': 'E'},
        '43': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'S55', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'S56', 'q': 'S57', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '44': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R11', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R11', 'q': 'R11', 'r': 'S58', 's': 'S59', 't': 'S60', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '45': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R15', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R15', 'q': 'R15', 'r': 'R15', 's': 'R15', 't': 'R15', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '46': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': '61', 'T': '44', 'F': '45', 'S': 'E'},
        '47': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R17', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R17', 'q': 'R17', 'r': 'R17', 's': 'R17', 't': 'R17', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '48': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R18', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R18', 'q': 'R18', 'r': 'R18', 's': 'R18', 't': 'R18', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '49': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S62', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '50': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R9', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R9', 'q': 'R9', 'r': 'S40', 's': 'S41', 't': 'S42', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '51': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R10', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R10', 'q': 'R10', 'r': 'S40', 's': 'S41', 't': 'S42', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '52': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R12', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R12', 'q': 'R12', 'r': 'R12', 's': 'R12', 't': 'R12', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '53': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R13', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R13', 'q': 'R13', 'r': 'R13', 's': 'R13', 't': 'R13', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '54': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R14', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R14', 'q': 'R14', 'r': 'R14', 's': 'R14', 't': 'R14', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '55': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'R16', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R16', 'q': 'R16', 'r': 'R16', 's': 'R16', 't': 'R16', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '56': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': '63', 'F': '45', 'S': 'E'},
        '57': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': '64', 'F': '45', 'S': 'E'},
        '58': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '65', 'S': 'E'},
        '59': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '66', 'S': 'E'},
        '60': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'S46', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S47', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'S48', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': '67', 'S': 'E'},
        '61': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'S68', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'S56', 'q': 'S57', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '62': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'S69', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '63': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R9', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R9', 'q': 'R9', 'r': 'S58', 's': 'S59', 't': 'S60', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '64': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R10', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R10', 'q': 'R10', 'r': 'S58', 's': 'S59', 't': 'S60', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '65': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R12', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R12', 'q': 'R12', 'r': 'R12', 's': 'R12', 't': 'R12', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '66': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R13', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R13', 'q': 'R13', 'r': 'R13', 's': 'R13', 't': 'R13', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '67': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R14', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R14', 'q': 'R14', 'r': 'R14', 's': 'R14', 't': 'R14', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '68': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'R16', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'R16', 'q': 'R16', 'r': 'R16', 's': 'R16', 't': 'R16', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '69': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'S70', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '70': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S71', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '71': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'S72', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '72': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'S73', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '73': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'S74', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'E', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
        '74': {'a': 'E', 'b': 'E', 'c': 'E', 'd': 'E', 'e': 'E', 'f': 'E', 'g': 'E', 'i': 'E', 'j': 'E', 'k': 'E', 'l': 'E', 'm': 'E', 'n': 'E', 'o': 'E', 'p': 'E', 'q': 'E', 'r': 'E', 's': 'E', 't': 'E', 'u': 'E', '$': 'R1', 'A': 'E', 'B': 'E', 'C': 'E', 'D': 'E', 'E': 'E', 'T': 'E', 'F': 'E', 'S': 'E'},
    }