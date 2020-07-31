def count_primes(num):
    list_prime = []
    for num1 in range(0, num + 1):
        if num1 > 1:
            for i in range(2, num1):
                if num1 % i == 0:
                    break
            else:
                list_prime.append(num1)
    return list_prime


list_result = count_primes(100)
print(list_result)
