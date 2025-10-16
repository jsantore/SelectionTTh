import comp151Helpers

student_id = int(input("Enter student ID: "))
if student_id in comp151Helpers.graduation_list or \
    comp151Helpers.get_credits_from_database(student_id) >= 120:
    print("You can graduate!")