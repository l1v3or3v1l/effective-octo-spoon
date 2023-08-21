def histogram(l: list) -> list:
	s = set();
	nl = [];
	for i in l:
		s.add(i);
	for x in s:
		c = 0;
		for i in l:
			if (x == i):
				c+=1;
		nl.append((x, c));
	for x in range(0, len(nl)-1):
		if (nl[x][1] > nl[x+1][1]):
			tmp = nl[x];
			nl[x] = nl[x+1];
			nl[x+1] = tmp;
	nl.sort(key=(lambda e: e[1]));
	return nl;



def transcript(coursedetails: list, studentdetails: list, grades: list) -> list:
	final = [];
	studentdetails.sort();
	for student in  studentdetails:
		rname = [student[0], student[1]];
		det = [(x[1],x[2]) for x in grades if x[0] == rname[0]];
		findet = []
		for x in coursedetails:
			for y in det:
				if x[0] == y[0]:
					findet.append((y[0], x[1], y[1]));
		final.append((student[0], student[1], findet));
	return final


#print(histogram([13,12,11,13,14,13,7,7,13,14,12]));
#print(histogram([7,12,11,13,7,11,13,14,12]));
#print(histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7]));

#print(transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2021001","Rohit Grewal"),("UGP2021132","Neha Talwar")],[("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")]));
#print(transcript([("T1","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Captain","Rohit Sharma"),("Batsman","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Batsman","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Batsman","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Batsman","T3","33"),("Captain","T3","95"),("No3","T3","51")]));