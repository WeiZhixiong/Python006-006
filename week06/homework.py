#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        self.suitable_for_pets = not self.is_fierce_animal


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
        if animal_class_name not in self.__animals:
            self.__animals[animal_class_name] = {}

        animal_id = id(animal)
        if animal_id in self.__animals[animal_class_name]:
            logger.info(f"已经有 id 为 {animal_id} 的「{animal_class_name}」，不能再加啦～")
        else:
            self.__animals[animal_class_name][animal_id] = animal

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
    logger.info(cat1.is_fierce_animal)
    logger.info(cat1.suitable_for_pets)

    cat2 = Cat('大花猫 2', '食肉', '大', '性格凶猛')
    logger.info(cat2.is_fierce_animal)
    logger.info(cat2.suitable_for_pets)

    # 增加两只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(cat2)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    logger.info(have_cat)

    have_dog = hasattr(z, 'Dog')
    logger.info(have_dog)
