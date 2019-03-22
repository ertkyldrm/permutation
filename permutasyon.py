#!/usr/bin/env python
# coding: utf-8

# In[3]:


def faktoriyelHesapla(i):
    
    if i==1:       
        return 1
    
    else: 
        return i * faktoriyelHesapla(i-1)
    
def permutasyonHesapla(j,k):
    
    l = 0
    
    if k>j:        
        l = l
        
    else:      
        l = faktoriyelHesapla(j)/faktoriyelHesapla(j-k)
        return l
  
 
sayi1 = int(input("Kaç kişilik masa : "))
 
sayi2 = int(input("Kişi sayısı ")) 

if sayi1<sayi2:
  print("Hata!!! Kişi sayısı masadaki boş yer sayısından fazla olamaz")
else:
  print( sayi1,"kişilik masaya",sayi2 ,"kadar kişi", permutasyonHesapla(sayi1,sayi2),"farklı şekilde oturur." ) 


# In[ ]:




