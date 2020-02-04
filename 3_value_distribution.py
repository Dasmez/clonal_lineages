from graphviz import Digraph

checklist = []
maximum = []
table = []
amino_acids = []


def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return str_list


names = ['S', 'A', 'C', 'D', 'K', 'F', 'G', 'Q', 'H', 'I', 'M', 'N', 'P', 'T', 'V', 'W', 'E', 'Y', '*', 'L', 'R']

hydrophobicity = {"R": -4.5, "K": -3.9, "E": -3.5, "N": -3.5, "Q": -3.5, "D": -3.5, "H": -3.2, "P": -1.6, "Y": -1.3,
                  "W": -0.9, "S": -0.8,
                  "T": -0.7, "G": -0.4, "A": 1.8, "M": 1.9, "C": 2.5, "F": 2.8, "L": 3.8, "V": 4.2, "I": 4.5, "*": 5}

values = [-4.5, -3.9, -3.5, -3.2, -1.6, -1.3, -0.9, -0.8, -0.7, -0.4, 1.8, 1.9, 2.5, 2.8, 3.8, 4.2, 4.5, 5]

isoelectricity = {"A": 6.11, "R": 10.76, "N": 5.41, "D": 2.87, "C": 5.02, "Q": 6.65, "E": 3.08, "G": 6.06, "H": 7.64,
                  "I": 6.04, "L": 6.04, "K": 9.47, "M": 5.74, "F": 5.91, "P": 6.30, "S": 5.68, "T": 5.60, "W": 5.88,
                  "Y": 5.63, "V": 6.02, "*": 5}

values_i = [2.87, 3.08, 5, 5.02, 5.41, 5.60, 5.63, 5.68, 5.74, 5.88, 5.91, 6.02, 6.04, 6.06, 6.11, 6.30, 6.65, 7.64,
            9.47, 10.76]

with open('lineage1867_vertices1828_edges3206_shms.txt') as file:
    file.readline()
    for line in file:
        f1, f2, f3, f4, f5, f6, f7, f8, f9 = line.split()
        edges = f4.split(",")
        for i in range(len(edges)):
            number = edges[i].split("-")
            if number not in checklist:
                checklist.append(number)
with open('result.txt', 'w') as ouf:
    for i in range(len(checklist)):
        if checklist[i][0] not in maximum:
            maximum.append(checklist[i][0])
        if checklist[i][1] not in maximum:
            maximum.append(checklist[i][1])
        ouf.write(checklist[i][0])
        ouf.write(' -> ')
        ouf.write(checklist[i][1])
        ouf.write('\n')
str_list_to_int_list(maximum)
maximum.sort()

with open('lineage1867_vertices1828_edges3206_seqs.txt') as file:
    file.readline()
    for line in file:
        parts = line.split()
        f1 = parts[0]
        f2 = parts[1]
        amino_acids.append(int(f1))
        amino_acids.append(f2)
        table.append(amino_acids)
        amino_acids = []

thr85 = [75]

# with open('value_distr2.txt', 'w') as ouf:
with open('isoel.txt', 'w') as ouf:
    for a_a in range(123):
        b = []
        for element in maximum:
            for acid in table:
                if element == acid[0]:
                    if acid[1][a_a] not in b:
                        # print(acid[1][a_a])
                        b.append(acid[1][a_a])
                    if str(a_a) == '57':
                        ouf.write(str(a_a))
                        ouf.write('\t')
                        ouf.write(str(element))
                        ouf.write('\t')
                        ouf.write(str(acid[1][a_a]))
                        ouf.write('\t')
                        ouf.write(str(hydrophobicity[acid[1][a_a]]))
                        ouf.write('\n')
