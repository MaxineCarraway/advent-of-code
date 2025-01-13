# steps to cover to verify 'safe' reports
# something to check the sequence is only decreasing or increasing
# gaps between levels should be at least 1 and not be bigger than 3
# matching subsequent numbers not allowed


# is_increasing and is_decreasing functions are set up for the whole input document
# the 'check' functions allow me to pick and choose certain elements
import os
print(os.getcwd())

def is_increasing(sequence):
    for i in range(1,len(sequence)):
        if not -3 <= sequence[i-1] - sequence[i] <= -1:
            return False
    return True

def is_decreasing(sequence):
    for i in range(1,len(sequence)):
        if not 1 <= sequence[i-1] - sequence[i] <= 3:
            return False
    return True

def check_inc(num):
        if -3 <= num <= -1:
            return True
        return False

def check_dec(num):
        if 1 <= num <= 3:
            return True
        return False

def check(check_func, sequence):
    for i in range(1, len(sequence)):
        if not check_func(sequence[i-1] - sequence[i]):
            return False
    return True

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
    else:
        for i in range(len(r)):
            removed = r.pop(i)

            if check(check_inc, r):
                valid += 1
                r.insert(i, removed)
                break
            elif check(check_dec, r):
                valid += 1
                r.insert(i, removed)
                break

# I originally only had the below line and this duplicated some of the checks, the youtuber I was watching pointed out there was no break out of the loop and the numbers had not been inserted back into the list
            r.insert(i, removed)

print(valid)

# YT did advise too many for loops in this. A more efficient way would be to add a tolerace to the initial "check" setting that at 0 for the first iteration. then (if not) check each time for tolerances == 1 (returning false) == - 1 (returning true) next check is i+1 and i+=2 (tolerance +=1) and next, if i - 2 < 0 checking for i += 1 (tolerance +=1)   -   lastly looking at if the above does nothing then we need to check i-1 and i+1 to see if it meets the conditions (returning false) remembering the tolerance of +=1

# def check(check_func, sequence):
#     tolerance = 0

# #   checking for: i-1, i-1, i, i+1
#     i = 1
#     while i < len(list):
#         if not check_func(sequence[i-1] - sequence[i]):
#             if tolerance == 1:
#                 return False

#             if i == len(sequence) -1:
#                 return True

#             if check_func(sequence[i-1] - sequence[i+1]):
#                 i += 2
#                 tolerance += 1
#                 continue

#             if not check_func(sequence[i-2] - sequence[i]) and not check_func(sequence[i-1] - sequence[i+1]):
#                 return False

# rows = []
# # following file will be auto closed
# with open ("2puzzle_input.txt") as f:
#     for line in f:
#         nums = list(map(int, line.split()))
#         rows.append(nums)

# valid = 0
# for r in rows:
#     if check(check_inc, r):
#         valid += 1
#     elif check(check_dec, r):
#         valid += 1
#     else:
#         for i in range(len(r)):
#             removed = r.pop(i)

#             if check(check_inc, r):
#                 valid += 1
#                 r.insert(i, removed)
#                 break
#             elif check(check_dec, r):
#                 valid += 1
#                 r.insert(i, removed)
#                 break

print(valid)

