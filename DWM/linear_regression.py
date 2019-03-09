def read_data():
	fd = open('Data.csv')
	x = []
	y = []
	for n, line in enumerate(fd):
		if n != 0:
			content = line.strip().split(',')
			x.append(int(content[0]))
			y.append(int(content[1]))
	return x, y


def find_coefficients(x, y):
	sum_x, sum_y, sum_xy, sum_x2 = 0, 0, 0, 0
	n = len(x)

	for i in range(n):
		sum_x += x[i]
		sum_y += y[i]
		sum_xy += x[i] * y[i]
		sum_x2 += x[i] ** 2

	m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
	m = round(m, 4)
	c = (sum_y - m * sum_x) / n
	c = round(c, 4)
	return m, c


def calculate(m, x, c):
	return round(m * x + c, 2)

input_x = int(input('Enter the value of x: '))
x, y = read_data()
m, c = find_coefficients(x, y)
eqn = 'y = ' + str(c) + ' + ' + str(m) + 'x'
predicted = calculate(m, input_x, c)
print("Equation of Line: " + eqn)
print("Predicted value of y: " + str(predicted))
