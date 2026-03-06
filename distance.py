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

    address_a = address_a.strip().lower()
    address_b = address_b.strip().lower()

    with open('distancetable.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        index_a = None
        index_b = None

        for i in range(len(rows)):
            cell = (rows[i][0] + " " + rows[i][1]).strip().lower()
            if address_a in cell:
                index_a = i
            if address_b in cell:
                index_b = i

        if index_a is not None and index_b is not None:
            distance = rows[index_a][index_b + 1]
            if distance == "":
                distance = rows[index_b][index_a + 1]
            return distance
        else:
            raise ValueError("One or both addresses not found in distance table.")
