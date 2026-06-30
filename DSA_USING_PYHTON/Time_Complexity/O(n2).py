def find_duplicates(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j and num[i] == num[j]:
                return True
    return False

num = [10, 20, 30, 50, 40]
res = find_duplicates(num)
print(res)