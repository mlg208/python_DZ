def volume (diameter, height):
    radius = diameter / 2
    volum = 3 * radius**2 * height
    volume_literes = volum * 1000
    return volume_literes
diameter = int(input("введите диаметр бака в метрах"))
height = int(input("введите высоту бака в метрах"))
result = volume (diameter, height)
print (result)