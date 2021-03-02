import numpy as np
#dizi oluşturma
result = np.array([1,3,5,7,9])
# 1 den n e kadar dizi oluşturma
result = np.arange(1,100)
#n den n e kadar n artışlı dizi
result = np.arange(10,100,3)
#n tane sıfırlı liste
result = np.zeros(10)
#n tane 1 li liste
result = np.ones(10)
#belirli bir aralıkta eşit artışa sahip olan liste n den başla n e kadar git n böl
result = np.linspace(0,1000,5)
result = np.linspace(0,5,5)
# n ile n arasından rastgele bir sayı random kütüphanesi ile aynı
result = np.random.randint(1,10)
#sıfırdan n e kadar  git 1 sayı al 
result = np.random.randint(20)
# n'den n'e kadar  n kadar git n sayı al listeye çevir
result = np.random.randint(1,60,6)
#0 ile 1 arasında n tane sayı üret
result = np.random.rand(5)
# 0 ile 1 arasında ve eksi 1 ile 0 ın arasında n sayı üret
result = np.random.randn(5)
# 0'dan n'e kadar n dahil değil listesi döndürür
np_array = np.arange(50)
# 0'dan n' e kadar olan listeyi n tane n parçaya bölüp ekrana yazdırır 
result = np_array.reshape(5,10)
# n'den n'e n tane sayı üreten liste
rd = np.random.randint(1,100,10)
print(rd)
# listedeki en büyük sayıyı ekrana döndürür
result = rd.max()
#listedeki en küçük sayıyı ekrana döndürür
result = rd.min()
#listede üretilen sayıların ortalaması
result  = rd.mean()
# en büyük sayı hangi indekste not: array 0dan başlar
result =  rd.argmax()
# en küçük sayı hangi indekste not: array 0 dan başlar
result = rd.argmin()



print(result)
