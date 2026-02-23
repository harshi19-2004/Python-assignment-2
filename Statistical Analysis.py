# Q13 Bonus - added median and mode

try:
    count = int(input("How many numbers? "))
    numbers = []

    for i in range(1, count + 1):
        num = float(input("Enter number " + str(i) + ": "))
        numbers.append(num)

    total = sum(numbers)
    average = total / count

    # median
    sorted_nums = sorted(numbers)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]

    # mode - number that appears most
    freq = {}
    for n in numbers:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    mode = max(freq, key=freq.get)

    print("Sum     : " + str(total))
    print("Average : " + str(average))
    print("Max     : " + str(max(numbers)))
    print("Min     : " + str(min(numbers)))
    print("Median  : " + str(median))
    print("Mode    : " + str(mode))

except:
    print("Invalid input!")