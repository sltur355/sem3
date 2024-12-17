import sys

def get_coeff(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректное значение. Пожалуйста, введите действительное число.")

def find_roots(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен нулю для биквадратного уравнения.")
        return []

    # Вычисляем дискриминант
    d = b**2 - 4*a*c

    if d < 0:
        print("Нет действительных корней.")
        return []
    elif d == 0:
        root = -b / (2*a)
        return [root**0.5, -root**0.5] if root >= 0 else []
    else:
        sqrt_d = d**0.5
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)

        roots = []
        if root1 >= 0:
            roots.append(root1**0.5)
            roots.append(-root1**0.5)
        if root2 >= 0:
            roots.append(root2**0.5)
            roots.append(-root2**0.5)

        return roots

def main():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные значения в командной строке. Пожалуйста, введите коэффициенты заново.")
            a = get_coeff("Введите коэффициент A: ")
            b = get_coeff("Введите коэффициент B: ")
            c = get_coeff("Введите коэффициент C: ")
    else:
        a = get_coeff("Введите коэффициент A: ")
        b = get_coeff("Введите коэффициент B: ")
        c = get_coeff("Введите коэффициент C: ")

    roots = find_roots(a, b, c)

    if roots:
        print("Действительные корни биквадратного уравнения:")
        for root in roots:
            print(root)

if __name__ == "__main__":
    main()
