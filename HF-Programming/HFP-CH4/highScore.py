highest_score = 0
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    if float(score) > highest_score:
        highest_score = float(score)
result_f.close()
print("The Highest score was: ")
print(highest_score)