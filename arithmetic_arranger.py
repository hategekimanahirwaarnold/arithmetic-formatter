def arithmetic_arranger(problems):
  topOperands = []
  bottomOperands = []
  signs = []
  widthList = []
  dashes = []
  solutions = []
  for problem in problems:
    splittedProb = problem.split()
    operand1= splittedProb[0]
    sign = splittedProb[1]
    operand2 = splittedProb[2]
    sln = 0
    if sign == "+":
        sln = str(int(operand1) + int(operand2))
    else:
        sln = str(int(operand1) - int(operand2))
    operands = [int(operand1), int(operand2)]
    maxlength = len(str(max(operands)))
    widthList.append(maxlength)
    whitespace1 = maxlength - len(operand1) + 2
    whitespace2 = maxlength - len(operand2) + 1
    whitespace3 = maxlength - len(sln) + 2
    problength = maxlength + 2
    space1 = ""
    space2 = ""
    dash = ""
    space3 = ""
    for sol in range(whitespace3):
        space3 = space3 + " "
    for da in range(problength):
        dash = dash + "-"
    for space in range(whitespace1):
        space1 = space1 + " "
    for space in range(whitespace2):
        space2 = space2 + " "
    topOperands.append(space1 + operand1)
    bottomOperands.append(sign+ space2 + operand2)
    signs.append(sign)
    dashes.append(dash)
    solutions.append(space3 + sln)
  topOperands = "    ".join(topOperands)
  bottomOperands = "    ".join(bottomOperands)
  solutions = "    ".join(solutions)
  dashes = "    ".join(dashes)
  arranged_problems = topOperands + "\n" + bottomOperands + "\n" + dashes + "\n" + solutions
  return arranged_problems