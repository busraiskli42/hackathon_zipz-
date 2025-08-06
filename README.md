Zuzu ile Düşün, Zıpzıp ile Çöz
Proje Tanımı
"Zuzu ile Düşün, Zıpzıp ile Çöz", Down sendromlu çocuklar için tasarlanmış, iletişim ve problem çözme becerilerini geliştirmeyi amaçlayan etkileşimli bir web uygulamasıdır. Proje, çeşitli oyunlar ve aktiviteler aracılığıyla çocukların duygusal zekalarını, mantıksal düşünme yeteneklerini ve yaratıcılıklarını desteklemeyi hedefler.
Özellikler
İletişim Becerileri Modülleri: Kelime-resim eşleştirme, basit cümle kurma, duyguları tanıma ve selamlaşma/vedalaşma gibi aktiviteleri içerir.

Problem Çözme Becerileri Modülleri: Basit sorunları tanıma ve çözüm yolları üretme üzerine interaktif oyunlar sunar.

Çizim Tahtası: Çocukların hayal güçlerini kullanarak serbestçe çizim yapmalarına olanak tanır.

Kullanıcı Yönetimi: Ebeveynler için basit bir kayıt ve giriş sistemi mevcuttur.

Teknoloji Yığını
Ön Uç (Frontend):

HTML5: Sayfa yapısı ve içeriği oluşturmak için.

CSS3: Sayfa tasarımı ve görsel efektler için. style.css dosyası genel stil ayarlarını içerir.

JavaScript (Vanilla JS): Modüllerin interaktifliğini ve oyun mantığını yönetmek için.

Arka Uç (Backend):


MySQL: Kullanıcı bilgileri ve görevlerin durumunu saklamak için veritabanı olarak kullanılır.

Proje Yapısı
/
├── assets/                  # Projede kullanılan tüm resim ve ikonlar bu dizinde yer alır.
├── basit_cumleler.html      # "Basit Cümle Kurma" oyununun HTML dosyası.
├── basit_sorunlar.html      # "Basit Sorun Tanıma" oyununun HTML dosyası.
├── cizim_tahtasi.html       # "Çizim Tahtası" modülünün HTML dosyası.
├── cozum_yolu_uretme.html   # "Çözüm Yolu Üretme" oyununun HTML dosyası.
├── duygu.html               # "Duygularımı İfade Ediyorum" oyununun HTML dosyası.
├── iletisim.html            # "İletişim Becerileri" modüllerini listeleyen sayfa.
├── index.html               # Projenin ana giriş sayfası.
├── kelimeeslestirme.html    # "Kelime Resim Eşleştirme" oyununun HTML dosyası.
├── modules.html             # Tüm ana modülleri (İletişim, Problem Çözme vb.) listeleyen sayfa.
├── problemcozme.html        # "Problem Çözme Becerileri" modüllerini listeleyen sayfa.
├── selamlasma.html          # "Selamlaşma ve Vedalaşma" oyununun HTML dosyası.
├── script.js                # Ana sayfadaki (index.html) giriş ve yönlendirme mantığını yöneten JS dosyası.
├── kelimeeslestirme.js      # Kelime eşleştirme oyununun mantığını içeren JS dosyası.
├── style.css                # Projenin genel stil ayarları.

Kurulum ve Kullanım
XAMPP uygulamasında APACHE ve MYSQL start verin.Sonra MYSQL de admin e tıklayın.

Dosyaları Kopyalayın: Tüm proje dosyalarını web sunucunuzun htdocs (XAMPP için) veya www (WAMP için) klasörüne kopyalayın.

Veritabanını Oluşturun:

phpMyAdmin gibi bir araç kullanarak zuzu.db adında yeni bir veritabanı oluşturun.

Aşağıdaki SQL sorgularını kullanarak gerekli tabloları oluşturun ve örnek verileri ekleyin:

-- `zuzu_db` adında bir veritabanı oluşturun
CREATE DATABASE cocuk_oyunu;

-- Veritabanını seçin
USE zuzu_db;

-- `users` tablosunu oluşturun
-- Bu tablo, ebeveynlerin giriş bilgilerini tutar.
CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(250),
     email VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Uygulamayı Çalıştırın:

Python arka ucunuzu başlatmak için terminalde app.py dosyanızın olduğu dizinde:

Bash

python app.py
Ardından, tarayıcınızda http://localhost:[Flask_port]/index.html (varsayılan Flask portu 5000'dir, yani http://localhost:5000/index.html) adresini ziyaret edin.Giriş Yapın: Uygulamanın ana sayfasından "Başla" butonuna tıklayarak giriş sayfasına gidin. Kayıt olup kullanıcı adı ve şifreyle giriş yapabilirsiniz
