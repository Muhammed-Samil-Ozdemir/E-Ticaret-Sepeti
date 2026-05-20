## Soru

"Adapter pattern burada uygun mu, yoksa Facade mı? Farkını açıkla."

## AI Yanıtı

Facade zaten mevcut — CartService tam olarak bu. Cart, PaymentService,
DiscountFactory üçlüsünü tek yüzey altında saklıyor. Yeni bir Facade açmak
için sistemde gizlenmesi gereken başka bir karmaşıklık katmanı olması gerekir,
şu an gerek yok.

Adapter ise farklı bir problemi çözer — arayüz uyumsuzluğu. Örneğin dışarıdan
bir ödeme kütüphanesi geldi ve IPaymentMethod arayüzüne uymuyorsa Adapter ile
sarılır. Bu kod tabanında dış kütüphane entegrasyonu olmadığı sürece Adapter
için gerçek bir neden yok.

Kısaca: Facade karmaşıklığı gizler, Adapter uyumsuzluğu çözer. Bu kod tabanında dış kütüphane entegrasyonu olmadığı sürece Adapter için gerçek bir neden yok. Facade ise zaten var, tekrar açmaya gerek yok.
