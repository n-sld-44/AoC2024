# Part 1
leftList = []
rightList = []
with open('input.txt', "r") as file:
    data = file.readlines()
    for line in data:
        couple = line.split('  ')
        leftList.append(int(couple[0]))
        rightList.append(int(couple[1]))


def distanceBetweenLists(list1 : list, list2: list) -> int:
    sortedList1 = sorted(list1)
    sortedList2 = sorted(list2)
    distance = 0
    for i in range(len(sortedList1)):
        distance+= abs (sortedList1[i] - sortedList2[i])
    return distance

def part1():
    print(distanceBetweenLists(leftList,rightList))

# Part 2

def similarityScore(list1 : list, list2 : list) -> int:
    score = 0
    for num in list1:
        score += num * list2.count(num) 
    return score

def part2():
    print(similarityScore(leftList,rightList))

if __name__ == "__main__":
    part1()
    part2()