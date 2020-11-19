def angka(x):
    listbaru = set()
    for i in x :
        listbaru.add(i)
    new = list(listbaru)
    return new

samplelist = [1,2,3,3,3,3,4,5]
print(angka(samplelist))
        