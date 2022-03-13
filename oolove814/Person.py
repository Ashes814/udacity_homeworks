# -*- coding: utf-8 -*-
"""Introduction to Person class

This module defines basic attributes of a person



"""
class Person(object):
    """A Person class contains basic human attributes

    Attributes:
        birthday (date): the day of a person borns
        age (int): the age of a person
        sex (str): male or female
        height (float): height in cm
        weight (float): weight in kg
    """

    def __init__(self, birthday, age, sex, height, weight):
        """Initializae basic attributes

        Args:
            birthday (date): the day of a person borns
            age (int): the age of a person
            sex (str): male or female
            height (float): height in cm
            weight (float): weight in kg
        """
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def calculate_age(self):
        pass

    def 