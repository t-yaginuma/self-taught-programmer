def even_odd():
  n = input("type a number:")
  n = int(n)

  if n % 2 == 0:
    print("even")
  else:
    print("odd")

def f(x = 2):
  return x ** x

def f2(x, y = 2):
  return x + y

# print(f())
# print(f(10))
print(f2(10))
print(f2(10, 100))