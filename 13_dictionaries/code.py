friends_ages = {"Rolf":24,"Adam":30,"Anne":27}

friends_ages["Rolf"] = 20

print(friends_ages)

friends = [
    {"name":"Rolf","age":24},
    {"name":"Adam","age":30},
    {"name":"Anne","age":27},
]

print(friends)
print(friends[1]["name"])

student_attendance = {"Rolf":96,"Bob":50,"Anne":100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")