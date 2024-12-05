

def checkIndex(i : int, input : str) -> int:
    if input[i:i+4] == "mul(":
            right =''
            left = ''
            delta = i+4
            while input[delta].isnumeric():
                right+= input[delta]
                delta +=1
            if input[delta] == ',':
                delta+=1
                while input[delta].isnumeric():
                    left+= input[delta]
                    delta +=1
                    if input[delta] == ')':
                        return int(right)*int(left)
                
            
    return 0

def sumLine(input):
    sum = 0
    for i in range(len(input)-4):
                sum += checkIndex(i,input)
    return sum
def part1() -> int:
    sum = 0
    with open("input.txt", 'r') as file:
        data = file.readlines()
        for line in data:
            sum +=    sumLine(line)   
        
    return sum



def checkEnable(i : int, string : str, enabled : bool ) -> bool:
    if string[i:i+len("don't()")] == "don't()":
        return False
    if string[i:i+len("do()")] == "do()":
        return True
    else:
        return enabled
    
     
def inp():
    string = ''
    with open("input.txt", 'r') as file:
        data = file.readlines()
        for line in data:
            string+= line
    return string

def part2(string):
    enabled = True
    sum = 0
    for i in range(len(string)):
        if enabled:
            enabled = checkEnable(i, string,enabled)
            sum += checkIndex(i,string)
        else :
            enabled = checkEnable(i,string,enabled)
    return sum  
         
         


def main():
    assert(checkIndex(0,'mul(2,3)')==6)
    assert(sumLine("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)") == 161)
    print(part1())
    assert(part2("""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)""") == 48)
    string = inp()
    print(part2(string))
if __name__ == "__main__":
    main()