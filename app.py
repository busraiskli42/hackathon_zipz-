from flask import Flask, render_template, send_from_directory, request, jsonify, redirect, url_for
import base64
import os
import openai
import mysql.connector
from PIL import Image
import io
import json

# Flask uygulamasını başlatıyoruz.
app = Flask(__name__, template_folder='zıpzu', static_folder='zıpzu')

# OpenAI API anahtarını ortam değişkeninden al
openai.api_key = os.getenv("OPENAI_API_KEY")

# Veritabanı bağlantı ayarları
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'zuzu_db'
}

# Veritabanı bağlantısını kuran fonksiyon
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Veritabanına bağlanılamadı: {err}")
        return None

# Ana sayfa (/) isteği geldiğinde çalışacak fonksiyon
@app.route('/')
def index():
    return render_template('index.html')

# CSS, JS ve diğer statik dosyalar için rota
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('zıpzu', filename)

# API endpoint'i: "Başla" butonuna basıldığında buraya POST isteği gelecek
@app.route('/api/start_education', methods=['POST'])
def start_education():
    print("---------------------------------------------")
    print("PYTHON TARAFINDA: Eğitime başlama isteği alındı!")
    print("---------------------------------------------")
    return jsonify({"message": "Eğitim başlatıldı!"})

# İletişim Becerileri sayfası için rota
@app.route('/iletisim.html')
def iletisim_becerileri_page():
    return render_template('iletisim.html')

# Problem Çözme Becerileri sayfası için rota
@app.route('/problemcozme.html')
def problem_cozme_becerileri_page():
    return render_template('problemcozme.html')

# "Basit Cümle Kurma" sayfası için yeni rota
@app.route('/basit_cumleler.html')
def basit_cumleler_page():
    return render_template('basit_cumleler.html')

# "Basit Sorun Tanıma" sayfası için yeni rota
@app.route('/basit_sorunlar.html')
def basit_sorunlar_page():
    return render_template('basit_sorunlar.html') 

@app.route('/duygu.html')
def duygu_page():
    return render_template('duygu.html')

@app.route('/cozum_yolu_uretme.html')
def cozum_yolu_uretme_page():
    return render_template('cozum_yolu_uretme.html')

# YENİ ROTA: Çizim tahtası sayfasını gösterir
@app.route('/cizim_tahtasi.html')
def cizim_tahtasi_page():
    return render_template('cizim_tahtasi.html')

# YENİ API ENDPOINT: Çizim analizini yapar ve yapay zekadan geri bildirim alır
@app.route('/api/analyze_drawing', methods=['POST'])
def analyze_drawing():
    data = request.json
    image_data_url = data.get('image')

    if not image_data_url:
        return jsonify({"success": False, "error": "Resim verisi bulunamadı."}), 400

    try:
        header, encoded = image_data_url.split(",", 1)
        image_bytes = base64.b64decode(encoded)

        prompt = "Bu resimde ne olduğunu tahmin et. Bunu bir çocuğa dostane, teşvik edici bir dille açıkla. Tahmininin ardından 'Şimdi ne çizebiliriz?' gibi bir soruyla devam et."
        
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_data_url}}
                ]}
            ],
            max_tokens=300
        )
        
        ai_response = response.choices[0].message.content
        return jsonify({"success": True, "prediction": ai_response})

    except Exception as e:
        print(f"Hata: {e}")
        return jsonify({"success": False, "error": f"Analiz sırasında bir hata oluştu: {str(e)}"}), 500

# Kayıt sayfası için rota
@app.route('/kayit.html')
def kayit_page():
    return render_template('kayit.html')

# Kullanıcı kayıt işlemi için API endpoint'i
@app.route('/register', methods=['POST'])
def register():
    # Form verilerini al ve boşlukları temizle
    username = request.form['username'].strip()
    email = request.form['email'].strip()
    password = request.form['password'].strip() # Güvenlik uyarısı: Gerçek uygulamalarda şifreler hashlenmelidir!

    conn = get_db_connection()
    if conn is None:
        return redirect(url_for('kayit_page', status='error', message='Veritabanı bağlantı hatası.'))

    try:
        cursor = conn.cursor()
        
        # Kullanıcı adının veya e-postanın zaten var olup olmadığını kontrol et
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if cursor.fetchone():
            return redirect(url_for('kayit_page', status='error', message='Kullanıcı adı veya e-posta zaten kullanılıyor.'))
        
        # Yeni kullanıcıyı veritabanına ekle
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, password))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        # Başarılı kayıt sonrası kayit.html sayfasına yönlendirme yap
        return redirect(url_for('kayit_page', status='success'))

    except mysql.connector.Error as err:
        print(f"Veritabanı hatası (kayıt): {err}")
        return redirect(url_for('kayit_page', status='error', message='Kayıt sırasında bir hata oluştu.'))

# Kullanıcı giriş işlemi için API endpoint'i
@app.route('/login', methods=['POST'])
def login():
    # Form verilerini al ve boşlukları temizle
    username = request.form['username'].strip()
    password = request.form['password'].strip() # Güvenlik uyarısı: Gerçek uygulamalarda şifreler hashlenmelidir!

    conn = get_db_connection()
    if conn is None:
        return redirect(url_for('index', status='login_error', message='Veritabanı bağlantı hatası.'))

    try:
        cursor = conn.cursor()
        # Kullanıcıyı kullanıcı adı ve şifre ile bul
        # ÖNEMLİ: Şifreler hashlenmişse, burada check_password_hash gibi bir fonksiyon kullanılmalıdır.
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            # Giriş başarılıysa, ana sayfaya veya modül sayfalarına yönlendir
            return redirect(url_for('index', status='login_success'))
        else:
            # Giriş başarısızsa hata mesajı ile ana sayfaya yönlendir
            return redirect(url_for('index', status='login_error', message='Geçersiz kullanıcı adı veya şifre.'))

    except mysql.connector.Error as err:
        print(f"Veritabanı hatası (giriş): {err}")
        return redirect(url_for('index', status='login_error', message='Giriş sırasında bir hata oluştu.'))

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)
