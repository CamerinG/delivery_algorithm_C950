import csv



"""
with open('distancetable.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

    for i in range(len(rows)):
        if "1060 Dalton Ave S" in rows[i][0]:
            print(i)
            """


def get_distance(address_a, address_b):
    with open('distancetable.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        index_a = None
        index_b = None

        for i in range(len(rows)):
            if address_a in rows[i][0]:
                index_a = i
            if address_b in rows[i][0]:
                index_b = i

        if index_a is not None and index_b is not None:
            distance = rows[index_a][index_b]
            if distance == "":
                distance = rows[index_b][index_a]
            return distance
        else:
            raise ValueError("One or both addresses not found in distance table.")
        

print(get_distance("177 W Price Ave", "1060 Dalton Ave S"))