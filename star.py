
print("Star Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue   
    print(i)

print("\nUsing break:")
for i in range(1, 6):
    if i == 4:
        break   
    print(i)