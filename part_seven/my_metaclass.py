# -*- coding:utf-8 -*-
__author__ = "leo"


def get_class(name):
    if name == "dog":
        class Dog:
            def run(self):
                print("dog run")
        return Dog
    else:
        class Cat:
            def run(self):
                print("cat run")
        return Cat


class Person:
    def run(self):
        print("person run")


p = Person
p.run(p)

# d = get_class("dog")
# d.run()
# print(d)