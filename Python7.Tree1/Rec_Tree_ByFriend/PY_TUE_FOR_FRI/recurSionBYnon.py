"""
จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

โดยแสดงผลตามตัวอย่าง

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

"""

'''
 * กลุ่มที่  : 20010101
 * 62010452 นนทกร จิตรชิรานันท์
 * chapter : 2	item : 1	ครั้งที่ : 0002
 * Assigned : Saturday 19th of September 2020 06:58:51 PM --> Submission : Saturday 19th of September 2020 07:04:58 PM	
 * Elapsed time : 6 minutes.
 * filename : 1.py
'''
def print1ToN(n):
    #code here
    if n <= 1:
        print(1, end=' ')
    else:
        print1ToN(n-1)
        print(n, end=' ')

def printNto1(n):
    #code here
    if n <= 1:
        print(1, end=' ')
    else:
        print(n, end=' ')
        printNto1(n-1)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)