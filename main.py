#!/usr/bin/python3
from parser import parseArg, parseFile
from tools import bc, printdic
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
class Solver:

    def __init__(self, rules, goals, dic, args):
        self.rules = rules
        self.goals = goals
        # self.stack = goals
        self.dic = dic   
        self.args = args

    # def cleanGoals(self):
        # self.goals = {k:v for (k,v) in self.goals.items() if self.dic[k]['value'] == None}
        # print(self.goals)
        # self.cleanGoals()
# + = AND
# | = OR
# ! = NEG
# ^ = XOR
    # def loop(self):
    def transformToBool(self, idx, side):
        boolean = self.rules[idx][side]
        for letter, key in self.dic.items():
            letterTrim = '#' + letter + '#'
            if re.search(letterTrim, boolean):
                value = str(key['value'])
                boolean = boolean.replace(letterTrim, value)
        return boolean

    def to_bool(self, value):
        if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
        if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False

    def solver(self):
    # for goal in goals:
    #     goals.pop(d)
    #     isfound = found(goal, dic, remove = False)
    #     print(isfound)
        for idx, rule in enumerate(self.rules):
            print(idx);
            boolLeft = self.transformToBool(idx, 0)
            print(self.to_bool(boolLeft))

            # boolRight = self.transformToBool(idx, 1)
            # print(bool(True ^ True))
        # for goal,i in list(self.goals.items()):
        #     print(goal, i)
            # self.goals[goal] = False
        # print(self.goals)
#     #     for rule in rules:
#     #         if goal in rule[1]:
#     #             print (goal, rule[1])
#     #             found = 1 
#     #         elif rule[2] == 'ssi' and goal in rule[0]:
#     #             print (goal, rule[0])
#     #             found = 1
#     #         else:
#     #             found = 0
#     #     if found != 1:
#     #         for rule in rules:
#     #             if goal in rule[0]:
#     #                 found = 2
#     #                 print (goal, rule[0])
                    
def main():
    global args, facts, goals, rules, dic
    args = parseArg()
    facts, goals, rules, dic = parseFile(args.filename, args.default)

    print(goals)
    if args.verbose:
        print(bc.GREEN + 'Facts:', list(facts.keys()), bc.RES, "\n")
        print(bc.BLUE + 'Goals:', list(goals.keys()), bc.RES, "\n")
        printdic(dic)
        for rule in rules:
            if rule[2] == '!ssi':
                print(bc.YELLOW, rule[0], '=>', rule[1], bc.RES)
            if rule[2] == 'ssi':
                print(bc.GREEN, rule[0], '<=>', rule[1], bc.RES)
        print('\n')
    solve = Solver(rules, goals, dic, args)
    solve.solver()
    if args.verbose:
        for rule in rules:
            if rule[2] == '!ssi':
                print(bc.YELLOW, rule[0], '=>', rule[1], bc.RES)
            if rule[2] == 'ssi':
                print(bc.GREEN, rule[0], '<=>', rule[1], bc.RES)
        print('\n')

if __name__ == "__main__":
    main()