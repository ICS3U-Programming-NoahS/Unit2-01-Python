#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Sept.21, 2023
# This program calculates and displays the area and perimeter of a
# circle with a radius of 4.9 cm.
import math


def main():
    print("")
    print("For a circle that has a radius of 4.9cm:")
    print("")
    print("Area = {:.2f} cm^2".format(math.pi * 4.9**2))
    print("Circumference = {:.2f} cm".format(2 * math.pi * 4.9))


if __name__ == "__main__":
    main()
