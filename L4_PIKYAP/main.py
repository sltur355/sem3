from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import circle
from lab_python_oop.quadrate import quadrate

num = True
while(num):
    print("Введите название фигуры:")
    name = input()

    match(name):
        case "Прямоугольник":
            print("Введите ширину:")
            width = int(input())
            print("Введите высоту:")
            height = int(input())
            print("Введите цвет:")
            color = input()
            item1 = Rectangle(name, height, width, color)
            print(item1.reper())
        case "Круг":
            print("Введите радиус:")
            radius = int(input())
            print("Введите цвет:")
            color = input()
            item2 = circle(name, radius, color)
            print(item2.reper())
        case "Квадрат":
            print("Введите длину стороны:")
            side = int(input())
            print("Введите цвет:")
            color = str(input())
            item3 = quadrate(name, side, color)
            print(item3.reper())
    print("Хотите продолжить? (Да/Нет)")
    procces = input()
    if procces == "Нет":
        num = False
    else:
        num = True
