def second_max(lst):
    first = second = -10**18
    for x in lst:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return second

def sort_list(lst):
    n = len(lst)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst

def count_words(s):
    words = s.split()
    return len(words)

def sum_of_list(lst):
    s = 0
    for x in lst:
        s += x
    return s

def multiplication_table(n):
    i = 1
    while i <= 10:
        print(n, "*", i, "=", n * i)
        i += 1

if __name__ == "__main__":
    n = int(input())
    print(is_prime(n))
    n = int(input())
    print(factorial(n))
    n = int(input())
    print(fibonacci(n))
    n = int(input())
    print(reverse_number(n))
    n = int(input())
    print(is_palindrome(n))
    n = int(input())
    print(sum_of_digits(n))
    a, b = map(int, input().split())
    print(gcd(a, b))
    a, b = map(int, input().split())
    print(lcm(a, b))
    s = input()
    print(count_vowels(s))
    lst = list(map(int, input().split()))
    print(max_in_list(lst))
    lst = list(map(int, input().split()))
    print(second_max(lst))
    lst = list(map(int, input().split()))
    print(sort_list(lst))
    s = input()
    print(count_words(s))
    lst = list(map(int, input().split()))
    print(sum_of_list(lst))
    n = int(input())
    multiplication_table(n)
