import datetime

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.deliver_time = None
        self.deliver_with = []
        self.truck_assigned = None
        self.delayed = None
        self.en_route_time = None
        self.loaded_truck = None

# Checks if package is already assigned to a truck
    def is_truckassigned(self):
        if self.truck_assigned is None:
            return False
        return True
# Parses the notes field to determine if the package can only be on a specific truck and assigns it to that truck if applicable.
    def assign_truck(self):
        if "Can only be on truck" in self.notes:
            self.truck_assigned = [int(s) for s in self.notes.split() if s.isdigit()][0]
            return self.truck_assigned
        else:
            return None
# Checks if the package is delayed and parses the notes field to determine the delay time
    def is_delayed(self):
        if "Delayed on flight" in self.notes:
            delayed_time = datetime.datetime.strptime(self.notes.split("until ")[1], "%I:%M %p")
            self.delayed = datetime.timedelta(hours=delayed_time.hour, minutes=delayed_time.minute)
            return self.delayed
        else:
            return None
# Checks if the package has a delivery deadline and parses the deadline time from the notes field
    def get_deadline(self):
        if self.deadline == "EOD":
            return None
        else:
            return datetime.strptime(self.deadline, "%I:%M %p").time()
#Checks if the package must be delivered with other packages
    def get_deliver_with(self):
        if "Must be delivered with" in self.notes:
            self.deliver_with = [int(s) for s in self.notes.split("Must be delivered with ")[1].split(",") if s.strip().isdigit()]
            self.deliver_with.append(self.id)
            return self.deliver_with
        else:
            return None