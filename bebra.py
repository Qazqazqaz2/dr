import sympy as sp

def main():
    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0:")
    a = float(input())
    b = float(input())
    c = float(input())
    print("Введите начальное приближение x0:")
    x0 = float(input())
    print("Введите требуемую точность epsilon:")
    epsilon = float(input())

    print("Метод Ньютона:")
    newton_iterations, newton_root = newton_method(a, b, c, x0, epsilon)
    print("Количество итераций:", newton_iterations)
    print("Корень:", newton_root)

    print("Метод простых итераций:")
    simple_iterations, simple_root = simple_iteration_method(a, b, c, x0, epsilon)
    print("Количество итераций:", simple_iterations)
    if diff(a, b, c, x0)<1:
        print("Корень:", simple_root)
    else:
        print("Нет корня")


def function(a, b, c, x):
    return a * x * x + b * x + c


def derivative(a, b, x):
    return 2 * a * x + b


def newton_method(a, b, c, x0, epsilon):
    iterations = 0
    while abs(function(a, b, c, x0)) > epsilon:
        x0 = x0 - function(a, b, c, x0) / derivative(a, b, x0)
        iterations += 1
    return iterations, x0

def diff(a, b, c, x0):

    a = sp.Symbol('a')
    b = sp.Symbol('b')
    c = sp.Symbol('c')
    x0 = sp.Symbol('x0')

    # Определение выражения
    expr = -c / (a * x0 + b)

    # Вычисление производной
    derivative = sp.diff(expr, x0)

    # Вывод результата
    return derivative

def simple_iteration_method(a, b, c, x0, epsilon):
    iterations = 0
    x1 = x0
    while abs(function(a, b, c, x1)) > epsilon:
        x1 = -c / (a * x0 + b)
        x0 = x1
        iterations += 1
    return iterations, x1


if __name__ == "__main__":
    main()
