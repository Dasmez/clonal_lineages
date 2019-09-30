checklist = []
with open('lineage1867_vertices1828_edges3206_shms.txt') as file:
#with open('pr.txt') as file:
    file.readline()
    for line in file:
        f4 = line.split()[3]
        edges = f4.split(",")
        for i in range(len(edges)):
            number = edges[i].split("-")
            if number not in checklist:
                checklist.append(number)
with open('result.txt', 'w') as ouf:
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
