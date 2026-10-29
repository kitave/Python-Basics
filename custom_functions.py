def greet():
    print("Hello World")

def greeting(name):
    print(f"Hello {name}")

def volume_cylinder(radius, height):
    v=22/7 * radius **2 * height
    print(round(v,2))

def volume_cylinder_better(radius, height):
    v = 22/7 * radius **2 * height
    return v

def volume_surface(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 * 2 + 22/7 * radius* 2 * height
    return v, a

#greet() #call == use no arguments/ params == data

result = volume_cylinder_better(6.5, 8.9)
print(result)

# with open("volumes.txt", "w") as file:
    #file.write(str(result))

volume, area = volume_surface(10, 20)
print(f"Volume is {volume} and area is {area}")


#name
v, a = volume_surface(height = 20, radius = 10)
print(f"Volume is {v} and area is {a}")

def divide (a, b, should_round=False):
    res = a/b
    if should_round== True:
        return round(res, 2)
    else:
        return res

print(divide(9, 5.11))






