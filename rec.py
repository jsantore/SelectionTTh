
line_number = 1
with open ("sillyRec.txt", 'r') as rec_file:
    lines = rec_file.readlines()
    for line in lines:
        if line_number%2 == 1:
            print(line.strip())
        line_number += 1