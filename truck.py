import package
import distance
import datetime
import csv


class Truck:
    def __init__(self, id):
        self.id = id
        self.current_location = "Hub"
        self.previous_location = None
        self.packages = []
        self.capacity = 16
        self.package_count = 0
        self.speed = 18
        self.time = 0
        self.truck_total_miles = 0.0

    

    def load_truck(self, packages_on_truck):
        for package in packages_on_truck:
            if self.is_eligible_package(package):
                if package.deliver_with not in self.packages:
                    continue
                elif package.truck_assigned and self.id != package.truck_assigned:
                    continue
                self.add_package(package)
            

    def load_truck(self, packages_on_truck):
        for package in packages_on_truck:
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






    """
    FROM PSEUDOCODE::::
    Def loadTruck():
	Truck.packagesontruck = []
	For packages_on_truck
		If EligiblePackage	
			If package.deliver_with == packagesontruck
				truck.packagesontruck.append(package)
			If truck.id == package.notes.truck_assigned.id
				truck.packagesontruck.append(package)
		Package.status = EnRoute
		If length(truck.packagesontruck) == TruckCapacity
			Break
    """

    def is_eligible_package(self, package):
        package.assign_truck()
        if package.status == "Delivered":
            return False
        if package in self.packages:
            return False
        if package.truck_assigned != None and package.truck_assigned != self.id:
            return False
      #  if package.delayed != None and time < package.delayed:
      #      return False
        return True

    def add_package(self, package):
        if self.package_count < self.capacity:
            self.packages.append(package)
            self.package_count += 1
            package.status = "En Route"
        else:
            print(f"Truck {self.id} is at full capacity. Cannot add package {package.id}.")

    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)
            self.package_count -= 1

    def delivery(self, package):
        miles = distance.get_distance(self.current_location, package.address)
        float_miles = float(miles)
        self.truck_total_miles += float_miles
        minutes = (float_miles / self.speed) * 60
        self.time += minutes
        self.remove_package(package)
        package.status = "Delivered"
        package.deliver_time = datetime.timedelta(minutes=self.time)