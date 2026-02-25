
# Sal's Shipping Company

weight = 41.5

# Ground Shipping:

def calculate_ground_shipping(weight):
  if weight <= 2:
    #cost_ground = weight * 1.5 + 20
    return weight * 1.5 + 20
  elif weight <= 6:
    #cost_ground = weight * 3.0 + 20
    return weight * 3.0 + 20
  elif weight <= 10:
    #cost_ground = weight * 4.0 + 20
    return weight * 4.0 + 20
  else:
    #cost_ground = weight * 4.75 +20
    return weight * 4.75 + 20
cost_ground = calculate_ground_shipping(weight)

print("Ground Shipping $",cost_ground)

# Ground Shipping Premium:

cost_ground_premium = 125.00

print("Ground Shipping Premium $",cost_ground_premium)

# Drone Shipping:

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping $",cost_drone)

# Determining the cheapest shipping method and Displaying it:

cheapest_method = min(cost_ground, cost_ground_premium, cost_drone)

if cheapest_method == cost_ground:
    print("Cheapest method is Ground Shipping: $", cost_ground)
elif cheapest_method == cost_ground_premium:
    print("Cheapest method is Ground Shipping Premium: $", cost_ground_premium)
else:
    print("Cheapest method is Drone Shipping: $", cost_drone)

# End of the program! Thank you :)



