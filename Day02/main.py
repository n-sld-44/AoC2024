def inputSan():
    inp = []
    with open('input.txt','r') as file:
        data = file.readlines()
        
        for line in data:
            level = line.split(' ')
            level = [int(i) for i in level]
            inp.append(level)          
                

    return inp

def part1(listOfLevel):
    safeCount = 0
    for level in listOfLevel:
        if isSafePart1(level):
            safeCount+=1
    return safeCount


def part2(listOflevels):
    safeCount = 0
    for level in listOflevels:
        if isSafePart2(level):
            safeCount+= 1
    return safeCount



def isSafePart1(level : list) -> bool:
    
    if sorted(level, reverse=True) == level or sorted(level, reverse=False)==level:
            for i in range(1,len(level)):
                if not (abs(level[i]-level[i-1])>0 and abs(level[i]-level[i-1])<4): 
                    break
                if i == len(level)-1:
                    return True
        
    return False


def isSafePart2(level : list) -> bool:
    
    for i in range(len(level)):
        copyLevel = [item for x,item in enumerate(level) if x != i  ]
        if sorted(copyLevel, reverse=True) == copyLevel or sorted(copyLevel, reverse=False)==copyLevel:
                for i in range(1,len(level)):
                    if not (abs(copyLevel[i]-copyLevel[i-1])>0 and abs(copyLevel[i]-copyLevel[i-1])<4): 
                        break
                    if i == len(copyLevel)-1:
                        return True
        
    return False




def main():
    levels = inputSan()
    print(part1(levels))
    print(part2(levels))

if __name__=="__main__":
    main()