import json

# JSON Dosyasını Okumak İçin Kullandığımız Kısım
with open("cv_verileri.json", "r", encoding="utf-8") as dosya:
    cv_listesi = json.load(dosya)

# İşe Alınacak Olan Kişide Aradığımız Kriterler
aranan_kriterler = {
    "mezuniyet_bolumu": ["Bilgisayar Mühendisliği", "Yazılım Mühendisliği", "Yönetim Bilişim Sistemleri", "Bilişim Sistemleri Ve Teknolojileri"],
    "min_deneyim": 5,
    "programlama_dilleri": ["HTML", "CSS", "JavaScript", "TypeScript", "React", "Vue.js"],
    "yabanci_diller": ["İngilizce"],
    "sertifikalar": ["Google Cloud Certified", "AWS Certified"],
    "pozisyon_tercihi": "Frontend Developer"  
}

def cv_skorla(cv, kriterler):
    skor = 0 #Skor Şuanda 0 Her Kritere Göre + Puan Veriyoruz Bu Puanları Nasıl Ve Ne kadar Verdiğimiz Bizim Seçimimiz

    for b in kriterler["mezuniyet_bolumu"]:
        if b.lower() == cv["mezuniyet"]["bolum"].lower():
            skor+=20

    #Deneyim Yılı Bizim Kriterden Büyük Veya Eşit İse +15 Puan
    if cv["deneyim_yili"] >= kriterler["min_deneyim"]:
        skor += 15

    # Kriterlere Uyan Her Dil İçin +10 Puan
    for pdk in kriterler["programlama_dilleri"]:
        for pdc in cv["programlama_dilleri"]:
            if pdk.lower()==pdc.lower():
                skor +=  10

    for ybdk in kriterler["yabanci_diller"]:
        for ybdc in cv["yabanci_diller"]:
            if ybdk.lower()==ybdc.lower():
                skor += 5            


    for srfk in kriterler["sertifikalar"]:
        for srfc in cv["sertifikalar"]:
            if srfk.lower()==srfc.lower():
                skor += 10

    # Pozisyon tercihi
    if cv["pozisyon_tercihi"] == kriterler["pozisyon_tercihi"]:
        skor += 10

    return skor

# CV'leri Skorluyoruz .append ile 
skorlanmis_cvler = []
for cv in cv_listesi:
    skor = cv_skorla(cv, aranan_kriterler)
    skorlanmis_cvler.append((cv, skor))

# Skoru En Yüksek Olan CVler En Üst Sırada Olacak
sirali_cvler = sorted(skorlanmis_cvler, key=lambda x: x[1], reverse=True)

# Skoru En Yüksek Olan 16 CVyi Yazdırcaz
print("\n📋 En Uygun 16 CV:")
for cv, skor in sirali_cvler[:16]:
    print(f"- {cv['ad']} | Skor: {skor}")
