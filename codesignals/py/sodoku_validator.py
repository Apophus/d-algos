# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn/description
import itertools
from collections import Counter


def solution(grid):
    # check for duplicates on rows
    def check_layout(layout):
        for row in layout:
            elements_count = Counter(row)
            filtered_nums = [elements_count[_] for _ in elements_count.keys() if _ != '.' and elements_count[_] > 1]
            if filtered_nums:
                return False
        return True

    # check for repeating numbers in columns
    columns = [[] for _ in range(9)]
    blocks = []
    # get columns
    for i in range(9):
        for j in range(9):
            columns[i].append(grid[j][i])

    # get blocks
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(grid[3 * r + i][3 * c + j])
            blocks.append(block)
    if not check_layout(grid) or not check_layout(columns) or not check_layout(blocks):
        return False

    return True


if __name__ == '__main__':
    grid = [[".", ".", ".", "1", "4", ".", ".", "2", "."],
            [".", ".", "6", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "1", ".", ".", ".", ".", ".", "."],
            [".", "6", "7", ".", ".", ".", ".", ".", "9"],
            [".", ".", ".", ".", ".", ".", "8", "1", "."],
            [".", "3", ".", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", "7", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", "7", "."]]
    print(solution(grid))  # true

