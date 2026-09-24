def compile_result(student, marks_list):
    total = sum(marks_list)
    average = round(total / len(marks_list), 2)
    return {"roll_no": student.roll_no, "total": total, "average": average}
