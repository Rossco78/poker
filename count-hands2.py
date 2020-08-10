# count poker hands

# 1. open poker data file for reading
pokerFile = open("poker-hands.py", 'rU')

totalCount = 0 # 2. create variable to hold the count -  initialize it.

# 3. step through each line of the file
for line in pokerFile:
    totalCount += 1   # (a) at each line increment the counter

    handRank = line.split(',') [-1] # (b) rank: split on comma, 
    handRank = int(handRank)        # get last item convet string input into integer

if handRank == 1:
    pairCount +=1

print("Total hands in file: ", totalCount)
print("Count of pair hands: ", pairCount)
