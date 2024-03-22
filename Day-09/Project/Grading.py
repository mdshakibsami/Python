student_number={
    "shakib":62,
    "samiya":95,
    "srabon":82,
    "alon":36,
}

student_grad={}
for student in student_number:
    num = student_number[student]
    if num>90:
        student_grad[student]="Outstanding"
    elif num>80:
        student_grad[student]="Very Good"
    elif num>60:
        student_grad[student]="Acceptable"
    else:
        student_grad[student]="Fail"


for key in student_grad:
    print(key,end="")
    print(f"={student_grad[key]}")