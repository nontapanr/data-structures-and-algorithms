"""
ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

"""

def length(txt):
    if txt == '':
        return 0
    else:
        s = length(txt[:-1])
        print(txt[s], end = "*" if s % 2 == 0 else "~")
        return 1 + s

print("\n", length(input("Enter Input : ")), sep="")
# # ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)

"""
Enter Input : hello
h*e~l*l~o*
5

Enter Input : data structure is easy
d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
22

Enter Input : *~*~*~
**~~**~~**~~
6



"""