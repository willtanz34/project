unit = ["","one","two","three","four","five","six","seven","eight","nine"]

n = float(input("Whats the number :"))

def terbilangEnglish(n):
    
    if n%1>0:
        x=str(n)
        find = x.find(".")
        BelakangKoma = find+1
        hasilKoma = []
        hasilDepan=[]

        for v in x[0:find]:
            hasilDepan.append(v)

        for i in x[BelakangKoma:]:
            hasilKoma.append(i)

        PenggabunganDepanKoma="".join(hasilDepan)
        convertD=int(PenggabunganDepanKoma)
            
        PenggabunganKoma = "".join(hasilKoma)
        ConvertK=int(PenggabunganKoma)

        return terbilangEnglish (convertD) + " comma " + terbilangEnglish(ConvertK)
    
    elif n < 10:
        return unit[int(n)]
    elif n >= 1_000_000_000:
        return terbilangEnglish(n // 1_000_000_000) + " billion " + terbilangEnglish(n % 1_000_000_000)
    elif n >= 1_000_000:
        return terbilangEnglish(n // 1_000_000) + " million " + terbilangEnglish(n %  1_000_000)
    elif n >= 1000:
        return terbilangEnglish(n // 1000) + " thousand " + terbilangEnglish(n % 1000)
    elif n >= 100:
        return terbilangEnglish(n // 100) + " hundred " + terbilangEnglish(n % 100)
    elif n >= 20:
        if n >= 60:
            return terbilangEnglish(n // 10) + "ty " + terbilangEnglish(n % 10)
        elif n >= 50:
            return "fifty " + terbilangEnglish(n % 10)
        elif n >= 40:
            return "forty " + terbilangEnglish(n % 10)
        elif n >= 30:
            return "thirty " + terbilangEnglish(n % 10)
        elif n >= 20:
            return "twenty " + terbilangEnglish(n % 10)
    elif n >= 10:
        if n == 10:
            return "ten"
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 15:
            return "fifteen"
        else:
            return terbilangEnglish(n % 10) + ("teen" if n%10 != 8 else "een")

if n % 1 > 0:
    print (f'{n} = {terbilangEnglish(n)}')
else:
    print (f'{int(n)} = {terbilangEnglish(n)}')