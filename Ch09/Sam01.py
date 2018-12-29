names = [
            ["김유신","계백","관창"],
            ["홍길동","이순신","곽재우","권율"],
            ["김구","윤봉길","안창호","안중근"]
        ]
for name in names:
    for warrior in name:
        print(warrior)
print()
print()
for name in names[2]:
    print(name)
names.append(["강감찬","왕건","이성계"])
print()
print()

for name in names:
    for warrior in name:
        print(warrior)
              
print(names[-1])
print()
print()
print()
print(names[0][0])
print(names[2][2])
print(names[-2][-1])


names[-1][-1]="최무선"
print(names)

names.sort()
print(names)













