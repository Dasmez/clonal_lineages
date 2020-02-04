with open('lineage1557_vertices73_edges86_seqs.txt') as file:
    with open('result_fasta.txt', 'w') as ouf:
        file.readline()
        for line in file:
            parts = line.split()
            f1 = parts[0]
            f2 = parts[1]
            ouf.write('>')
            ouf.write(f1)
            ouf.write('\n')
            ouf.write(f2)
            ouf.write('\n')
amino_acids = []
table = []
with open('result_fasta.txt') as file:
    file.readline()
    for line in file:
        amino_acids.append(line)
        table.append(amino_acids)
        amino_acids = []
        file.readline()
d = len(table)
acids = []
counter = []
list_of_acid = []

for j in range(124):
    for i in range(d):
        seq = table[i]
        acid = seq[0][j]
        acids.append(acid)
    listik = []

    for el in acids:
        s = 0
        if el not in counter:
            counter.append(el)
            count = acids.count(el)
            tup = (round(count * 100 / 73, 2), el)
            listik.append(tup)
    list_of_acid.append(listik)
    acids = []
    counter = []

posions_trh = []
pos = 0
for el in list_of_acid:
    # if len(el) > 1:
    el = sorted(el)
    el = list(reversed(el))
    if el[0][0] < 100:
        posions_trh.append(pos)
    pos += 1


# threshold <100
# [15, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 117, 119]

# threshold <95
# [22, 27, 29, 30, 34, 49, 50, 51, 53, 55, 56, 57, 58, 60, 61, 63, 64, 69, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 87, 88, 92, 94, 99, 107, 108, 110, 112, 114, 117]

# threshold <90
# [22, 27, 30, 34, 49, 51, 53, 55, 56, 57, 58, 60, 61, 64, 75, 76, 77, 79, 83, 84, 87, 94, 108, 110, 114, 117]

# threshold <85
# thr85 = [22, 27, 34, 51, 53, 55, 56, 57, 58, 60, 75, 76, 79, 87, 108, 110, 114, 117]

hydrophobicity = {"F": 2.8, "V": 4.2, "L": 3.8, "W": -0.9, "M": 1.9, "A": 1.8, "G": -0.4, "C": 2.5, "Y": -1.3,
                  "P": -1.6, "T": -0.7,
                  "S": -0.8, "H": -3.2, "E": -3.5, "N": -3.5, "Q": -3.5, "D": -3.5, "K": -3.9, "R": -4.5, "I": 4.5, "*": 5}


pos2 = 1
for el in list_of_acid:
    el = sorted(el)
    el = list(reversed(el))
    #print(el)
    for i in range(len(el)):
        #print(pos2, el[i][0], el[i][1], i, hydrophobicity[el[i][1]], sep='\t')
        print(pos2, el[i][0], el[i][1], sep='\t')
        posions_trh.append(pos)
    pos2 += 1
# print("\n")
# print(el, count)
# print(posions_trh)


#                 a = hydrophobicity[acid[i]]
#                 if a not in value_all:
#                     value_all.append(a)
#                 if int(name[1:-1]) in position:
#                     if a not in value_terminal:
#                         value_terminal.append(a)
# print(thr85)
# print(sorted(value_all))
# print(sorted(value_terminal))
