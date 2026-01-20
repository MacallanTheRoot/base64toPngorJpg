<div align="center">
  <a href="#en">🇺🇸 English</a> | <a href="#tr">🇹🇷 Türkçe</a>
</div>

<a name="en"></a>
# 🖼️ Base64 to PNG/JPG Converter
### Professional Base64 Image Encoder & Decoder with GUI

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)

---

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Developer](#developer)

---

## 🎯 Description

**Base64 to PNG/JPG Converter** is a **professional** Base64 image encoding/decoding tool designed for web developers, data analysts, and security researchers.

Convert Base64 codes to image files or encode your images to Base64 format with a modern and user-friendly PyQt5 interface. Speed up your workflow with Drag & Drop support, history tracking, and live preview features.

---

## ⚡ Features

### 1. **🔄 Bidirectional Conversion**
- **Base64 → Image**: Convert Base64 code to PNG, JPG, GIF, BMP formats
- **Image → Base64**: Encode image files to Base64 format
- Automatic format detection (PNG, JPEG, GIF, BMP)
- Data URI prefix support (`data:image/png;base64,`)

### 2. **🎨 Modern GUI Interface**
- **PyQt5** based professional interface
- Modern dark theme design
- Responsive layout (window size adaptive)
- Intuitive controls for easy use

### 3. **📂 Drag & Drop Support**
- Upload image files with drag and drop
- Fast Base64 conversion
- Multiple file format support (PNG, JPG, JPEG, GIF, BMP)

### 4. **👁️ Live Preview**
- Automatic preview while pasting Base64 code
- Thumbnail generation (300x300px)
- Invalid code detection
- Debugging messages

### 5. **📜 History Management**
- History of all converted codes
- Timestamp recording
- One-click copy feature
- Easy access via hamburger menu

### 6. **💾 File Saving**
- Save in original format (PNG, JPG, GIF, BMP)
- Custom filename specification
- File path selection
- Success/error notifications

### 7. **🔐 Data Security**
- Local processing (no internet required)
- Data security (no external server)
- Offline operation support

---

## 🚀 Installation

### Requirements

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **PyQt5**: GUI framework
- **Pillow**: Image processing library

### Step 1: Clone the Repository

```bash
git clone https://github.com/MacallanTheRoot/base64toPngorJpg.git
cd base64toPngorJpg
```

### Step 2: Install Dependencies

#### Windows Users:
```bash
requiertments.bat
```

#### Linux/Mac Users:
```bash
pip install --upgrade pip
pip install --upgrade Pillow
pip install --upgrade PyQt5
pip install --upgrade pyqt5-tools
```

or

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python base64topng.py
```

---

## 📖 Usage

### 1️⃣ Base64 → Image Conversion

1. Launch the application: `python base64topng.py`
2. Paste the Base64 code into the upper text box
3. You will see automatic preview
4. Click the **"Download"** button
5. Choose filename and location
6. Your image file will be saved (PNG/JPG/GIF/BMP)

### 2️⃣ Image → Base64 Conversion

#### Method A: Drag & Drop
1. Drag the image file to the **"Drop image here"** area
2. Base64 code automatically appears in the upper box
3. Copy and use the code

#### Method B: File Selection
1. Click the **"Convert Image to Base64"** button
2. Select the image file with the file picker
3. Base64 code is automatically generated

### 3️⃣ Using History

1. Click the **hamburger menu (≡)** in the upper left
2. View previous conversion operations
3. Copy Base64 code with the **"Copy"** button
4. Click the hamburger again to close the history menu

> **Note:** History data is deleted when the application is closed (stored in RAM).

---

## 🛠️ Technical Details

### Used Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **PyQt5** | 5.15+ | GUI interface and widgets |
| **Pillow (PIL)** | 9.0+ | Image processing and format conversion |
| **Base64** | Built-in | Base64 encode/decode operations |

### Supported Image Formats

- **PNG** (Portable Network Graphics)
- **JPEG/JPG** (Joint Photographic Experts Group)
- **GIF** (Graphics Interchange Format)
- **BMP** (Bitmap Image File)

### Format Detection Mechanism

The application performs automatic format detection based on the starting characters of the Base64 code:

```python
# PNG: starts with iVBOR (Base64)
# JPEG: starts with /9j/ (Base64)
# GIF: starts with R0lGOD (Base64)
```

### Architecture

```
base64topng.py
├── MainWindow (QWidget)
│   ├── text_input (QTextEdit) - Base64 input
│   ├── preview_label (QLabel) - Image preview
│   ├── drop_label (QLabel) - Drag & Drop area
│   └── hamburger_btn (QPushButton) - History menu trigger
│
└── HistoryMenu (QWidget)
    ├── scroll (QScrollArea) - History list
    └── add_history() - Add to history function
```

### Code Features

- **Event-Driven Architecture**: PyQt5 signal/slot system
- **Drag & Drop**: `dragEnterEvent` and `dropEvent` implementation
- **Memory Management**: Image processing in RAM using BytesIO
- **Error Handling**: Safe operations with try-except blocks
- **UI/UX**: Responsive design and hover effects

---

## 🎯 Use Cases

### **Scenario 1: Web Development**
```
Problem: You want to embed small icons in HTML/CSS.
Solution: Convert PNG icons to Base64 and use as <img src="data:image/png;base64,...">
```

### **Scenario 2: Data Analysis**
```
Problem: You want to verify Base64 images coming from API.
Solution: Paste the Base64 code, verify by preview and download as PNG.
```

### **Scenario 3: Email Template**
```
Problem: You want to embed images in email templates.
Solution: Convert images to Base64 and use inline.
```

### **Scenario 4: Forensics & OSINT**
```
Problem: You want to extract Base64 images found in web sources (HTML/JS).
Solution: Copy the code, paste into application and save as PNG/JPG.
```

---

## ⚠️ Disclaimer

> **This application is developed for EDUCATION, RESEARCH and LEGAL PURPOSES only.**

Converting or distributing copyrighted images without permission may constitute a crime. Users must ensure they have legal rights to the data they process.

The developer (**MacallanTheRoot**) is not responsible for any legal and financial consequences arising from misuse of this software.

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Hamza Efe Şahinbaş (MacallanTheRoot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**MacallanTheRoot**  
*Cybersecurity Researcher & Software Developer*

- 🌐 **GitHub:** [https://github.com/MacallanTheRoot](https://github.com/MacallanTheRoot)
- 🔐 **Expertise:** OSINT, Malware Analysis, Python Development
- 🛡️ **Other Projects:**
  - [AmateurOSINT](https://github.com/MacallanTheRoot/AmateurOSINT) - Professional OSINT Platform
  - [Aslan-Bey-OPSEC](https://github.com/MacallanTheRoot/Aslan-Bey-OPSEC) - Metadata Sanitization Tool
  - [Blue-Team-Toolkit](https://github.com/MacallanTheRoot/Blue-Team-Toolkit) - Cybersecurity Defense Platform
  - [Red-Team-Toolkit](https://github.com/MacallanTheRoot/Red-Team-Toolkit) - Adversary Emulation Suite

---

## 🚀 Future Features (Roadmap)

- [ ] Batch conversion support
- [ ] Image compression options
- [ ] EXIF metadata preservation/removal
- [ ] SVG format support
- [ ] CLI (Command Line Interface) mode
- [ ] Encryption/Decryption features
- [ ] Cloud storage integration (optional)
- [ ] JSON/XML base64 parsing support

---

## 🤝 Contributing

We welcome your contributions! Feel free to submit a pull request.

1. Fork it
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Contact & Support

- **Bug Report:** Use GitHub Issues
- **Feature Request:** Use GitHub Discussions
- **Email:** Contact via repository

---

<div align="center">

### ⭐ Don't forget to star the project if you like it!

**Base64 to PNG/JPG Converter** - Powered by **MacallanTheRoot**

*"Simplicity is the ultimate sophistication."*

</div>

<br>
<br>
<br>

---

<a name="tr"></a>
# 🖼️ Base64 to PNG/JPG Converter
### GUI ile Profesyonel Base64 Görsel Kodlayıcı & Çözücü

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)

---

## 📋 İçindekiler

- [Açıklama](#açıklama)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Teknik Detaylar](#teknik-detaylar)
- [Yasal Uyarı](#yasal-uyarı)
- [Lisans](#lisans)
- [Geliştirici](#geliştirici)

---

## 🎯 Açıklama

**Base64 to PNG/JPG Converter**, web geliştiricileri, veri analisti ve güvenlik araştırmacıları için tasarlanmış **profesyonel** bir Base64 görsel kodlama/çözme aracıdır.

Modern ve kullanıcı dostu PyQt5 arayüzü ile Base64 kodlarını görsel dosyalara dönüştürün veya görsellerinizi Base64 formatına kodlayın. Drag & Drop desteği, geçmiş takibi ve canlı önizleme özellikleriyle iş akışınızı hızlandırın.

---

## ⚡ Özellikler

### 1. **🔄 Çift Yönlü Dönüştürme**
- **Base64 → Görsel**: Base64 kodunu PNG, JPG, GIF, BMP formatlarına dönüştürün
- **Görsel → Base64**: Görsel dosyalarını Base64 formatına kodlayın
- Otomatik format algılama (PNG, JPEG, GIF, BMP)
- Data URI prefix desteği (`data:image/png;base64,`)

### 2. **🎨 Modern GUI Arayüzü**
- **PyQt5** tabanlı profesyonel arayüz
- Modern karanlık tema tasarımı
- Responsive layout (pencere boyutu uyumlu)
- Kolay kullanım için sezgisel kontroller

### 3. **📂 Drag & Drop Desteği**
- Görsel dosyalarını sürükle-bırak ile yükleyin
- Hızlı Base64 dönüştürme
- Çoklu dosya formatı desteği (PNG, JPG, JPEG, GIF, BMP)

### 4. **👁️ Canlı Önizleme**
- Base64 kodunu yapıştırırken otomatik önizleme
- Thumbnail oluşturma (300x300px)
- Geçersiz kod tespiti
- Hata ayıklama mesajları

### 5. **📜 Geçmiş (History) Yönetimi**
- Dönüştürülen tüm kodların geçmişi
- Zaman damgası ile kayıt
- Tek tıkla kopyalama özelliği
- Hamburger menü ile kolay erişim

### 6. **💾 Dosya Kaydetme**
- Orijinal formatta kaydetme (PNG, JPG, GIF, BMP)
- Özel dosya adı belirleme
- Dosya yolu seçimi
- Başarı/hata bildirimleri

### 7. **🔐 Veri Güvenliği**
- Yerel işleme (internet gerektirmez)
- Veri güvenliği (harici sunucu yok)
- Offline çalışma desteği

---

## 🚀 Kurulum

### Gereksinimler

- **Python**: 3.8 veya üstü
- **pip**: Python paket yöneticisi
- **PyQt5**: GUI framework
- **Pillow**: Görsel işleme kütüphanesi

### Adım 1: Repository'yi Clone Et

```bash
git clone https://github.com/MacallanTheRoot/base64toPngorJpg.git
cd base64toPngorJpg
```

### Adım 2: Bağımlılıkları Yükle

#### Windows Kullanıcıları:
```bash
requiertments.bat
```

#### Linux/Mac Kullanıcıları:
```bash
pip install --upgrade pip
pip install --upgrade Pillow
pip install --upgrade PyQt5
pip install --upgrade pyqt5-tools
```

veya

```bash
pip install -r requirements.txt
```

### Adım 3: Uygulamayı Çalıştır

```bash
python base64topng.py
```

---

## 📖 Kullanım

### 1️⃣ Base64 → Görsel Dönüştürme

1. Uygulamayı başlatın: `python base64topng.py`
2. Base64 kodunu üst metin kutusuna yapıştırın
3. Otomatik önizleme göreceksiniz
4. **"İndir"** butonuna tıklayın
5. Dosya adı ve konum seçin
6. Görsel dosyanız kaydedilir (PNG/JPG/GIF/BMP)

### 2️⃣ Görsel → Base64 Dönüştürme

#### Yöntem A: Sürükle-Bırak
1. Görsel dosyayı **"Buraya fotoğraf sürükleyip bırakın"** alanına sürükleyin
2. Base64 kodu otomatik olarak üst kutuda görünür
3. Kodu kopyalayıp kullanın

#### Yöntem B: Dosya Seçimi
1. **"Fotoğrafı Base64'e Dönüştür"** butonuna tıklayın
2. Dosya seçici ile görsel dosyayı seçin
3. Base64 kodu otomatik oluşturulur

### 3️⃣ Geçmiş Kullanımı

1. Sol üstteki **hamburger menüsüne (≡)** tıklayın
2. Önceki dönüştürme işlemlerini görün
3. **"Kopyala"** butonu ile Base64 kodunu kopyalayın
4. Geçmiş menüsünü kapatmak için tekrar hamburger'e tıklayın

> **Not:** Geçmiş veriler, uygulama kapatıldığında silinir (RAM'de tutulur).

---

## 🛠️ Teknik Detaylar

### Kullanılan Kütüphaneler

| Kütüphane | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| **PyQt5** | 5.15+ | GUI arayüzü ve widget'lar |
| **Pillow (PIL)** | 9.0+ | Görsel işleme ve format dönüştürme |
| **Base64** | Built-in | Base64 encode/decode işlemleri |

### Desteklenen Görsel Formatları

- **PNG** (Portable Network Graphics)
- **JPEG/JPG** (Joint Photographic Experts Group)
- **GIF** (Graphics Interchange Format)
- **BMP** (Bitmap Image File)

### Format Algılama Mekanizması

Uygulama, Base64 kodunun başlangıç karakterlerine göre otomatik format tespiti yapar:

```python
# PNG: iVBOR ile başlar (Base64)
# JPEG: /9j/ ile başlar (Base64)
# GIF: R0lGOD ile başlar (Base64)
```

### Mimari Yapı

```
base64topng.py
├── MainWindow (QWidget)
│   ├── text_input (QTextEdit) - Base64 girişi
│   ├── preview_label (QLabel) - Görsel önizleme
│   ├── drop_label (QLabel) - Drag & Drop alanı
│   └── hamburger_btn (QPushButton) - Geçmiş menüsü tetikleyici
│
└── HistoryMenu (QWidget)
    ├── scroll (QScrollArea) - Geçmiş listesi
    └── add_history() - Geçmişe ekleme fonksiyonu
```

### Kod Özellikleri

- **Event-Driven Architecture**: PyQt5 signal/slot sistemi
- **Drag & Drop**: `dragEnterEvent` ve `dropEvent` implementasyonu
- **Memory Management**: BytesIO kullanarak RAM'de görsel işleme
- **Error Handling**: Try-except blokları ile güvenli işlem
- **UI/UX**: Responsive tasarım ve hover efektleri

---

## 🎯 Kullanım Senaryoları

### **Senaryo 1: Web Geliştirme**
```
Problem: HTML/CSS'de küçük ikonları embed etmek istiyorsunuz.
Çözüm: PNG ikonları Base64'e çevirin ve <img src="data:image/png;base64,..."> olarak kullanın.
```

### **Senaryo 2: Veri Analizi**
```
Problem: API'den gelen Base64 görselini doğrulamak istiyorsunuz.
Çözüm: Base64 kodunu yapıştırın, önizleyerek doğrulayın ve PNG olarak indirin.
```

### **Senaryo 3: Email Template**
```
Problem: Email şablonunda görsel embed etmek istiyorsunuz.
Çözüm: Görseli Base64'e çevirin ve inline olarak kullanın.
```

### **Senaryo 4: Forensics & OSINT**
```
Problem: Web kaynağında (HTML/JS) bulunan Base64 görselini çıkarmak istiyorsunuz.
Çözüm: Kodu kopyalayın, uygulamaya yapıştırın ve PNG/JPG olarak kaydedin.
```

---

## ⚠️ Yasal Uyarı

> **Bu uygulama sadece EĞİTİM, ARAŞTIRMA ve YASAL AMAÇLAR için geliştirilmiştir.**

Telif hakkı olan görselleri izinsiz dönüştürmek veya dağıtmak suç teşkil edebilir. Kullanıcılar, işledikleri verilerin yasal kullanım haklarına sahip olduklarından emin olmalıdır.

Geliştirici (**MacallanTheRoot**), bu yazılımın kötüye kullanımından doğacak yasal ve maddi sonuçlardan sorumlu değildir.

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır.

```
MIT License

Copyright (c) 2025 Hamza Efe Şahinbaş (MacallanTheRoot)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Geliştirici

**MacallanTheRoot**  
*Siber Güvenlik Araştırmacısı & Yazılım Geliştirici*

- 🌐 **GitHub:** [https://github.com/MacallanTheRoot](https://github.com/MacallanTheRoot)
- 🔐 **Uzmanlık:** OSINT, Malware Analysis, Python Development
- 🛡️ **Diğer Projeler:**
  - [AmateurOSINT](https://github.com/MacallanTheRoot/AmateurOSINT) - Professional OSINT Platform
  - [Aslan-Bey-OPSEC](https://github.com/MacallanTheRoot/Aslan-Bey-OPSEC) - Metadata Sanitization Tool
  - [Blue-Team-Toolkit](https://github.com/MacallanTheRoot/Blue-Team-Toolkit) - Cybersecurity Defense Platform
  - [Red-Team-Toolkit](https://github.com/MacallanTheRoot/Red-Team-Toolkit) - Adversary Emulation Suite

---

## 🚀 Gelecek Özellikler (Roadmap)

- [ ] Toplu (Batch) dönüştürme desteği
- [ ] Görsel sıkıştırma seçenekleri
- [ ] EXIF metadata koruma/kaldırma
- [ ] SVG format desteği
- [ ] CLI (Command Line Interface) modu
- [ ] Şifreleme/Decryption özellikleri
- [ ] Cloud storage entegrasyonu (opsiyonel)
- [ ] JSON/XML base64 parse desteği

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

---

## 📞 İletişim & Destek

- **Bug Report:** GitHub Issues kullanın
- **Feature Request:** GitHub Discussions kullanın
- **Email:** Repository üzerinden iletişime geçin

---

<div align="center">

### ⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Base64 to PNG/JPG Converter** - Powered by **MacallanTheRoot**

*"Simplicity is the ultimate sophistication."*

</div>
