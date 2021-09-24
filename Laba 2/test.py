counter = 0
mas = [[0] * 4] * 5
for i in range(5):
    for j in range(4):
        mas[i][j] = counter
        counter += 1
print(mas)
