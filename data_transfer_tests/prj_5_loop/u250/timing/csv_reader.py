import csv

rows = []
rd_active = []
wr_active = []

with open("../hw_emu/summary.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)
#        if row[1] == "BUFFER_RD_ACTIVE_TIME_MS":
#            read_active.append(row[2])   

#print(rd_active)

for row in rows:
    if row != []:
        if row[0] == 'BUFFER_RD_ACTIVE_TIME_MS':
            rd_active.append(row[2])   

        elif row[0] == 'BUFFER_WR_ACTIVE_TIME_MS':
            wr_active.append(row[2])

print(rd_active)
print(wr_active)
