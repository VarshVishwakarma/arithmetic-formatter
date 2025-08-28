def arithmetic_arranger(problems, val=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_row = []
    second_row = []
    dashes = []
    solutions = []

    for prob in problems:
        parts = prob.split()
        num1, op, num2 = parts[0], parts[1], parts[2]

        # Operator validation
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Digits validation
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Length validation
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Width of each problem
        width = max(len(num1), len(num2)) + 2

        # Build formatted rows
        first_row.append(num1.rjust(width))
        second_row.append(op + num2.rjust(width - 1))
        dashes.append("-" * width)

        if val:
            if op == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            solutions.append(result.rjust(width))

    arranged = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n" + "    ".join(dashes)
    if val:
        arranged += "\n" + "    ".join(solutions)

    return arranged
