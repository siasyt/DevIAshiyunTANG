def check_salute(couloir):
    if not isinstance(couloir, str):
        return 0
    
    salutations = 0
    left_officers = []
    right_officers = []

    for i, direction in enumerate(couloir):
        if direction not in ['-', '>', '<']:
            return 0
        if direction == '>':
            right_officers.append(i)
        elif direction == '<':
            left_officers.append(i)
            salutations += len(right_officers)

    return salutations

print(check_salute("->-------------<-------"))
print(check_salute("-<------------->-------"))
print(check_salute("-->>----<<--"))
print(check_salute("--->--->----->--"))
print(check_salute("---<---->-->----<<-->"))





