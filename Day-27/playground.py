# # enable infinite number of arguments by using *args within () of method name
# def add(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
#
# # this argument passed is of type <tuple> which consists of the following items
# # add(5, 7, 5)
#
#
# # UNLIMITED KEYWORD ARGUMENTS
# def calculate(n, **kwargs):
#     print(kwargs)
#     # print(type(kwargs))                     # the kwargs is a dict
#     # print(kwargs["add"])                    # access a specific value of kwargs using its key
#     # for key, value in kwargs.items():       # looping through the dictionary kwargs
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)              # the passed arguments have now become the kwargs
class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")      # kw["make"]
        self.model = kw.get("model")    # kw["model"]
        self.color = kw.get("color")    # kw["color"]
        self.seats = kw.get("seats")    # kw["seats"]
    # [] raises an error if a specific kw has been called, but it does not exist
    # get() doesn't raise any error even if the kw doesn't exist, just returns None


car = Car(make="Nissan", color="Blue", seats=6)
print(car.make, car.model, car.color, car.seats)
