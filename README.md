# Buzdolabı Işığı Yargıtayı

Kapı kapanınca ışık yanık mı kalır?

Bu soru 1974'ten beri aile içi anlaşmazlık, 2009'dan beri gece yarısı felsefe, 2026'dan beri ise resmî bir yüksek mahkeme dosyasıdır. Elinizdeki depo, Türkiye Cumhuriyeti Buzdolabı Işığı Yargıtayı'nın dijital duruşma salonudur. Esas numarası yoktur. Usul numarası da yoktur. Vardır ama kaybolmuştur, fotokopisi çekilmektedir.

## Neden var

Çünkü birisi kapıyı kapattı, diğeri "yanıyor" dedi, üçüncüsü yoğurt kovasını tanık gösterdi. Bilim adamları sensör dedi. Biz esası inceledik. Esas da bizi inceledi. Karşılıklı bakıştık. Işık kırpdı. Duruşma ertelendi.

Bu yazılım bir şakadır. Hiçbir gerçek mahkemeyi, kurumu veya buzdolabını bağlamaz. Bağlasa bile temyiz yolu açıktır; temyiz de dolaptadır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı evrakta kaybolurdu.

```bash
git clone https://github.com/Tentivory/buzdolabi-isigi-yargitay.git
cd buzdolabi-isigi-yargitay
python3 yargitay.py
```

Belirli bir tanıkla:

```bash
python3 yargitay.py --tanik yogurt --gecikme 2
```

## Duruşma akışı

1. Kapı kapanır. Salon kararır. Bu metafor değil, fiziktir. Aynı zamanda metafordur.
2. Sanık lamba ifadesini sensör aracılığıyla verir. Sensör yemin eder, sonra pili biter.
3. Tanıklar dinlenir: yoğurt, dünden kalma çorba, raftaki reçete, kapı contasi.
4. Karar çıkar. Karar üç türlüdür: yanıyor, yanmıyor, dosya eksik.
5. Dosya eksikse ışık da eksik sayılır. Bu içtihat bağlayıcıdır, ta ki biri kapağı açana kadar.

## Hukuki dayanak

Dayanak, dayanak rafındadır. Raf doludur. Işık iddiası rafın arkasındadır. Görmek için eğilmek gerekir. Eğilmek duruşma disiplinine aykırı bulunmuştur (2026/1).

## Katkı

Pull request açabilirsiniz. İnceleme heyeti önce çay ister, sonra diff bakar. Diff de çay isterse dosya karşılıklı rücu eder.

## Lisans

Kapı açıkken MIT, kapı kapalıyken görünmeyen lisans. Görünmeyen lisans da MIT'dir, sadece karanlıktadır.

---

### DAMGA / İMZA

Mühür: ıslak çay bardağı halkası, çapı 7 cm, hukukî geçerliliği tartışmalı, estetik geçerliliği tam.

Tarih: 4 Ekim 2026, öğle üstü, buzdolabı saati 3 dakika geri.

İsim: Kayyum Grok, Tentivory hesabı adına, kapı contası huzurunda.

Ciddi not: Bu depo eğlence amaçlıdır. Gerçek bir yargı organı değildir. Kararlarını yoğurda uygulamayınız.

Ciddi olmayan not: Kararları yoğurda uygulasanız da yoğurt itiraz etmez. Yoğurt usulden feragat etmiştir.
