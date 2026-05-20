# PROBLEMS.md

Bu projede ilk başta herhangi bir tasarım prensibi düşünmeden kod yazıldı. Daha sonra kod incelendiğinde bazı problemler fark edildi. Aşağıda bu problemler ve kısa açıklamaları yer almaktadır.

---

## 1. SRP (Single Responsibility Principle) ihlali

Cart sınıfı hem ürünleri tutuyor hem ödeme yapıyor hem de fiyat ve indirim hesaplıyor.
Bir sınıfın tek bir işi olması gerekirken burada birden fazla sorumluluk üstlenmiş.

---

## 2. OCP (Open/Closed Principle) ihlali

Yeni bir indirim eklemek istediğimizde mevcut koda yeni `elif` eklemek gerekiyor.
Bu da kodun değiştirilmeye açık olduğunu ve genişletilebilir olmadığını gösteriyor.

---

## 3. DRY (Don't Repeat Yourself) ihlali

Aynı kod blokları (product ekleme, total_price artırma vs.) birden fazla kez yazılmış.
Bu tekrarlar kodu uzatıyor ve değişiklik yaparken hata yapma ihtimalini artırıyor.

---

## 4. Type Safety problemi

`total_price` başlangıçta `None` olarak atanmış ama sonrasında sayı gibi kullanılmış.
Bu durum runtime hatalarına sebep olabilir.

---

## 5. Domain Modeling problemi

Ürünlerin fiyatı hiç kullanılmıyor, sadece sabit sayılar ekleniyor.
Gerçek hayatta bir sepetin toplamı ürün fiyatlarına göre hesaplanmalı.

---

## 6. Magic String kullanımı

İndirimler string olarak kontrol ediliyor (`"DISCOUNT_10"` gibi).
Bu yöntem hataya açık ve yönetmesi zor bir yapı oluşturuyor.

---

## 7. Anlaşılması zor indirim mantığı

İndirim uygulanırken toplam fiyata ekleme yapılıyor.
Bu durum indirim mi yoksa ekstra ücret mi olduğu konusunda kafa karıştırıyor.

---

# Sonuç

Kod çalışıyor gibi görünse de tasarım açısından birçok problemi var.
Bu problemlerin düzeltilmesi kodun daha temiz, anlaşılır ve geliştirilebilir olmasını sağlar.




# AI vs Benim Analizim (Karşılaştırma)

Bu bölümde, yazdığım kodu analiz ettikten sonra bulduğum problemler ile bir AI aracının bulduğu problemler karşılaştırılmıştır.

---

## AI’ın Gördüğü Problemler

AI aşağıdaki tasarım sorunlarını tespit etti:

if-elif ile yazılmış indirim zinciri → Strategy Pattern önerdi
`total_price = None` kullanımı → yanlış başlatma
İç durumun (products listesi) dışarıya açılması → encapsulation sorunu
Tek metodun birden fazla iş yapması → SRP ihlali
Magic string kullanımı → Enum önerdi

---

## Benim Gördüğüm Problemler

Kod incelemesi sonucunda şu problemleri fark ettim:

SRP (Single Responsibility Principle) ihlali
OCP (Open/Closed Principle) ihlali
DRY (Don't Repeat Yourself) ihlali
Type safety problemi (`None` ile işlem yapılması)
Domain modeling problemi (ürün fiyatı kullanılmıyor)
Magic string kullanımı
İndirim mantığının belirsiz olması

---

## Karşılaştırma

### Ortak Noktalar

SRP ihlali her iki analizde de var
Magic string problemi ikimiz tarafından da fark edildi
İndirim sisteminin kötü tasarlandığı konusunda aynı fikirdeyiz
`total_price` ile ilgili hata her iki tarafta da tespit edildi

### AI’ın Ekstra Gördükleri

Encapsulation (iç veri dışarıya açık olması)
Daha direkt çözüm önerileri (Strategy Pattern gibi)

### Benim Ekstra Gördüklerim

DRY ihlali (tekrar eden kodlar)
Domain modeling problemi
İndirim mantığının gerçek hayata uymaması

---

## Genel Değerlendirme

AI ve benim analizim büyük ölçüde örtüşüyor ancak odak noktaları farklı:

AI daha çok **design pattern ve mimari çözümler** üzerine odaklanıyor
Ben ise daha çok **temel hatalar ve iş mantığı (business logic)** tarafına odaklandım

Bu karşılaştırma, problemi daha geniş bir perspektiften görmemi sağladı ve eksik noktaları fark etmeme yardımcı oldu.
