sec = int(input())
h = (sec // 3600)
m = (sec % 3600) // 60
s = (sec % 60)
print(f"{h}:{m}:{s}")