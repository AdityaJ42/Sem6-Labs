# Left Recursion

n = int(input('Enter the number of rules: '))
rules = {}
for i in range(n):
    prod = input('Enter rule {}: '.format(i + 1)).split('->')
    rules[prod[0]] = prod[1].split('|')
temp = rules.copy()

for i in temp:
    rec = []
    rules[i + "'"] = []

    for j in temp[i]:
        if j[0] == i:
            rules[i + "'"].append(j[1:] + (i + "'"))
            rec.append(j)
    if rec:
        rules[i + "'"].append('@')
        for j in rec:
            rules[i].remove(j)
        for k in range(len(rules[i])):
            rules[i][k] += i + "'"
    else:
        del rules[i + "'"]

for i in rules:
    print('{} -> {}'.format(i, '|'.join(rules[i])))
