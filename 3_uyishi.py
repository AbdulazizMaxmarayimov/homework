# act 3
suz = input(">>> ")
for i in suz.split():
    quti = 1
    m = ""
    for j in i:
        if j in m:
            quti = 0
            break
        if j.isalpha():
            m += j
    if quti:
        n = len(m) // 2
        m = m[-n:] + m[:-n]
        print(m)