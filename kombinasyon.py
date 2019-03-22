

def faktoriyelHesapla(i):
    
    if i==1:       
        return 1
    
    else: 
        return i * faktoriyelHesapla(i-1)
    
def kombinasyonHesapla(j,k):
    
    if (j<k):
        print("1. Sayının 2. Sayıdan büyük yada eşit olması gerekli. Verdiğiniz sayıların çözümü yoktur!")
   
    elif(j==k):
        print("1")
    
    elif(j>k):
        
        s=1
        s= faktoriyelHesapla(j) #n faktöriyel
        
        l=1
        l= faktoriyelHesapla(k) #m faktöriyel
        
        f=1
        f= faktoriyelHesapla(j-k) #n-m faktöriyel
        
        w=s/(l*f)
        return w
       
 
sayi1 = int(input("Torbadaki bilye sayısı :"))
 
sayi2 = int(input("Torbadan kaç adet bilye seçileceği :  ")) 
 
print(sayi1, "kadar bilyeden ", sayi2,"kadar bilye", kombinasyonHesapla(sayi1,sayi2),"şekilde seçilebilir.", )

