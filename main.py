from parser import parseArg, parseFile
from tools import bc, printdic

def setdic(dic, facts, val=True):
    for letter in dic:
        for fact in facts:
            dic[fact]['value'] = val

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
        self.dic = dic   
        self.args = args

    def cleanGoals(self):
        self.goals = {k:v for (k,v) in self.goals.items() if self.dic[k]['value'] == None}
    
    def starter(self):
        print(self.goals)
        self.cleanGoals()
        print(self.goals)

# def solve(rules, goals, dic):
#     print(goals);
#     cleanGoals();
#     print(goals);
#     # for goal in goals:
#         # isfound = found(goal, dic, remove = False)
#         # print(isfound)
#     # print(g)
#     # print(goals)
#     # for goal in goals:
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
    facts, goals, rules, dic = parseFile(args.filename)
    setdic(dic, facts)

    if args.verbose:
        print(bc.GREEN + 'Facts:', list(facts.keys()), bc.RES, "\n")
        print(bc.BLUE + 'Goals:', list(goals.keys()), bc.RES, "\n")
        for rule in rules:
            if rule[2] == '!ssi':
                print(bc.YELLOW, rule[0], '=>', rule[1], bc.RES)
            if rule[2] == 'ssi':
                print(bc.GREEN, rule[0], '<=>', rule[1], bc.RES)
        printdic(dic)
        print('\n')
    solve = Solver(rules, goals, dic, args)
    solve.starter()

if __name__ == "__main__":
    main()