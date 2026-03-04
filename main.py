import csv
import package
import truck
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
            address = row[1]
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


if __name__ == "__main__":
    hash_table = load_packages("packagefile.csv")

    # Test lookup
    test_package = hash_table.lookup(1)
    print(test_package.id, test_package.address, test_package.status)