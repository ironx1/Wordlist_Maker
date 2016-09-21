print("""
**----------------------------**
     Wordlist Maker  V2.0     
        Coder : Ironx1             
**----------------------------**
""")

while True:	
	a = int(input("İlk Sayı : "))
	b = int(input("Son Sayı : "))
	dosya = input("Dosya Adı : ")
	f = open("{}".format(dosya), "w")
	for i in range(a, b+1):
		print(i, file=f)
	f.close()
	soru = input("Devam Edilsin mi? (e/h) : ")# Not : programdan çıkmak istiyorsanız bu soruya h diyin yoksa dosya kaydedilmez!
	if soru == "e":
		pass
	else:
		break
