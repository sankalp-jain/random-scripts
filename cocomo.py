def basic(value):
    d = {}
    s = ["organic", "semi-detached", "embedded"]
    d['organic'] = [2.4, 1.05, 2.5, 0.38, 60]
    d['semi-detached'] = [3, 1.12, 2.5, 0.35, 75]
    d['embedded'] = [3.6, 1.20, 2.5, 0.32, 90]

    for i in s:
        a = d[i]
        print(i.upper())
        effort = a[0] * pow(a[4], a[1]) * value
        tdev = a[2] * pow(effort, a[3])
        print("effort for ", i, "is", effort)
        print("tdev for ", i, "is", tdev)
        print("cost for ", i, "is", tdev * 45000)

def intermediate():
    l = []
    for i in range(15):
        num = float(input("Enter the value"))
        l.append(num)
    s = sum(l)
    basic(s)

print("The effort, tdev, cost required for Basic is")
basic(1)
print("The effort, tdev, cost required for Intermediate is")
intermediate()
