def add(a, b, c):
    res = a + b + c
    return res


def addition(*args):  # list
    """
        returns the sum of all the numbers passed as arguments
    :param:
        integers or floats or a mix of integers and floatd
    :return:
        integers or floats
    """
    total = sum(args)
    return total


# call function
print(add(9, 7, 5))

print(addition(5, 15, 37, 4, 52, 93))


def build_portfolio(**kwargs):  # dict key-word args
    for k, w in kwargs.items():
        print(f"{k}: {w}")


def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


build_portfolio(age=100, name="Jane", profession="programming", gender="female")


# anonymous == lambda
def square(num):
    return num * num


result = square(5)
print(result)

square = lambda num: num * num

print(square(5))
res= square(2.9)
print(res)

surface_area_cylinder = lambda r, h: 22/7 * r **2 *2 + 22/7 * 2 * r * h

print(surface_area_cylinder(13, 40))

people = [
    {"name": "Alex", "age" : 30},
    {"name": "Bob", "age": 23},
    {"name": "Alvin", "age": 56},
]

#lambda x : x['age']
sorted_by_age= sorted(people, key=lambda x: x["age"], reverse=True)

print(sorted_by_age)

