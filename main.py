# Student ID: 001204962 --------Camerin Graeff ------- C950 Data Structures and Algorithms II ------- 
import csv
import package
import truck
import distance
from hashtable import Hashtable



def load_packages(filename):
    hash_table = Hashtable()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if not row or not row[0].isdigit():
                continue
            id = int(row[0])
            address = row[1].strip()
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]
            status = "At Hub"

            package_instance = package.Package(id, address, city, state, zip_code, deadline, weight, notes, status)

            hash_table.insert(package_instance)
            
    return hash_table

def total_miles_traveled(trucks):
    total_miles = 0
    for truck in trucks:
        total_miles += truck.truck_total_miles
    return total_miles

def route_truck(truck):
    while truck.packages:
        next_package = choose_next_package(truck)
        truck.delivery(next_package)
        truck.previous_location = truck.current_location
        truck.current_location = next_package.address



"""def choose_next_package(truck):
    if not truck.packages:
        return 'HUB'
    next_package = min(truck.packages, key=lambda p: distance.get_distance(truck.current_location, p.address))
    return next_package"""

def choose_next_package(truck):
    closest_package = None
    closest_distance = float('inf')
    for package in truck.packages:
        dist = float(distance.get_distance(truck.current_location, package.address))
        if dist < closest_distance:
            closest_distance = dist
            closest_package = package
    return closest_package


if __name__ == "__main__":
    hash_table = load_packages("packagefile.csv")
    
    # Test lookup
    truck1 = truck.Truck(1)
    truck2 = truck.Truck(2)

    packages = []

    for bucket in hash_table.table:
        if bucket:
            for p in bucket:
                packages.append(p)

    truck1.load_truck(packages)
    truck2.load_truck(packages)

    route_truck(truck1)
    route_truck(truck2)

    print(total_miles_traveled([truck1, truck2]))
    print("Total miles for Truck 1:", round(truck1.truck_total_miles, 2))
    print("Total miles for Truck 2:", round(truck2.truck_total_miles, 2))