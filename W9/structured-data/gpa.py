
def gpa(a):
    total=0
    for grade in a["grades"]:
        print(grade)
        total += float(grade)
    print("The GPA for student is:", total/len(a['grades']))
student = {"grades":["3.1",
                   "4.0",
                   "3.2",
                   "3.6",
                   "2.9",
                   "1.2"
                   ]
        }
gpa(student)
