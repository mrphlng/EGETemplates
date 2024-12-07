a = int(input())
if 11 <= a % 100 <= 14:
    print("Грибов")
elif 1 < a % 10 <=4:
    print("Гриба")
elif a % 10 == 1:
    print("Гриб")
else:
    print("Грибов")
