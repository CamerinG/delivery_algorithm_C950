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


    def is_truckassigned(self):
        if self.truck_assigned is None:
            return False
        return True
    
    def assign_truck(self):
        if "Can only be on truck" in self.notes:
            self.truck_assigned = [int(s) for s in self.notes.split() if s.isdigit()][0]
            return self.truck_assigned
        else:
            return None
        
    def is_delayed(self):
        if "Delayed on flight" in self.notes:
            self.delayed = datetime.strptime(self.notes.split("Delayed on flight ")[1], "%I:%M %p").time()
            return self.delayed
        else:
            return None
        
    def get_deadline(self):
        if self.deadline == "EOD":
            return None
        else:
            return datetime.strptime(self.deadline, "%I:%M %p").time()

    def get_deliver_with(self):
        if "Must be delivered with" in self.notes:
            self.deliver_with = [int(s) for s in self.notes.split("Must be delivered with ")[1].split(",") if s.strip().isdigit()]
            self.deliver_with.append(self.id)
            return self.deliver_with
        else:
            return None