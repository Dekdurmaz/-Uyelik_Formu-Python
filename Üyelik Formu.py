from tkinter import *
window = Tk()

window.title("Üyelik Formu")
window.geometry("500x350")
window.resizable(height=False, width=False)
window.iconbitmap("pro.ico")
window.configure(bg="#D7C6EE")

# Bu bölümde üyelik formu için gerekli olan tüm widgetlar oluşturuldu.
frame1 = Frame(window, bg="#D7C6EE")
frame1.grid(row=0, column=0,)
frame2 = Frame(window, bg="#D7C6EE")
frame2.grid(row=0, column=1,)
frame3 = Frame(window, bg="#D7C6EE")
frame3.grid(row=0, column=2,)
frame4 = Frame(window, bg="#D7C6EE")
frame4.grid(row=1, column=2,)
frame5 = Frame(window, bg="#D7C6EE")
frame5.place(x=100, y=230,)

#Bu bölümde frame1 için gerekli olan tüm widgetlar oluşturuldu.
Label(frame1, text="Adınız", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame1, text = "Soyadınız", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame1, text = "Yaşınız", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame1, text = "Doğum", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame1, text = "Cinsiyet", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()

# Bu bölümde frame2 için gerekli olan tüm widgetlar oluşturuldu.
Label(frame2, text=":", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame2, text=":", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame2, text=":", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame2, text=":", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()
Label(frame2, text=":", bg="#D7C6EE", fg="#000000", font=("Arial bold", 12),padx=5, pady=5).pack()

# Bu bölümde frame3 için gerekli olan tüm widgetlar oluşturuldu.
Entry(frame3, bg="#ffffff", fg="#000000", justify="center" ).pack(padx=5, pady=5)
Entry(frame3, bg="#ffffff", fg="#000000", justify="center").pack(padx=5, pady=5)
Spinbox(frame3, from_=18, to=100, bg="#ffffff", fg="#000000", justify="center",width=19).pack(padx=5, pady=5)

# Bu bölümde en alttaki ekran görüntüsünde bulunan tüm widgetlar oluşturuldu.
Button(window, text="Kaydet", bg="green", font=("Arial bold", 12), width=12, ).place(x=100, y=270)
Button(window, text="Temizle", bg="yellow", font=("Arial bold", 12), width=12, ).place(x=260, y=270)

# Bu bölümde görsel yüklenmesi için gerekli olan tüm widgetlar oluşturuldu.
photo = PhotoImage(file="profil.png")
photoResized = photo.subsample(8, 8)
Button(window, text="Yükle" , image= photoResized , compound=TOP ).place(x=325, y=11)

#Bu bölümde Aylar için gerekli olan tüm widgetlar oluşturuldu.
optionList = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
sval = StringVar(frame3)
sval.set(optionList[0])
opm1 = OptionMenu(frame3, sval, *optionList)
opm1.config(bg="#ffffff",fg="#000000", justify="center", width=15)
opm1.pack(padx=5, pady=5)

#Bu bölümde Erkek ve Kadın butonları için gerekli olan tüm widgetlar oluşturuldu.
rdm1= Radiobutton(frame3, text="Erkek", value=1 ).pack(side=LEFT, padx=5, pady=5)
rdm2= Radiobutton(frame3, text="Kadın", value=2).pack(side=LEFT,  padx=5, pady=5)

#Bu bölümde onay kutusu için gerekli olan tüm widgetlar oluşturuldu.
Checkbutton(frame4, text="Formu okudum, onaylıyorum.", bg="#ffffff", fg="#000000", font=("Arial bold", 8),justify="center").pack(padx=5, pady=5)

#Bu bölümde ara siyah çizgi olurşturuldu.
cv = Canvas(frame5, width=273, height=2,bg="black",highlightthickness=0)
cv.create_line(100, 50, 300, 0, fill="black", width=2)
cv.pack()

#Bu bölümde sürekli çalışan bir döngü oluşturuldu.
window.mainloop()