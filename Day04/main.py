


def part1(matrix : list) -> int:
    # Vertical
    count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)-3):
            box = matrix[row][col]+matrix[row+1][col]+matrix[row+2][col]+matrix[row+3][col]
            
            if box =="XMAS" or box == "SAMX":
                
                count += 1


    # Horizontal
    for col in range(len(matrix[0])-3):
        for row in range(len(matrix)):
            box = matrix[row][col]+matrix[row][col+1]+matrix[row][col+2]+matrix[row][col+3]
            
            if box =="XMAS" or box == "SAMX":
              
                count += 1
    # Diagonal
    for col in range(len(matrix[0])-3):
        for row in range(len(matrix)-3):
            box = matrix[row][col]+matrix[row+1][col+1]+matrix[row+2][col+2]+matrix[row+3][col+3]
            if box =="XMAS" or box == "SAMX":
                count += 1

    for col in range(len(matrix[0])-1,2,-1):
        for row in range(len(matrix)-3):

            box = matrix[row][col]+matrix[row+1][col-1]+matrix[row+2][col-2]+matrix[row+3][col-3]
            if box =="XMAS" or box == "SAMX":
                count += 1

    return count

def part2(matrix : list) -> int :
    count = 0
    for col in range(len(matrix[0])-2):
        for row in range(len(matrix)-2):
            diag1 = matrix[row][col]+matrix[row+1][col+1]+matrix[row+2][col+2]
            diag2 = matrix[row][col+2]+matrix[row+1][col+1]+matrix[row+2][col]
            if (diag1 =="MAS" or diag1 == "SAM") and ( diag2== "SAM" or diag2 == "MAS"):
                count += 1
    return count

def main():
    data = []
    with open('input.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            data.append(line)


    assert part2(
[
"MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"]) == 9

    print(part2(data))

if __name__ == '__main__':
    main()