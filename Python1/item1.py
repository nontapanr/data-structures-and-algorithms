print("*** Rabbit & Turtle ***")

d, vr, vt, vf = input("Enter Input : ").split()
d = int(d)
vr = int(vr)
vt = int(vt)
vf = int(vf)

deltaV = abs(vr-vt)
time = d/deltaV
df = time*vf

print("{:.2f}".format(df))