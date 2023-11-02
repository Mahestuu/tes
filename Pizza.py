print ("=============== =============== \n" "  SELAMAT DATANG DI PIZZA HUT       \n" "=============== =============== \n" )
print ("                SILAHKAN PILIH MENU           ")
print ("| ========== Pizza ========= |" " ====== Harga ===== | ")
print ("|   1. Frankfurter BBQ       |     Rp. 43.637     |")
print ("|   2. Meat Monsta           |     Rp. 43.637     |")
print ("|   3. Super Supreme         |     Rp. 43.637     |")
print ("|   4. Super Supreme Chicken |     Rp. 43.637     |")


# def pesanan():
    # global listpizza 

    # listpizza = ["Frankfurter BBQ","Meat Monsta","Super Supreme","Super Supreme Chicken"]
harga_pizza = 0

jumlah_pesan = (input("Masukan Jumlah Pesanan : "))
pesan = str(input("\nMasukan No Menu Yang Di Inginkan : "))

if pesan == "1" : 
    listpizza = "Frankfurter BBQ"
    harga_pizza = (43637*jumlah_pesan)
        # listpizza [0]
elif pesan == "2" :
    listpizza = "Meat Monsta"
    harga_pizza = (43637*jumlah_pesan)
        #jumlah_pesan = (input("Masukan Jumlah Pesanan : "))
        # listpizza [1]
elif pesan == "3" : 
    listpizza = "Super Supreme"
    harga_pizza = (43637*jumlah_pesan)
        #jumlah_pesan = (input("Masukan Jumlah Pesanan : "))
        # listpizza [2]
elif pesan == "4" :
    listpizza = "Super Supreme Chicken"
    harga_pizza = (43637*jumlah_pesan)
        # jumlah_pesan = (input("Masukan Jumlah Pesanan : "))
        # listpizza [3]
else : 
    print("\n=== Maaf Pesanan Tidak Tersedia Di Dalam Menu ===\n" "=== Silahkan Pilih Menu Lagi ===")
    # pesanan()


# pesanan()
total = harga_pizza

print("Menu : ", listpizza)
print("Jumlah Pesanan : ", jumlah_pesan)
print("Total Harga : ", harga_pizza)


