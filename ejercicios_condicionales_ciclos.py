# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:38:03 2021

@author: LENOVO
"""
a = int(input("Entre un número entero: "))

b = int(input("Entre otro número entero: "))

c = int(input("Entre un tercer número entero: "))

if a <= b and b <= c:

        print("a", a, "b", b, "c", c)

else:

       if a <= c and c <= b:

              print("a", a, "c", c, "b", b)

       else:

             if b <= a and a <= c:

                     print("b", b, "a", a, "c", c)

            else:

                     if b <= c and c <= a:

                         print("b", b, "c", c, "a", a)

                     else:

                          if c <= a and a <= b:

                               print("c", c, "a", a, "b", b)

                         else:

                               print("c", c, "b", b, "a", a)