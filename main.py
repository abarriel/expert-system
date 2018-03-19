#!/usr/bin/python3
from parser import parseArg, parseFile
from tools import bc, printdic, clean, error
import re

# def isfound():
#     isfound = 0
#     for letter, key in dic.items():
#         for goal in goals:
#             if letter == goal:
#                 if key['value'] == None:
#                     return None
#                 if key['value'] == True or False:
#                     isfound = letter
#     if isfound != 0
#         del goals[isfound]

# remove item from goal one foiund
# !\(*(#.+?#)[\+\^\|\)]*\)*
class Solver:

    def __init__(self, rules, goals, dic, args):
        self.rules = rules
        self.goals = goals
        # self.stack = goals
        self.dic = dic   
        self.args = args
        self.rcx = 1
        self.loop = 1
    # + = AND
    # | = OR
    # ! = NEG
    # ^ = XOR
    def transformToBool(self, idx, side):
        boolean = self.rules[idx][side + 3]
        for letter, key in self.dic.items():
            letterTrim = '#' + letter + '#'
            if re.search(letterTrim, boolean):
                value = str(key['value'])
                boolean = boolean.replace(letterTrim, value)
        return boolean

    def updateRule(self, oper):
        # letterToFalse = re.search('(!)\(+(#.+?#)\)+', oper)
        lettersToTrue = re.findall('#(.+?)#', oper)
        lettersToFalse = re.findall('#(.+?)#', oper)
        return lettersToTrue, lettersToFalse
    
    def setLetter(self, letters, value):
        for letter in letters:
            if self.dic[letter]['value']:
                error('Pas coehrant true than false?')
            self.dic[letter]['value'] = value

    def looping(self):
        self.rcx = 0
        for idx, rule in enumerate(self.rules):
            boolLeft = eval(self.transformToBool(idx, 0))
            if boolLeft:
                self.rules.pop(idx)
                lettersToTrue, lettersToFalse = self.updateRule(rule[1])
                self.setLetter(lettersToTrue, True)
                self.rcx += 1
        # if self.rcx == 0

    def solver(self):
        while 1 == 1:
            loop = self.looping()
            # if loop = 1
        printdic(self.dic)
        # print(self.rules)
        # self.looping()
        # printrules(rules)        
        # print('\n\n\n\n', self.rules)
        # self.looping()
                    
def printrules(rules):
    for rule in rules:
        if rule[2] == '!ssi':
            print(bc.CYAN, clean(rule[0]), '=>', clean(rule[1]), bc.RES)
        if rule[2] == 'ssi':
            print(bc.GREEN, clean(rule[0]), '<=>', clean(rule[1]), bc.RES)
    print('')

def main():
    global args, facts, goals, rules, dic
    args = parseArg()
    facts, goals, rules, dic = parseFile(args.filename, args.default)

    print(goals)
    if args.verbose:
        print(bc.GREEN + 'Facts:', list(facts.keys()), bc.RES, "\n")
        print(bc.BLUE + 'Goals:', list(goals.keys()), bc.RES, "\n")
        printdic(dic)
        printrules(rules)
    solve = Solver(rules, goals, dic, args)
    solve.solver()

if __name__ == "__main__":
    main()