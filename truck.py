from package import Package

class Truck:
    def __init__(self, id):
        self.id = id
        self.current_location = "Hub"
        self.previous_location = None
        self.packages = []
        self.capacity = 16
    

    def load_truck(self, packages_on_truck):
        self.packages = []
        for package in packages_on_truck:
            if self.is_eligible_package(package):
                if package.deliver_with in self.packages:
                    self.packages.append(package)
                elif self.id == package.notes.truckonly.id:
                    self.packages.append(package)
            package.status = "En Route"
            if len(self.packages) == self.capacity:
                break


"""
    FROM PSEUDOCODE::::
    Def loadTruck():
	Truck.packagesontruck = []
	For packages_on_truck
		If EligiblePackage	
			If package.deliver_with == packagesontruck
				truck.packagesontruck.append(package)
			If truck.id == package.notes.truckonly.id
				truck.packagesontruck.append(package)
		Package.status = EnRoute
		If length(truck.packagesontruck) == TruckCapacity
			Break
"""