def prime_count_vanilla(range_from: int, range_til: int):
    """ Returns the number of prime numbers within a given range """
    prime_count = 0
    num = range_from if (range_from >= 2) else 2
    while num <= range_til:
        divnum = 2
        flag = 0
        while divnum < num:
            if ((num % divnum) == 0):
                flag = 1
                break
            divnum += 1
        if flag == 0:
            prime_count += 1
        num += 1
    return prime_count


def prime_count_vanilla_range(range_from: int, range_til: int):
    """ Returns the number of found prime numbers using range"""
    prime_count = 0
    range_from = range_from if range_from >= 2 else 2
    for num in range(range_from, range_til + 1):
        for divnum in range(2, num):
            if ((num % divnum) == 0):
                break
        else:
            prime_count += 1
    return prime_count


print(prime_count_vanilla(0, 100000))
print(prime_count_vanilla_range(1, 100000))
