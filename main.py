# Student ID: 001204962 --------Camerin Graeff ------- C950 Data Structures and Algorithms II ------- 
import csv
import package
import truck
import distance
import datetime
from hashtable import Hashtable

# Load and read packages from CSV file, create package instances, and insert them into a hash table for efficient lookup by package ID.
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

# Get a list of packages that are currently at the hub and available for loading onto trucks.
def available_packages(hash_table):
    packages = []
    for bucket in hash_table.table:
        if bucket:
            for p in bucket:
                p.get_deliver_with() # TEST ATM
                if p.status == "At Hub":
                    packages.append(p)
    return packages

# Calculates the total miles traveled by all of the trucks
def total_miles_traveled(trucks):
    total_miles = 0
    for truck in trucks:
        total_miles += truck.truck_total_miles
    return total_miles

# Routes truck by repeatedly choosing the closest package to the truck's current location, delivering it, and updating the truck's location until all packages on the truck are delivered.
def route_truck(truck):
    while truck.packages:
        next_package = choose_next_package(truck)
        truck.delivery(next_package)
        truck.previous_location = truck.current_location
        truck.current_location = next_package.address

# To determine the status of a package at a given query time
def status_at_time(package, query_time):
    if package.delayed is not None and query_time < package.delayed:
        return "Delayed"
    elif package.en_route_time is None or query_time < package.en_route_time:
        return "At Hub"
    elif package.deliver_time is None or query_time < package.deliver_time:
        return "En Route"
    else:
        return "Delivered"

# Used for the menu CLI
def lookup_package_status(hash_table):
    input_query_time = input("Enter time to check package status (HH:MM AM/PM): ")
    input_query_time = datetime.datetime.strptime(input_query_time, "%I:%M %p")
    input_query_time = datetime.timedelta(hours=input_query_time.hour, minutes=input_query_time.minute)
    input_package_id = int(input("Enter package ID to look up: "))
    print("************************************************")
    package = hash_table.lookup(input_package_id)
    if package:
        print(f"Package {input_package_id}\ndelivery address: {package.address} {package.city} {package.zip}\ndeadline: {package.deadline}\nweight: {package.weight}" )
        print(f"Status: {status_at_time(package, input_query_time)}")
    else:
        print("Package not found")

# Chooses the next package for the truck to deliver by finding the package with the closest distance to the truck's current location
def choose_next_package(truck):
    closest_package = None
    closest_distance = float('inf')
    for package in truck.packages:
        dist = float(distance.get_distance(truck.current_location, package.address))
        if dist < closest_distance:
            closest_distance = dist
            closest_package = package
    return closest_package

# for the CLI
def menu():
    print("************************************************")
    print("D.  Provide an intuitive interface for the user to view the DELIVERY STATUS (including the DELIVERY TIME) \n" \
    "of any package at any time and the total mileage traveled by all trucks. \n"
    "(The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)\n" \
    "D asks for the status and time of any package at any time, however I will add a menu option to view ALL package statuses at a specific time \n " \
    "I will also include the address, deadline, and weight of the package in the all status look up as per request. \n")
    print("************************************************")
    print("\nMenu:")
    print("1. Look up package status at a specific time")
    print("2. Look up all package statuses at a specific time")
    print("3. View total miles traveled by all trucks")
    print("4. Exit")
    print("\n")
    choice = input("Enter your choice: ")
    print("\n")
    print("************************************************")
    return choice

# Main loop for the CLI menu
def menu_loop(hash_table, trucks):
    while True:
        choice = menu()
        if choice == "1":
            lookup_package_status(hash_table)
        elif choice == "2":
            input_query_time = input("Enter time to check all package statuses (HH:MM AM/PM): ")
            print_all_statuses(hash_table, input_query_time)
        elif choice == "3":
            print(f"Total miles traveled by all trucks: {total_miles_traveled(trucks)}")
            print("Total miles for Truck 1:", round(truck1.truck_total_miles, 2))
            print("Total miles for Truck 2:", round(truck2.truck_total_miles, 2))
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Runs the delivery simulation
def run_delivery_simulation(hash_table, truck1, truck2):
    for bucket in hash_table.table:
        if bucket:
            for package in bucket:
                package.is_delayed()

    packages = available_packages(hash_table)

    truck1.load_truck(packages)
    truck2.load_truck(packages)

    route_truck(truck1)
    route_truck(truck2)

    truck1.return_to_hub()
    truck2.return_to_hub()

    packages = available_packages(hash_table)

    truck1.load_truck(packages)
    truck2.load_truck(packages)

    route_truck(truck1)
    route_truck(truck2)

# Used for Screenshots for D
def print_all_statuses(hash_table, query_time):
    query_time = datetime.datetime.strptime(query_time, "%I:%M %p")
    query_time = datetime.timedelta(hours=query_time.hour, minutes=query_time.minute)
    for bucket in hash_table.table:
        if bucket:
            for package in bucket:
                status = status_at_time(package, query_time)
                print(f"Package {package.id} | Truck: {package.loaded_truck} | Status: {status}")

if __name__ == "__main__":
    hash_table = load_packages("packagefile.csv")

    for pid in [13, 14, 15, 16, 19, 20]:
        p = hash_table.lookup(pid)
        p.get_deliver_with()
        print(pid, p.deliver_with, "|", p.notes)

    
    truck1 = truck.Truck(1)
    truck2 = truck.Truck(2)

    run_delivery_simulation(hash_table, truck1, truck2)

    """
    print("\nStatus at 8:35 AM")
    print_all_statuses(hash_table, "8:35 AM")

    print("\nStatus at 9:35 AM")
    print_all_statuses(hash_table, "9:35 AM")

    print("\nStatus at 12:03 PM")
    print_all_statuses(hash_table, "12:03 PM")
    """

    menu_loop(hash_table, trucks=[truck1, truck2])