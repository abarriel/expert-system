from parser import parseArg, parseFile
from tools import bc
def main():
    global args
    args = parseArg()
    facts, goals, rules, dic = parseFile(args.filename)

    if args.verbose:
        print(bc.GREEN + 'Facts:', list(facts.keys()), bc.RES, "\n")
        print(bc.BLUE + 'Goals:', list(goals.keys()), bc.RES, "\n")
        for rule in rules:
            if rule[2] == '!ssi':
                print(bc.YELLOW, rule[0], '=>', rule[1], bc.RES)
            if rule[2] == 'ssi':
                print(bc.GREEN, rule[0], '<=>', rule[1], bc.RES)

if __name__ == "__main__":
    main()
        
    