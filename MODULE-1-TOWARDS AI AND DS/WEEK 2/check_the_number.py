def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        # Your code here
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results


n = 7
assert check_the_number(n) == "False"
n = 2
results = check_the_number(n)
print(results)
