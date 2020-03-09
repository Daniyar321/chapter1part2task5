class_A = int(input())
class_B = int(input())
class_C = int(input())
if class_A and class_B and class_C % 2 != 0:
    print((class_A + 1) // 2, (class_B + 1) // 2, (class_C + 1) // 2)
else:
    print(((class_A+1) // 2) + ((class_B+1) // 2) + ((class_C+1) // 2))
