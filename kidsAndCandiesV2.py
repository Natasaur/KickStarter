#import readline


with open("D:\\Mis cosas\\Descargas\\test_data\\sample_test_set_1\\sample_ts1_input.txt","r") as file:
    testCases = int(file.readline()) #The first number is the number of test cases
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
