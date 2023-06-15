start = 32
end = 126

for num in range(start, end + 1):

    if (num - start) % 5 == 0:
        print()

    print(f"{num}: {chr(num)}", end="  ")

print() 