# -*- coding: utf-8 -*-
for i in range(1,101):
  if i % 5 == 0:
    if i % 3 == 0:
      print("FizzBuzz",i)
    else:
      print("Buzz",i)
  elif i % 3 ==0:
    print("Fizz",i)
  else:
    print(i)
