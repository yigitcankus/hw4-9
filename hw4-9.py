import numpy as np
import random
import matplotlib.pyplot as plt

örneklem = []
örneklem_ortalamaları = []
for atış_sayısı in range(1,2000):
    atış = np.random.randint(low=0,high=2, size=1)
    örneklem.append(atış)
    örneklem_ortalamaları.append(np.mean(örneklem))

def orneklem_plotla(örneklem_ortalaması,orneklem_sayisi, subplot_no):
    plt.subplot(subplot_no)
    plt.plot(örneklem_ortalaması[0:orneklem_sayisi])
    plt.ylim((0,1))
    plt.title("Örneklem Sayısı = {}, (0 yazı 1 tura)".format(orneklem_sayisi))
    plt.xlabel("Örneklem Sayısı")
    plt.ylabel("Örneklem Ortalaması")

plt.figure(figsize=(13,5), dpi=100)

orneklem_plotla(örneklem_ortalamaları,50, 131)
orneklem_plotla(örneklem_ortalamaları, 500, 132)
orneklem_plotla(örneklem_ortalamaları, 2000, 133)
plt.show()

#-----

#Netflixe ilk üye olurken bize beğendiğimiz tür ve kategorileri soruyor.
#burda seçtiğimiz şeyler netflixi yeni kullanmaya başladığımız zamanlarda yardımcı oluyor ve ekranda hep onları görüyoruz
#daha sonra biizm izlediğimiz diziler ve onların konusuyla alakalı şeyler olmaya başlıyor.
#yeni öneriler çıkarığında onlara tıklayıp tıklamadığmıız önemli bir şey olabilir. Eğer bir kişi asla tıklamıyorsa yeni
#şeyler çıkarmayı bırakabilir ve eskiden izlediğimiz şeyleri tekrar önümüze koyabilir.

