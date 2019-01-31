import csv
n=int(input())
for i in range(n):
	name = input()
	event = input()
	event_list[name]=event
print(event_list)
with open('pgm5.csv','a',newline='')as csvfile:
	spamwriter=csv.writer(csvfile,delimiter=' ')
	for name1 in event_list :
		spamwriter.writerow([name1,': ',event_list[name1]])