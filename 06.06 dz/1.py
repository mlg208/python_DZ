def print_smileys(n):
    if n <= 0:
        return
    print("😊", end="")
    print_smileys(n - 1)

print_smileys(5)
