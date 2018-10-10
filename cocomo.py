def basic(value):

    d = {}
    print("Enter category")
    s = input()
    d['organic'] = [2.4, 1.05, 2.5, 0.38, 60]
    d['semi-detached'] = [3, 1.12, 2.5, 0.35, 75]
    d['embedded'] = [3.6, 1.20, 2.5, 0.32, 90]

    a = d[s]
    
    effort = a[0] * pow(a[4], a[1]) * value
    tdev = a[2] * pow(effort, a[3])
    print(effort)
    print(tdev)
    print(tdev * effort * 45000)

def intermediate():
    l = []
    for i in range(15):
        num = float(input("Enter the value"))
        l.append(num)
    #l = [0.75, 0, 0, 0, 0.7, 0, 1.46, 1.29, 1.42, 0, 1.21, 0, 1.24, 1.24, 1.23]
    s = sum(l)
    basic(s)
    
        
    
stage = input("Enter stage")
flag = 0
if stage == 'basic':
    basic(1)
else:
    intermediate()
