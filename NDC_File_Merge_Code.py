import csv


all_values1 = []
all_values2 = []
output_data = []


with open('/uploads/package.txt', 'r') as file:
    for line in file:
        all_values1.append(line.strip())

with open('/uploads/product.txt', 'r') as file:
    for line in file:
        all_values2.append(line.strip())

for line1 in all_values1:
    columns1 = line1.split("\t")
    for line2 in all_values2:
        columns2 = line2.split("\t")
        if columns1[0] == columns2[0]:
            output_data.append(columns1[0:4] + columns2[2:4] + columns2[5:8] + columns2[13:17])
            print(columns1[0:4] + columns2[2:4] + columns2[5:8] + columns2[13:17])
            
with open('/myfiles/ndc_merged_data.txt', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t') 
    writer.writerows(output_data)  


            


      



