file = "d1_input.txt"
with open(file) as f:
    data = f.readlines()

elves = []
calories_temp = 0
for _ in data:
    new = _.strip()  #get rid of the newlines, this will leave the newline separating each elve as an empty space
    if new == '':
        elves.append(calories_temp)  #if this separation is met, store the sum of calories so far in a list
        calories_temp = 0 #then reset the calories to 0
    else:
        calories_temp += int(new)  #otherwise, add the number of calories to the temporary counter

# part 1 - find the elf carrying the most calories
print(max(elves))

# for part 2 we need the sum of the top 3 elves
#easiest way is to reverse sort the list (aka sort in descending order) then sum up the first 3 values.
elves.sort(reverse= True)
print(sum(elves[0:3]))




