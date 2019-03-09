n = int(input('Enter number of rules: '))
rules = {}
for i in range(n):
    a, b = map(str.strip, input('Enter rule ' + str(i+1) + ': ').split('='))
    rules[a] = list(map(list, map(str.strip, b.split('|'))))

x = rules.copy()
for i in x:
    rec = []
    rules[i+"'"] = []
    for j in x[i]:
        if j[0] == i:
            rules[i+"'"].append(j[1:] + [i+"'"])
            rec.append(j)
    if rec:
        rules[i+"'"].append(['$'])
        for j in rec:
            rules[i].remove(j)
        for k in x[i]:
            k.append(i+"'")
    else:
        del rules[i+"'"]

for i in rules:
    for j in range(len(rules[i])):
        rules[i][j] = ''.join(rules[i][j])
    print(i + ' = ' + ' | '.join(map(str, rules[i])))
