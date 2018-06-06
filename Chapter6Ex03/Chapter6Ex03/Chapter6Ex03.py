#Sphere_Area_Volume.py
#chaper 6 example 3
#    Sphere functions

import math

def sphereArea(radius):
    return 4 * math.pi * radius * radius

def sphereVolume(radius):
    return 4.0/3.0 * math.pi * radius**3

def main():
    print("This program computes some properties of a sphere\n")

    radius = float(input("Please enter the radius of the sphere: "))
    print("\nThe surface area for the sphere is %0.2f square units." % (sphereArea(radius)))
    print("The volume for the sphere is %0.2f cubic units." % (sphereVolume(radius)))

main()

