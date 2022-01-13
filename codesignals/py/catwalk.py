def solution(code):
    stripped = code.strip()
    s_list = stripped.split()

    return ' '.join(s_list)


code = "      for      i      in         ra   nge(x,   29):"

print(solution(code))