# Helen Li
# February 11, 2015
# Assignment #2: Problem #2: Grade Calculator

# ask user for name and course, the weight of tests and 3 scores, the weight of hw and 3 
# scores, provide averages and final grade

# ask for user's name and name of course
name = input("What is your name? ")
course = input("What class are you in? ")
print ()

# ask for weight of tests and 3 test scores
test_worth = float(input("How much are tests worth in this class (Enter as a decimal):"))
t1 = float(input("Enter test score #1:"))
t2 = float(input("Enter test score #2:"))
t3 = float(input("Enter test score #3:"))
print()

# calculate average, to 2 decimals
tAverage = float((t1+t2+t3)/3)
new_tAverage = format(tAverage, ".2f")

# print tests average for user to see
print ("Your test average is:", new_tAverage)
print()

# ask for weight of homework and 3 hw scores
hw_worth = float(input("How much are homework assignments worth in this class (Enter as a decimal):"))
h1 = float(input("Enter homework score #1:"))
h2 = float(input("Enter homework score #2:"))
h3 = float(input("Enter homework score #3:"))
print()

# calculate average, to 1 decimal place
hAverage = float((h1+h2+h3)/3)
new_hAverage = format(hAverage, ".1f")

# print hw average for user
print ("Your homework average is:", new_hAverage)
print()

# calculate final score
final_score = (test_worth*tAverage)+(hw_worth*hAverage)
new_final_score = format(final_score, ".2f")

# print final score
print ("Thanks, ", name, ". ", "Your final score in ", course, " is ", new_final_score, ".", sep="")
