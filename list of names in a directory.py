import os
path = 'C:\\xampp\\htdocs\\ShoppingPortalProVersion\\shopping\\admin\\productimages'
d = {}
a = os.listdir(path)
print(a)
for i in a:
    path1 = path + "\\" + i
    if i != 'index.php': 
        if os.path.exists(path1) and os.listdir(path1) != 0:
            dirs = os.listdir(path1)
        if os.path.exists(path1) and len(dirs) != 0:
            a1 = os.listdir(path + "\\" + i)
            d[i] = a1

print(d)

for i in d.keys():
    print(i)
    print(d[i])
