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


"""
Alternatively: use a set to check for uniqueness
"""


def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue

        if num in s:
            return False
        s.add(num)
    return True


def solution(grid):
    for line in grid:
        if not check_unique(line):
            return False

    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]):
                return False

    return True