from lab_python_oop import abstract , circle , square , rectangle
import black

def main():
    circle_ = circle.circle(20 , 'Красный')
    circle_.repr()

    kvadrat_ = square.kvadrat(30 , 'Зеленый')
    kvadrat_.repr()

    rectangle_ = rectangle.rectangle(10,  40 , 'Синий')
    rectangle_.repr()




if __name__ == '__main__':
    main()
