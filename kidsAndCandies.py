# You have gathered N bags of candy and you want to distribute the candy amongst M kids. The i-th bag contains Ci pieces of candy. You want to make sure that every kid get the same amount of candy and that the number of pieces of candy they receive is the greatest  possible. You can open each bag and mix all pieces of candy before distributing them to the kids. How many pieces of candy will remain after you share the candy amongst kids, based on the rules described above?

# For a solution here, we have to find the total
#number of candys and divide it with no residue
#with open("D:\\Mis cosas\\Descargas\\test_data\\sample_test_set_1\\sample_ts1_input.txt","r")
testCases = int(input()) #The first number is the number of test cases
numTestCase = 0
res = dict() #store the results
while numTestCase < testCases :
    #loads the data into the program
    numberCandyBags = list(map(int, input().strip().split()))#[:testCases]
    numberCandies = list(map(int, input().strip().split()))#[:numberCandyBags(1)]
    #finds the total number of candies
    totalCandies = sum(numberCandies)
    totalBags = totalCandies / numberCandyBags[1]
    #finds the remaining candies 
    remainCandy = totalCandies % numberCandyBags[1]
    numTestCase = numTestCase + 1
    res[numTestCase] = remainCandy

#print(res)

for i in res:
    print("Case #",i,":",res[i])
