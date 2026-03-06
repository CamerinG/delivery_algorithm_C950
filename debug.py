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
    p3 = package.Package(3, "233 Canyon Rd", "Salt Lake City", "UT", "84103", "EOD", "2", "None", "At Hub")

    p4 = package.Package(4, "380 W 2880 S", "Salt Lake City", "UT", "84115", "EOD", "4", "None", "At Hub")

    p5 = package.Package(5, "410 S State St", "Salt Lake City", "UT", "84111", "10:30 AM", "5", "None", "At Hub")

    p6 = package.Package(6, "3060 Lester St", "West Valley City", "UT", "84119", "EOD", "88", "None", "At Hub")

    p7 = package.Package(7, "1330 2100 S", "Salt Lake City", "UT", "84106", "EOD", "8", "None", "At Hub")

    p8 = package.Package(8, "300 State St", "Salt Lake City", "UT", "84103", "EOD", "9", "None", "At Hub")

    p9 = package.Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD", "2", "Must be delivered with 5, 8", "At Hub")

    p10 = package.Package(10, "600 E 900 South", "Salt Lake City", "UT", "84105", "EOD", "1", "Can only be on truck 2", "At Hub")

    p11 = package.Package(11, "2600 Taylorsville Blvd", "Taylorsville", "UT", "84118", "EOD", "1", "None", "At Hub")

    p12 = package.Package(12, "3575 W Valley Central Station Bus Loop", "West Valley City", "UT", "84119", "EOD", "1", "None", "At Hub")
    ht.insert(p1)
    ht.insert(p2)
    ht.insert(p3)
    ht.lookup(1)
    ht.lookup(2)
    ht.lookup(3)
    ht.remove(1)
    ht.lookup(1)
    print("\nTesting truck loading:")
    t = truck.Truck(1)

    packages = [p3, p9, p4, p5, p6, p7, p8, p10, p11, p12]

# make sure deliver_with gets parsed
    for p in packages:
        p.get_deliver_with()

    t.load_truck(packages)

    for p in t.packages:
        print(f"Loaded package {p.id}")

if __name__ == "__main__":
    main()