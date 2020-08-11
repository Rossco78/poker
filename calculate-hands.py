# count poker hands

pokerFile = open("poker-hands-csv", 'r') # 1. Open file for reading

# 2. create and initialize variables to hold the counts
totalCount = 0
nothingCount = 0
pairCount = 0
twoPairCount = 0
threeOfAKindCount = 0
straingCount = 0
flushCount = 0
fullHouse = 0
fourKindCount = 0
straightFlushCount = 0
royalFlushCount = 0

# 3. Loop through each of the file
for line in pokerFile:
    totalCount += 1 # each line increments the counter

    # get hand rank: split on comma's get last item as int
    handRank = int(line.split(',') [-1])
    
    #for each type of hand increment the appropriate counter
    if handRank == 0:
        nothingCount += 1
    if handRank == 1:
        pairCount += 1
    if handRank == 2:
        twoPairCount += 1
    if handRank == 3:
        threeOfAKindCount += 1
    if handRank == 4:
        straingCount += 1
    if handRank == 5:
        flushCount += 1
    if handRank == 6:
        fullHouse += 1
    if handRank == 7:
        fourKindCount += 1
    if handRank == 8:
        straightFlushCount += 1
    if handRank == 9:
        royalFlushCount += 1

print('total hands in file: ', totalCount)
print("Count of hands: ", nothingCount, pairCount, twoPairCount, threeOfAKindCount, 
straingCount, flushCount, fullHouse, fourKindCount, straightFlushCount, royalFlushCount)

totalCountFP = float(totalCount) # Float to force floating-point division
 

print("Probibility: ")
print("of nothing: ", (100 * nothingCount/totalCountFP), "%")
print("of one pair: ", (100 * pairCount/totalCountFP), "%")
print("of two pairs: ", (100 * twoPairCount/totalCountFP), "%")
print("of three of a kind: ", (100 * threeOfAKindCount/totalCountFP), "%")
print("of a straight: ", (100 * straingCount/totalCountFP), "%")
print("of a flush: ", (100 * flushCount/totalCountFP), "%")
print("of a full house: ", (100 * fullHouse/totalCountFP), "%")
print("of a four of a kind: ", (100 * fourKindCount/totalCountFP), "%")
print("of straight flush: ", (100 * straingCount/totalCountFP), "%")
print("of a royal flush: ", (100 * royalFlushCount/totalCountFP), "%")