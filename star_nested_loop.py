
print("Star Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\nPass Statement Example:")
for i in range(1, 6):
    if i == 3:
        pass  
    print(i)