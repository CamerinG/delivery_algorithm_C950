import distance
import datetime
import hashtable
import package
import truck

def main():
    print("Testing distance function:")
    print(distance.get_distance("177 W Price Ave", "1060 Dalton Ave S"))
    print("\nTesting hashtable:")
    ht = hashtable.Hashtable()
    p1 = package.Package(1, "177 W Price Ave", "Salt Lake City", "UT", "84115", "EOD", "37", "None", "status")
    p2 = package.Package(2, "1060 Dalton Ave S", "Salt Lake City", "UT", "84104", "EOD", "5","None", "status")
    ht.insert(p1)
    ht.insert(p2)
    ht.lookup(1)
    ht.lookup(2)
    ht.remove(1)
    ht.lookup(1)
    print("\nTesting truck loading:")
    t = truck.Truck(1)
    t.load_truck([p1, p2])
    for p in t.packages:
        print(f"Package ID {p.id} loaded on truck {t.id}")

if __name__ == "__main__":
    main()