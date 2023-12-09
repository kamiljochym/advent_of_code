total = 0
file = open("1input", "r")

for line in file:

    print(line)

    digitsOnly = filter(str.isdigit, line)

    digitsOnly = "".join(digitsOnly)

    print(digitsOnly)
    

    lineSum = eval(digitsOnly[0] + digitsOnly[len(digitsOnly)-1])
    total += lineSum

print(total)

