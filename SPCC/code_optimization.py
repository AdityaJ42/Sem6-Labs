import time

def before_optimization_constant_prop():
    x = 7
    y = 14 - x/2
    print("Result:", (y*(28/x+2)))

def after_optimization_constant_prop():
    y = 14 - 7/2
    print("Result:",(y*(28/7+2)))

def before_optimization_code_movement():
    a, b, c = 2, 5, 1
    for _ in range(1, 11):
        temp = a**b
        c *= temp
    print("Result:", c)

def after_optimization_code_movement():
    a, b, c = 2, 5, 1
    temp = a**b
    for _ in range(1, 11):
        c *= temp
    print("Result:", c)

def before_optimization_common_sub_elim():
    r, pi = 10.0, 3.14
    area = r*r*pi
    circum = 2*pi*r
    print("Area of circle:", area)
    print("cirumference of circle:", circum) 

def after_optimization_common_sub_elim():
    r, pi = 10.0, 3.14
    temp = r*pi
    print("Area of circle:", r*temp)
    print("cirumference of circle:", 2*temp) 

def before_optimization_strength_reduction():
    result = 0
    for i in range(1, 11):
        result = i*7
    print("Result:", result)

def after_optimization_strength_reduction():
    result = 0
    for i in range(1, 11):
        result += 7
    print("Result:", result)

def before_optimization_dead_code_elimination():
    a, b = 10, 0
    for i in range(100):
        b += 1
    print("Result:", a)

def after_optimization_dead_code_elimination():
    a = 10
    print("Result:", a)

def check(choice):
    choices = {1: [before_optimization_constant_prop, after_optimization_constant_prop],
               2: [before_optimization_code_movement, after_optimization_code_movement],
               3: [before_optimization_common_sub_elim, after_optimization_common_sub_elim],
               4: [before_optimization_strength_reduction, after_optimization_strength_reduction],
               5: [before_optimization_dead_code_elimination, after_optimization_dead_code_elimination]}
    start = time.time()
    choices[choice][0]()
    print('Time req before opt.' + str(time.time() - start))

    start = time.time()
    choices[choice][1]()
    print('Time req after opt.' + str(time.time() - start))

if __name__ == "__main__":
    print(' Constant Propogation: 1\n',
            'Code Movement: 2\n',
            'Common sub-exp elimination: 3\n',
            'Strength Reduction: 4\n',
            'Dead code elimination: 5\n')
    choice = int(input("Enter choice: "))
    check(choice)