import csv
class_list={}
for i in range(3):
	name = input()
	USN=input()
	class_list[name]=USN
print(class_list)
with open('pgm3.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    for name in class_list :
    	spamwriter.writerow([name,': ',class_list[name]])