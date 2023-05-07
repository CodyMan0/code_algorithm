n = int(input())

nums_pileup = 1
count = 1

while n > nums_pileup:
    nums_pileup += 6 * count
    count += 1

print(count)