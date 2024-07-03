score = input("Enter Score: ")
score_num = float(score)

if score_num > 1.0:
    print("Error - invalid score")

if score_num >= 0.9:
    print("A")
elif score_num >= 0.8:
    print("B")
elif score_num >= 0.7:
    print("C")
elif score_num >= 0.6:
    print("D")
else:
    print("F")
