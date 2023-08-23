import sys

def gpa(s: list) -> str:
	students = {"Rno": [], "Fname": []};
	grades = {"Rno": [], "Grade": []};
	gpa = {
		"A": 10,
		"AB": 9,
		"B": 8,
		"BC": 7,
		"C": 6,
		"CD": 5,
		"D": 4
		};
	cgpa = {};
	c_tkn = {};
	c_idx = s.index("Courses");
	s_idx = s.index("Students")+1;
	g_idx = s.index("Grades");
	c = len(s[c_idx+1:s_idx-1]);
	for line in s[s_idx:g_idx]:
		students["Rno"].append(line.split("~")[0]);
		students["Fname"].append(line.split("~")[1]);
	for line in s[g_idx+1:len(s)-1]:
		grades["Rno"].append(line.split("~")[-2]);
		grades["Grade"].append(gpa[(line.split("~")[-1])]);
	students["Rno"], students["Fname"] = zip(*sorted(zip(students["Rno"], students["Fname"])))
	for x in students["Rno"]:
		cgpa[x] = 0;
		c_tkn[x] = 0;
	for x, y in zip(grades["Rno"], grades["Grade"]):
		cgpa[x] += y;
		c_tkn[x] += 1;
	for x in cgpa:
		if c_tkn[x] != 0:
			cgpa[x] = round(cgpa[x] / c_tkn[x], 2);

	for x, y in zip(students["Fname"], cgpa):
		print(y, x, cgpa[y], sep="~")


gpa(sys.stdin.read().splitlines());
