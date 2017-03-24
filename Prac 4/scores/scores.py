"""
CP1404/CP5632 Practical
CSV scores file program - broken one
scores file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")
    score_values = []
    scores_file.close()
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    print_line(subjects)
    for i in range(len(score_values)):
        print_line(score_values[i])


def print_line(line):
    for value in line:
        print('{:>6}'.format(value), end='')
    if isinstance(line[0], int):
        print("\t\tMax: {:2}\t\tMin: {:2}\t\tAverage: {:4}".format(max(line), min(line), sum(line)/len(line)))
    print()


main()
