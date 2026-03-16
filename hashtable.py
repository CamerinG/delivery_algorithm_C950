class Hashtable:
    def __init__(self, capacity=40):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = len(self.table)

# Inserts a package into the hash table based on the package's ID and handles collisions using chaining
    def insert(self, package):
        bucket = hash(package.id) % self.size

    
        if self.table[bucket] is None:
            self.table[bucket] = [package]
        else:
            for p in self.table[bucket]:
                if p.id == package.id:
                    print(f"Package with ID {package.id} already exists in bucket {bucket}")
                    return
            self.table[bucket].append(package)

        #print(f"Inserting package with ID {package.id} into bucket {bucket}")
        
# To lookup package by ID
    def lookup(self, package_id):
        bucket = hash(package_id) % self.size
        if self.table[bucket] is not None:
            for p in self.table[bucket]:
                if p.id == package_id:
                    print(f"Package with ID {package_id} found in bucket {bucket}")
                    return p
        print(f"Package with ID {package_id} not found in bucket {bucket}")
        return None
# Removes package by ID
    def remove(self, package_id):
        bucket = hash(package_id) % self.size
        if self.table[bucket] is not None:
            for i, p in enumerate(self.table[bucket]):
                if p.id == package_id:
                    del self.table[bucket][i]
                    print(f"Package with ID {package_id} removed from bucket {bucket}")
                    return
        print(f"Package with ID {package_id} not found in bucket {bucket}")

