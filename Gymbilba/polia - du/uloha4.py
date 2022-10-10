A = [4,8,2,7,3,6,1,5]

for i in range(len(A)):
    is_bigger = True
    for j in range(i + 1, len(A)):
        print("if " + str(A[i]) + " < " + str(A[j]) + ": ")
        if A[i] < A[j]:
            is_bigger = False
    if is_bigger:
       print(i)