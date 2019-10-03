checklist = []
maximum = []


# Перевод list из str в int
def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return str_list


# Запись всех рёбер в файл result.txt
with open('lineage1867_vertices1828_edges3206_shms.txt') as file:
    # with open('pr.txt') as file:
    file.readline()
    for line in file:
        f1, f2, f3, f4, f5, f6, f7, f8, f9 = line.split()
        # f4 = line.split()[3]
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
        # ouf.write(' [color = black, tooltip = "", penwidth = ""]')
        ouf.write('\n')
str_list_to_int_list(maximum)
maximum.sort()
# print(maximum)

with open('tree.dot', 'w') as ouf:
    for element in maximum:
        ouf.write(str(element))
        ouf.write(' [style = filled, fillcolor = "#506bda"]')
        ouf.write('\n')
    for i in range(len(checklist)):
        ouf.write(checklist[i][0])
        ouf.write(' -> ')
        ouf.write(checklist[i][1])
        ouf.write(' [color = black, tooltip = "", penwidth = ""]')
        ouf.write('\n')
# r = 0
# with open('result.txt') as file:
#     for line in file:
#         r = r + 1
# print(r)
#
# rd = 0
# with open('result_without_duplicates.txt') as file:
#     for line in file:
#         rd = rd + 1
# print(rd)