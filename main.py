# NOTICE

# number of boolean variables are A, B, C, D, etc... specified by an input variable n
# the user can specify the number of rows with another input variable m
# the user must input the truth values they want for the amount of variables they have
# the user starts with an empty row
# the top part of the row is the user input for a specific operation

# for example (A AND B) OR (C AND (NOT D)) is a valid operation for n=4
# AND, OR, NOT are operations that must be included
# the user can also use IMP for imply -> and IAOI for if and only if <->
# the user can use parentheses to group operations

# the bottom part of the row is the result of the operation
# the user can add, edit, or delete rows

# not all the features are implemented yet

import itertools

def parseexpression(expr):
    expr = expr.replace("AND", " and ")
    expr = expr.replace("OR", " or ")
    expr = expr.replace("NOT", " not ")
    
    while "IMP" in expr:
        start = expr.index("IMP")
        left = expr[start - 2:start].strip()
        right = expr[start + 4:start + 5].strip()
        expr = expr[:start - 2] + f"((not {left}) or ({right})) " + expr[start + 5:]
    
    while "IAOI" in expr:
        start = expr.index("IAOI")
        left = expr[start - 2:start].strip()
        right = expr[start + 5:start + 6].strip()
        expr = expr[:start - 2] + f"(({left} and {right}) or (not {left} and not {right})) " + expr[start + 6:]

    return expr

n = int(input("How many variables do you want to work with? "))
vars = [chr(i) for i in range(65, 65 + n)]  # Generate variable names A, B, C, ...
combinations = list(itertools.product([False, True], repeat=n))

expr = input(f"Enter a logical expression using variables {', '.join(vars)}: ")
parsed = parseexpression(expr)

results = []
for c in combinations:
    local = dict(zip(vars, c))
    result = eval(parsed, {}, local)
    results.append(result)

print(" | ".join(vars) + " | Result")
print("-" * (n * 4 + 6))
for combo, res in zip(combinations, results):
    print(" | ".join(str(int(val)) for val in combo) + " | " + str(int(res)))
