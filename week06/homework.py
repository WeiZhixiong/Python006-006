#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, food_type, shape, character):
        self.food_type = food_type
        self.shape = shape
        self.character = character
        self.is_fierce_animal = True \
            if shape != "小" and food_type == "食肉" and character == "性格凶猛" \
            else False


class Cat(Animal):

    voice = "喵～"

    def __init__(self, name, food_type, shape, character):
        super().__init__(food_type, shape, character)
        self.name = name
        self.suitable_for_pets = False if self.is_fierce_animal else True


class Dog(Animal):

    voice = "汪汪汪～"

    def __init__(self, name, food_type, shape, character):
        super().__init__(food_type, shape, character)
        self.name = name
        self.suitable_for_pets = False if self.is_fierce_animal else True


class Zoo:

    def __init__(self, name):
        self.name = name
        self.__animals = {}

    def add_animal(self, animal):
        animal_class_name = animal.__class__.__name__
        if animal_class_name in self.__animals:
            print(f"已经有「{animal_class_name}」，不能再加啦～")
        else:
            self.__animals[animal_class_name] = animal

    def __getattr__(self, item):
        if item in self.__animals:
            return self.__animals[item]
        else:
            raise AttributeError(f"No {item} attribute")


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化两只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(cat1.is_fierce_animal)
    print(cat1.suitable_for_pets)

    cat2 = Cat('大花猫 2', '食肉', '大', '性格凶猛')
    print(cat2.is_fierce_animal)
    print(cat2.suitable_for_pets)

    # 增加两只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

    have_cat = hasattr(z, 'Dog')
    print(have_cat)
