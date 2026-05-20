# Design Patterns — CartService Örneği

---

## 1. Factory Pattern — `DiscountFactory`

### Nerede
`DiscountFactory.create(amount, is_percentage)` → `Discount` nesnesi döner.
`Product` ve `CartService` bu factory'yi doğrudan kullanır.

### Neden
`Discount` nesnesini her ihtiyaç duyulan yerde `Discount(amount, is_percentage)` ile oluşturmak yerine,
üretim sorumluluğunu tek bir sınıfa delege ediyoruz.
İleride `PercentageDiscount`, `FlatDiscount` gibi alt türler gelirse sadece factory değişir;
çağıran kod dokunmadan kalır.

### Ne kazandın
| | Olmadan | Factory ile |
|---|---|---|
| Discount alt türü eklemek | Her `Product.set_discount()` çağrısını bul/değiştir | Sadece `factory.create()` içini genişlet |
| Test etmek | Tüm `Product` oluşturmak gerekir | Factory mock'lanır, bağımlılık izole olur |
| Nesne mantığı | Caller'a dağılmış | Tek yerde merkezi |

---

## 2. Strategy Pattern — `IPaymentMethod`

### Nerede
`IPaymentMethod` soyut arayüzü; `CreditCardPayment`, `PaypalPayment`, `BankTransferPayment` somut stratejileri.
`CartService.apply_payment_method(payment_method)` ile çalışma zamanında strateji atanır.

### Neden
Ödeme yöntemi ekleme/çıkarma işlemleri `CartService` veya `PaymentService`'e dokunmayı gerektirmemeli.
Her yeni ödeme yöntemi bağımsız bir sınıf olarak gelir, mevcut kod etkilenmez (Open/Closed Principle).

### Ne kazandın
| | Olmadan | Strategy ile |
|---|---|---|
| Yeni ödeme yöntemi | `PaymentService.pay()` içine `if/elif` ekle | Sadece yeni sınıf yaz, gerisi değişmez |
| Test | Tüm branch'leri aynı test altında zorla geç | Her strateji tamamen izole test edilir |
| Runtime seçim | Mümkün değil / hacky | `apply_payment_method()` ile temiz seçim |

---

## 3. Facade Pattern — `CartService`

### Nerede
`CartService`; `Cart`, `PaymentService`, `DiscountFactory`'yi tek bir arayüz altında sarar.
Dış dünya `CartService.add_product()`, `CartService.pay()` gibi basit metodlar görür.

### Neden
`Cart`, `PaymentService`, `DiscountFactory` üçlüsünü istemci kodun doğrudan bileşenlerle koordine etmesi karmaşık olurdu.
Facade bu koordinasyonu kapsüller; istemci subsystem'ın iç yapısını bilmek zorunda kalmaz.

### Ne kazandın
| | Olmadan | Facade ile |
|---|---|---|
| İstemci kodu | 3 nesneyi ayrı ayrı yönetir | 1 servis nesnesi yeterli |
| Subsystem değişimi | Her istemciyi güncelle | Sadece `CartService` içini güncelle |
| Karmaşıklık | Dışarı sızdı | CartService sınırında kaldı |

---

## 4. Bridge Pattern — `IPaymentMethod` × `IPaymentChannel`

### Nerede
`IPaymentMethod` artık bir `IPaymentChannel` referansı taşıyor.
`LiveChannel`, `SandboxChannel`, `MockChannel` somut implementasyonlar.
Ödeme yöntemi ve ortam runtime'da bağımsız olarak seçiliyor.

### Neden
Her ödeme yöntemi için her ortamda ayrı subclass açmak m × n sınıf patlaması yaratır.
Bridge ile iki hiyerarşi birbirinden ayrılır, composition ile birleştirilir.
`CartService` hiç değişmez.

### Ne kazandın
| | Olmadan | Bridge ile |
|---|---|---|
| Yeni ortam eklemek | Her ödeme sınıfına dokunmak gerekir | Sadece yeni Channel sınıfı yaz |
| Test ortamı | Gerçek API'ye istek gider | `MockChannel` inject et, ağ yok |
| Kombinasyon sayısı | m × n sınıf | m + n sınıf |

---

## 5. Decorator Pattern — `IProduct`

### Nerede
`Product` sınıfı `IProduct` arayüzünü implemente ediyor.
`LoggedProduct` ve `PremiumProduct` zincirlenerek sarılabiliyor:
`PremiumProduct(LoggedProduct(product))`.

### Neden
Ürün davranışı kombinasyonları compile-time'da bilinemez.
Subclass ile her kombinasyon için ayrı sınıf gerekirdi.
Decorator ile mevcut `Product` kodu dokunulmadan runtime'da davranış ekleniyor.

### Ne kazandın
| | Olmadan | Decorator ile |
|---|---|---|
| Yeni davranış eklemek | Product'a doğrudan yaz ya da subclass aç | Yeni dekoratör sınıfı yaz, zincire ekle |
| Kombinasyon | LoggedPremiumProduct, PremiumProduct... patlama | İstediğin kadar zincirle |
| Mevcut kod | Değişmek zorunda | Hiç dokunulmadı |

---

## Birlikte çalışma özeti

```
İstemci
  └─► CartService (Facade)
        ├─► Cart ──────────────────► IProduct (Decorator)
        │                                └─► Product
        │                                └─► LoggedProduct
        │                                └─► PremiumProduct
        │                                └─► DiscountFactory (Factory)
        └─► PaymentService
              └─► IPaymentMethod (Strategy + Bridge)
                    ├─ CreditCardPayment ──► IPaymentChannel
                    ├─ PaypalPayment         ├─ LiveChannel
                    └─ BankTransferPayment   ├─ SandboxChannel
                                            └─ MockChannel
```

Beş örüntü birbirini tamamlar:
- **Factory** nesne üretimini merkezileştirir.
- **Strategy** ödeme davranışını değiştirilebilir kılar.
- **Facade** karmaşıklığı dış dünyadan gizler.
- **Bridge** ödeme yöntemi ile ortamı birbirinden ayırır.
- **Decorator** ürünlere runtime'da davranış ekler.