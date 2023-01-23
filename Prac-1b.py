print("Prac 1b - Find S")
print("Name - Pritesh Tayade - Roll No 15")
print("------------------------------------------------------")
import csv

num_attributes = 6
dataset = []
with open(r"C:\Workspace\un-org\MScIT\Part-II-2022-23\Sem-3\Machine-Learning\practical\Pritesh\MLPracsProject\Data-Files\data_find_s_1b.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataset.append(row)

# print(row)
# print(dataset)
print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = dataset[1][j]
    print("\n Find S: Finding a Maximally Specific Hypothesis \n:")
    for i in range(1, len(dataset)):
        if dataset[i][num_attributes] == 'Yes':
            for j in range(0, num_attributes):
                if dataset[i][j] != hypothesis[j]:
                    hypothesis[j] = '?'
                else:
                    hypothesis[j] = dataset[i][j]
        print("For Training instance no:{0} the hypothesis is ".format(i), hypothesis)
    print("\n The Maximally Specific Hypothesis for a given training examples: \n")
    print(hypothesis)

