# steps to cover to verify 'safe' reports
# something to check the sequence is only decreasing or increasing
# gaps between levels should be at least 1 and not be bigger than 3
# matching subsequent numbers not allowed


# is_increasing and is_decreasing functions are set up for the whole input document
# the 'check' functions allow me to pick and choose certain elements

def is_increasing(list):
    for i in range(1,len(list)):
        if not -3 <= list[i-1] - list[i] <= -1:
            return False
    return True

def is_decreasing(list):
    for i in range(1,len(list)):
        if not 1 <= list[i-1] - list[i] <= 3:
            return False
    return True

def check_inc(num):
        if -3 <= num <= -1:
            return True
        return False

def check_dec(num):
        if 1 <= num <= 3:
            return False
        return True

def check(check_func, list):
    for i in range(1, len(list)):
        if not check_func(list[i-1] - list[i]):
            return False


rows = []
# following file will be auto closed
with open ("2puzzle_input.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))
        rows.append(nums)

valid = 0
for r in rows:
    if check(check_inc, r):
        valid += 1
    elif check(check_dec, r):
        valid += 1

print(valid)


