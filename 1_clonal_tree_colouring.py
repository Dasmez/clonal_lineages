from graphviz import Digraph

import matplotlib as mplt
import matplotlib.pyplot as plt

checklist = []
maximum = []

names = ['S', 'A', 'C', 'D', 'K', 'F', 'G', 'Q', 'H', 'I', 'M', 'N', 'P', 'T', 'V', 'W', 'E', 'Y', '*', 'L', 'R']

def norm_value(acid, pos):
    for i in range(len(names)):
        if acid[1][pos] == names[i]:
            return i / 21

def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return str_list

def GetColorByNormalizedValue(cmap_name, norm_value):
    if norm_value < 0 or norm_value > 1:
        print("ERROR: value " + str(norm_value) + ' does not belong to [0, 1]')
    cmap = plt.cm.get_cmap(cmap_name)
    color = cmap(norm_value)
    return mplt.colors.rgb2hex(color[:3])

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

amino_acids = []
table = []
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

for a_a in thr85:
    for element in maximum:
        for acid in table:
            if element == acid[0]:
                norm_value_def = norm_value(acid, a_a)
                color_code = str(GetColorByNormalizedValue('gist_rainbow', norm_value_def))
                dot.node(str(element), acid[1][a_a], style='filled', color=color_code)
                break
    for i in range(len(checklist)):
        dot.edge(checklist[i][0], checklist[i][1])
    dot.render(str(a_a), view=True)
    dot.save(str(a_a))
    dot.clear()
