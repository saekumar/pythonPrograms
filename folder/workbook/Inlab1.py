def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
   
    if targetCapacity > jug1Capacity + jug2Capacity or targetCapacity < 0:
        return False

    if targetCapacity == jug1Capacity or targetCapacity == jug2Capacity or targetCapacity == jug1Capacity + jug2Capacity:
        return True

   
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

   
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
jug1Capacity = 3  # Capacity of first jug
jug2Capacity = 5  # Capacity of second jug
targetCapacity = 4  # Capacity to measure

if canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    print("It is possible to measure exactly {} liters using jugs with capacities {} and {}.".format(targetCapacity, jug1Capacity, jug2Capacity))
else:
    print("It is impossible to measure exactly {} liters using jugs with capacities {} and {}.".format(targetCapacity, jug1Capacity, jug2Capacity))
