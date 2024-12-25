int1 = 1002 # global variable

def check_scope():
  global int1
  int1 += 1

print(int1)
check_scope()
print(int1)

check_scope()
check_scope()
print(int1)