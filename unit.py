import random

questions = [
    ["π/6","1/2", "(3)/2", "(3)/3"],
    ["π/4", "(2)/2", "(2)/2", "1"],
    ["π/3", "(3)/2", "1/2", "(3)"],
    ["π/2", "1", "0", "DNE"],
    ["2π/3", "(3)/2", "-1/2", "-(3)"],
    ["3π/4", "(2)/2", "-(2)/2", "-1"],
    ["5π/6", "1/2", "-(3)/2", "-(3)/3"],
    ["π", "0", "-1", "0"],
    ["7π/6", "-1/2", "-(3)/2", "(3)/3"],
    ["5π/4", "-(2)/2", "-(2)/2", "1"],
    ["4π/3", "-(3)/2", "-1/2", "(3)"],
    ["3π/2", "-1", "0", "DNE"],
    ["5π/3", "-(3)/2", "1/2", "-(3)"],
    ["7π/4", "-(2)/2", "(2)/2", "-1"],
    ["11π/6", "-1/2", "(3)/2", "-(3)/3"],
    ["0", "0", "1", "0"],
    ["2π", "0", "1", "0"],
]

while True:
    op = random.randint(1,3)
    value = random.randint(0,16)
    stringop = ""
    if op == 1:
        stringop = "sin"
    elif op == 2:
        stringop = "cos"
    else:
        stringop = "tan"
    inval = input(stringop + "(" + questions[value][0] + ") = ")
    if(inval == questions[value][op]):
        print("Correct!")
    else:
        print("Sorry it was: " + questions[value][op])
