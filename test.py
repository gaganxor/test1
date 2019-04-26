#!C:\Users\XOR SOLUTIONS\AppData\Local\Programs\Python\Python37-32\python.exe

printer("Content-Type: text/html\n")
print ("Hello Python Web Browser!! This is cool!!" + "<br>")



def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

fruits = ["apple", "banana", "cherry"]

points = [1,4,5,9]

fruits.extend(points)

print(fruits)


