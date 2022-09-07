#!/usr/bin/env python3

class People: 
    def __init__(self, name):
        self.name = name

    def sayHello(self): 
        print(f"Hello, {self.name}!")


man = People("John")
print(man.sayHello())


