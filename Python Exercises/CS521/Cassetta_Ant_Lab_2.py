import csv
with open('Cassetta_Ant_lab_2.csv','w') as lab_write:
    file_writer = csv.writer(lab_write)
    for num in range(0,11):
        file_writer.writerow([num])
        num = num + num
lab_write.close()

with open('Cassetta_Ant_lab_2.csv','r', newline='') as lab_read:
    #lab_num = []
    lab_num = [int(item) for item in lab_read]

print(lab_num)

for index in lab_num:
    print(lab_num[index])
lab_read.close()
# I didn't know what format you wanted the print to be in