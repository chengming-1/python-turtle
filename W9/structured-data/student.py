def student(a):
    print("The student's name is", a['name'])
    print("The student's major is", a['major'])
    print("His favorite food is", a['favorite_food'])
    print("His favorite color is", a['favorite_color'])
student1 = {
            'name': "Coonor Gunders",
            'major': "Media and Information",
            'favorite_food': "steak",
            'favorite_color': "blue"
        }
student2 = {
            'name': "Chengming Wang",
            'major': "Media and Information",
            'favorite_food': "noddles",
            'favorite_color': "blue"
        }
student(student1)
student(student2)




