#2
open_file = open("CupcakeInvoices.csv")

#3
for line in open_file:
    print(line)

#4
for line in open_file:
    values = line.split(',')
    print(values[2])

#5
for line in open_file:
    values = line.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

#6
total_all = 0

for line in open_file:
    values = line.split(',')
    total = (int(values[3]) * float(values[4]))
    total_all += total

print(total_all)

#7
open_file.close()

