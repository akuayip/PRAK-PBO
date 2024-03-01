#  M.Arief Rahman Hakim
#  122140083

batas_bawah = int(input("batas bawah : "))
batas_atas = int(input("batas atas : "))

if batas_bawah  < 0 or batas_atas < 0 :
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah nol")
else:
    sum = 0
    for i in range(batas_bawah, batas_atas):
        if i % 2 != 0 :
            print(i)
            sum += i
    print("Total : ", sum)



