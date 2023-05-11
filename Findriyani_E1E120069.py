print(" Nama : Findriyani ")
print(" NIM : E1E120069 ")
print(" Pengecekkan Jumlah Produksi Kemasan Makanan ABC, Metode Mamdani")

pmt_b = 5000
pmt_k = 1000
psd_b = 600
psd_k = 100
prd_max = 7000
prd_min = 2000

x = int(input("Masukkan Jumlah Permintaan\t: "))
y = int(input("Masukkan Jumlah Persediaan\t: "))

#Permintaan Naik --> Linear Naik
if x<pmt_k:
    miu_pmt_naik = 0
elif x>=pmt_k and x<=pmt_b:
    miu_pmt_naik = (x-pmt_k)/(pmt_b-pmt_k)
else:
    miu_pmt_naik = 1

#Permintaan Turun --> Linear Turun
if x<pmt_k:
    miu_pmt_turun = 1
elif x>=pmt_k and x<=pmt_b:
    miu_pmt_turun = (pmt_b-x)/(pmt_b-pmt_k)
else:
    miu_pmt_turun = 0

#Persediaan Sedikit --> Linear Turun
if y<psd_k:
    miu_psd_sedikit = 1
elif y>=psd_k and y<=psd_b:
    miu_psd_sedikit = (psd_b-y)/(psd_b-psd_k)
else:
    miu_psd_sedikit = 0

#Persediaan Banyak --> Linear Naik
if y<psd_k:
    miu_psd_banyak = 0
elif y>=psd_k and y<=psd_b:
    miu_psd_banyak = (y-psd_k)/(psd_b-psd_k)
else:
    miu_psd_banyak = 1

print("\nNilai Derajat Keanggotaan Permintaan Naik\t:",miu_pmt_naik)
print("Nilai Derajat Keanggotaan Permintaan Turun\t:",miu_pmt_turun)
print("Nilai Derajat Keanggotaan Persediaan Sedikit\t:",miu_psd_sedikit)
print("Nilai Derajat Keanggotaan Persediaan Banyak\t:",miu_psd_banyak)
print("")

#Rule
def r1():
    r1=min(miu_pmt_turun,miu_psd_banyak)
    return r1

def r2():
    r2=min(miu_pmt_turun,miu_psd_sedikit)
    return r2

def r3():
    r3=min(miu_pmt_naik,miu_psd_banyak)
    return r3

def r4():
    r4=min(miu_pmt_naik,miu_psd_sedikit)
    return r4

#Agregasi
linear_turun = max(r1(),r2())
linear_naik = max(r3(),r4())

if (linear_turun>linear_naik):
    a1 = round(prd_max - (((prd_max - prd_min)* linear_turun)-prd_max))
    a2 = round(prd_max - (((prd_max - prd_min) * linear_naik) - prd_max))
    print("a1\t= ",a1,"\na2\t= ",a2)
    print("*************")
    print(miu_pmt_naik,";\t\t\tz<=",a1)
    print("(",prd_max," - z )/",(prd_max-prd_min),";\t",a1,"<=","z<=",a2)
    print(miu_psd_banyak,";\t\t\tz>=",a2)
    def m(z):
        if(z<=a1):
            mz=linear_turun
        elif(z>a1 and z<a2):
            mz=(prd_max-z)/(prd_max-prd_min)
        else:
            mz=linear_naik
        return mz

elif (linear_turun==linear_naik):
    a1 = round(prd_max-((prd_max-prd_min)*linear_turun))
    print("Adapun nilai a1 yang didapatkan adalah ",a1)
    print("*************")
    print(miu_pmt_turun,";\t\t\tz<=",prd_max)
    def m(z):
        mz=linear_turun
        return mz

else:
    a1 = round(((prd_max-prd_min)*linear_turun)+prd_min)
    a2 = round(((prd_max - prd_min) * linear_naik) + prd_min)
    print("a1\t= ",a1,"\na2\t= ",a2)
    print("*************")
    print(miu_pmt_turun,";\t\t\tz<=",a1)
    print("( z -",prd_min,")/",(prd_max-prd_min),";\t",a1,"<=","z<=",a2)
    print(miu_psd_sedikit,";\t\t\tz>=",a2)
    
    def m(z):
        if(z<=a1):
            mz=linear_turun
        elif(z>a1 and z<a2):
            mz=(z-prd_min)/(prd_max-prd_max)
        else:
            mz=linear_naik
        return mz