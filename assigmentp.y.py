#-------------------------------------------------------------------------------
# Name:        module12
# Purpose:
#
# Author:      Dell 5490
#
# Created:     13/01/2024
# Copyright:   (c) Dell 5490 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def estimate_travel_cost(destination, transportation_cost, accommodation_cost, activity_cost, travel_style, duration):
    if travel_style == "budget":
        total_cost = transportation_cost + accommodation_cost + activity_cost
    elif travel_style == "luxury":
        total_cost = 2 * (transportation_cost + accommodation_cost + activity_cost)
    else:
        return "Invalid travel style. Please choose between 'budget' and 'luxury'."

    total_cost *= duration
    return total_cost

# Test the updated function
destination = "Paris"
transportation_cost = 500
accommodation_cost = 1000
activity_cost = 500
travel_style = "budget"
duration = 7

total_cost = estimate_travel_cost(destination, transportation_cost, accommodation_cost, activity_cost, travel_style, duration)
print("The estimated travel cost for", destination, "is $", total_cost)

