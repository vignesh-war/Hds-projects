import csv
n=int(input())
event_list={}
for i in range(n):
	name=input()
	event=input()
	event_list(name)=event
print(event_list)
def add_participant():
	with open('events.csv','a',newline='')as csvfile:
	spamwriter=csv.writer(csvfile)
	for name1 in event_list :
		spamwriter.writerow([name1,': ',event_list[name1]])
def see_participant():
	 with open('events.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile)
      for row in spamreader:
          print(' '.join(row))