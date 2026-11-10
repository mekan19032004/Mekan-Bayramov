#!/usr/bin/env python
# Author: Mekan Bayramov
# Date: september  25, 2026
# This program changes speed from KM/H to MPH.
kmh = int(input("Enter km/h: ")) # Ask the user for a speed in KM/H.
mph = 0.6214 * kmh # Change KM/H to MPH.
print("Speed:", kmh, "KM/H = ", mph, "MPH") # Show the speed in both KM/H and MPH.