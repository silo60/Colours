#Tried to make this work but I think due to the indexing of Python in every combination the output was not completely correct!  Please let me know if there is an answer to this!!!

colors_list = ["blue", "blue", "green", "red", "brown", "purple", "pink", "white", "black", "grey", "yellow"]

num_1 = input("Please enter a number between 0 and 4: ")
num_2 = input("Please enter a number between 5 and 9: ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_1 <= num_2 <= len(colors_list):
        result = []
        for i in range(num_1, num_2+1):
            if i == 1:
                continue
            result.append(colors_list[i])
        print(result)
    else:
        print("Invalid input. Please try again.")
except ValueError:
    print("Invalid input. Please enter integers only.")

