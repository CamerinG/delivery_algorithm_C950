import package
import distance
import datetime
import csv



class Truck:
    def __init__(self, id):
        self.id = id
        self.current_location = "4001 South 700 East"
        self.previous_location = None
        self.packages = []
        self.capacity = 16
        self.package_count = 0
        self.speed = 18
        self.elapsed_time = 0
        self.start_time = datetime.timedelta(hours=8)
        self.truck_total_miles = 0.0
    
# Loads the truck with eligible packages until the truck reaches its capacity
    def load_truck(self, packages_on_truck):
        for package in packages_on_truck:
            if self.package_count >= self.capacity:
                break
            if self.is_eligible_package(package):
                if package.truck_assigned and self.id != package.truck_assigned:
                    continue
                if package.deliver_with:
                    self.add_package(package)
                    for p in packages_on_truck:
                        if p.id in package.deliver_with and p not in self.packages:
                            self.add_package(p)
                else:
                    self.add_package(package)

# Checks if a package is eligible to be loaded onto the truck based on its status, assigned truck, and delay time
    def is_eligible_package(self, package):
        current_time = self.start_time + datetime.timedelta(minutes=self.elapsed_time)
        package.assign_truck()
        package.is_delayed()
        if package.status == "Delivered":
            return False
        if package in self.packages:
            return False
        if package.truck_assigned != None and package.truck_assigned != self.id:
            return False
        if package.delayed is not None and current_time < package.delayed:
            return False
        return True
# Adds a package to the truck and updates the package's status 
    def add_package(self, package):
        if self.package_count < self.capacity:
            self.packages.append(package)
            self.package_count += 1
            package.loaded_truck = self.id
            package.en_route_time = self.start_time + datetime.timedelta(minutes=self.elapsed_time)
            package.status = "En Route"
        else:
            print(f"Truck {self.id} is at full capacity. Cannot add package {package.id}.")
#Removes package from the truck and updates the package count and status
    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)
            self.package_count -= 1
# Delivers the package by calculating the distance from the truck's current location to the package's delivery address, updating the truck's total miles and elapsed time, and updating the package's status and delivery time
    def delivery(self, package):
        miles = distance.get_distance(self.current_location, package.address)
        float_miles = float(miles)
        self.truck_total_miles += float_miles
        minutes = (float_miles / self.speed) * 60
        self.elapsed_time += minutes
        self.remove_package(package)
        package.status = "Delivered"
        package.deliver_time = self.start_time + datetime.timedelta(minutes=self.elapsed_time)
        #print(f"Truck {self.id} delivered package {package.id} to {package.address}. Total miles: {self.truck_total_miles:.2f}, Time: {package.deliver_time}")
# Returns truck to hub after finishing first delivery route
    def return_to_hub(self):
        miles = distance.get_distance(self.current_location, "4001 South 700 East")
        float_miles = float(miles)
        self.truck_total_miles += float_miles
        minutes = (float_miles / self.speed) * 60
        self.elapsed_time += minutes
        self.current_location = "4001 South 700 East"
        #print(f"Truck {self.id} returning to hub. Total miles: {self.truck_total_miles}")