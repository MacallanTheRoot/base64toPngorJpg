import sys
import base64
import os
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton,
    QFileDialog, QMessageBox, QScrollArea, QFrame, QPlainTextEdit
)
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import Qt
from PIL import Image
from io import BytesIO

class HistoryMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background: rgba(20,20,20,210);")
        self.setVisible(False)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Başlık
        title = QLabel("Geçmiş (Uygulama yeniden başlatıldığında geçmiş silinir.)")
        title.setStyleSheet("""
            color: #FAFAFA;
            font-weight: bold;
            font-size: 18pt;
            padding: 24px 0 12px 0;
        """)
        title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.main_layout.addWidget(title)

        # Scroll alanı
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("background: transparent; border: none;")
        self.inner = QWidget()
        self.inner_layout = QVBoxLayout(self.inner)
        self.inner_layout.setAlignment(Qt.AlignTop)
        self.inner_layout.setContentsMargins(24, 0, 24, 24)
        self.inner_layout.setSpacing(12)
        self.scroll.setWidget(self.inner)
        self.main_layout.addWidget(self.scroll)
        self.history = []

    def add_history(self, code, timestamp, filename=None):
        entry = QFrame()
        entry.setStyleSheet("""
            QFrame {
                background-color: #23272e;
                border-radius: 12px;
                min-height: 48px;
                max-height: 90px;
            }
        """)
        v = QVBoxLayout(entry)
        v.setContentsMargins(14, 8, 14, 8)
        v.setSpacing(6)

        code_edit = QPlainTextEdit()
        code_edit.setReadOnly(True)
        code_edit.setPlainText(code)
        code_edit.setStyleSheet("""
            background: #181c20;
            color: #5FCDD9;
            border: none;
            font-family: Consolas;
            font-size: 10pt;
        """)
        code_edit.setFixedHeight(44)
        code_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        code_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        v.addWidget(code_edit)

        h = QHBoxLayout()
        btn = QPushButton("Kopyala")
        btn.setStyleSheet("""
            QPushButton {
                background: #04BFAD; color: #222831; font-weight: bold;
                border: none; border-radius: 4px; font-size: 10pt; padding: 2px 16px;
            }
            QPushButton:hover { background: #04BF9D; }
        """)
        btn.setCursor(Qt.PointingHandCursor)
        btn.clicked.connect(lambda _, c=code: QApplication.instance().clipboard().setText(c))
        h.addWidget(btn, alignment=Qt.AlignLeft)

        # Dosya ismi
        if filename:
            file_lbl = QLabel(f"Dosya ismi: {filename}")
            file_lbl.setStyleSheet("color: #aaaaaa; font-style: italic; font-size: 9pt;")
            h.addWidget(file_lbl, alignment=Qt.AlignLeft)

        h.addStretch()
        time_lbl = QLabel(timestamp)
        time_lbl.setStyleSheet("color: #aaaaaa; font-style: italic; font-size: 9pt;")
        h.addWidget(time_lbl, alignment=Qt.AlignRight)
        v.addLayout(h)

        self.inner_layout.insertWidget(0, entry)
        self.history.append((code, timestamp))

    def clear_history(self):
        while self.inner_layout.count():
            child = self.inner_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.history.clear()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base64 → Görsel Dönüştürücü")
        self.setMinimumSize(500, 700)
        self.setStyleSheet("background-color: #172026;")
        self.history_menu = HistoryMenu(self)

        # Hamburger butonu
        self.hamburger_btn = QPushButton("≡", self)
        self.hamburger_btn.setFixedSize(44, 44)
        self.hamburger_btn.setStyleSheet("""
            QPushButton {
                background: #04BFAD; color: #172026; font-size: 22pt; font-weight: bold;
                border: none; border-radius: 8px;
            }
            QPushButton:hover { background: #04BF9D; }
        """)
        self.hamburger_btn.setCursor(Qt.PointingHandCursor)
        self.hamburger_btn.move(20, 20)
        self.hamburger_btn.clicked.connect(self.toggle_history_menu)

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.content = QWidget()
        self.content.setStyleSheet("background: transparent;")
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.main_layout.addWidget(self.content)

        # Üst bar (başlık)
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(64, 20, 20, 10)
        top_bar.setSpacing(0)
        lbl = QLabel("📄 Base64 kodunu buraya yapıştır:")
        lbl.setStyleSheet("""
            color: #5FCDD9; background: #172026; font-weight: bold; font-size: 13pt;
            padding-left: 24px; padding-right: 24px;
        """)
        lbl.setAlignment(Qt.AlignCenter)
        top_bar.addWidget(lbl, stretch=1, alignment=Qt.AlignCenter)
        self.content_layout.addLayout(top_bar)

        # Base64 input
        self.text_input = QTextEdit()
        self.text_input.setStyleSheet("""
            background: #172026; color: #5FCDD9; border: 2px solid #04BFAD;
            font-family: Consolas; font-size: 10pt; border-radius: 6px;
        """)
        self.text_input.setFixedHeight(120)
        self.text_input.textChanged.connect(self.preview_base64_image)
        self.content_layout.addWidget(self.text_input)
        self.content_layout.addSpacing(10)

        # --- Butonlar (Ortalanmış) ---
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btn_preview = QPushButton("Dönüştür (Önizle)")
        self.btn_download = QPushButton("İndir")
        for btn in (self.btn_preview, self.btn_download):
            btn.setStyleSheet("""
                QPushButton {
                    background: #04BFAD; color: #172026; font-weight: bold;
                    border: none; border-radius: 6px; font-size: 10pt; padding: 8px 18px;
                }
                QPushButton:hover { background: #04BF9D; }
            """)
            btn.setCursor(Qt.PointingHandCursor)
        self.btn_preview.clicked.connect(self.preview_base64_image)
        self.btn_download.clicked.connect(self.download_image)
        btn_row.addWidget(self.btn_preview)
        btn_row.addWidget(self.btn_download)
        btn_row.addStretch()
        btn_frame = QWidget()
        btn_frame.setLayout(btn_row)
        btn_frame.setStyleSheet("background: #027373; border-radius: 8px;")
        btn_frame.setContentsMargins(30, 0, 30, 0)
        self.content_layout.addWidget(btn_frame)
        self.content_layout.addSpacing(10)

        # Önizleme alanı
        self.preview_label = QLabel("Önizleme yok")
        self.preview_label.setStyleSheet("""
            background: #172026; color: #5FCDD9; font-style: italic; font-size: 10pt;
            border: 2px groove #04BFAD; border-radius: 8px;
        """)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setFixedHeight(440)
        self.content_layout.addWidget(self.preview_label)
        self.content_layout.addSpacing(10)

        # Sürükle bırak alanı
        self.drop_label = QLabel("Buraya fotoğraf sürükleyip bırakın")
        self.drop_label.setStyleSheet("""
            background: #172026; color: #5FCDD9; font-style: italic; font-size: 10pt;
            border: 2px groove #04BFAD; border-radius: 8px;
        """)
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setFixedHeight(100)
        self.content_layout.addWidget(self.drop_label)
        self.content_layout.addSpacing(10)
        self.drop_label.setAcceptDrops(True)

        # Fotoğrafı Base64'e Dönüştür butonu
        self.btn_img2b64 = QPushButton("Fotoğrafı Base64'e Dönüştür")
        self.btn_img2b64.setStyleSheet("""
            QPushButton {
                background: #04BFAD; color: #172026; font-weight: bold;
                border: none; border-radius: 6px; font-size: 10pt; padding: 8px 18px;
            }
            QPushButton:hover { background: #04BF9D; }
        """)
        self.btn_img2b64.setCursor(Qt.PointingHandCursor)
        self.btn_img2b64.clicked.connect(self.image_to_base64)
        self.content_layout.addWidget(self.btn_img2b64)
        self.content_layout.addSpacing(20)

        self.content_layout.addStretch()

        # Alt bilgi alanı
        footer_widget = QWidget()
        footer_layout = QVBoxLayout(footer_widget)
        footer_layout.setContentsMargins(0, 10, 0, 20)
        footer_layout.setSpacing(2)

        author_label = QLabel("MacallanTheRoot")
        author_label.setStyleSheet("color: #5FCDD9; font-size: 11pt; font-weight: bold;")
        author_label.setAlignment(Qt.AlignHCenter)
        footer_layout.addWidget(author_label)

        github_label = QLabel('<a href="https://github.com/MacallanTheRoot/">https://github.com/MacallanTheRoot/</a>')
        github_label.setStyleSheet("color: #04BFAD; font-size: 10pt;")
        github_label.setAlignment(Qt.AlignHCenter)
        github_label.setOpenExternalLinks(True)
        footer_layout.addWidget(github_label)

        self.content_layout.addWidget(footer_widget)

        self.setAcceptDrops(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Hamburger menü ve geçmiş menüsünü tam ekran yap
        self.history_menu.setGeometry(0, 0, self.width(), self.height())
        self.hamburger_btn.raise_()

    def toggle_history_menu(self):
        if self.history_menu.isVisible():
            self.history_menu.setVisible(False)
        else:
            self.history_menu.setGeometry(0, 0, self.width(), self.height())
            self.history_menu.setVisible(True)
            self.history_menu.raise_()
            self.hamburger_btn.raise_()

    def add_to_history(self, b64_code):
        # Aynı kodu tekrar ekleme
        if any(b64_code == c for c, _ in self.history_menu.history):
            return
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history_menu.add_history(b64_code, timestamp)

    def preview_base64_image(self):
        b64_data = self.text_input.toPlainText().strip()
        if not b64_data:
            self.preview_label.setText("Önizleme yok")
            self.preview_label.setPixmap(QPixmap())
            return
        try:
            image_bytes, _ = self.decode_base64_to_image(b64_data)
            img = Image.open(BytesIO(image_bytes))
            img.thumbnail((300, 300))
            buf = BytesIO()
            img.save(buf, format="PNG")
            qt_img = QImage.fromData(buf.getvalue())
            pixmap = QPixmap.fromImage(qt_img)
            self.preview_label.setPixmap(pixmap)
            self.preview_label.setText("")
            self.add_to_history(b64_data)
        except Exception:
            self.preview_label.setText("Geçersiz Base64")
            self.preview_label.setPixmap(QPixmap())

    def download_image(self):
        b64_data = self.text_input.toPlainText().strip()
        if not b64_data:
            QMessageBox.warning(self, "Uyarı", "Lütfen Base64 kodunu girin.")
            return
        try:
            image_bytes, ext = self.decode_base64_to_image(b64_data)
            output_path, _ = QFileDialog.getSaveFileName(self, "Kaydet", f"base64_output.{ext}", f"*.{ext}")
            if output_path:
                with open(output_path, "wb") as img_file:
                    img_file.write(image_bytes)
                QMessageBox.information(self, "Başarılı", f"Görsel kaydedildi:\n{output_path}")
                self.add_to_history(b64_data)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"İndirme sırasında hata oluştu:\n{e}")

    def image_to_base64(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Bir görsel seçin", "", "Görsel Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif);;Tüm Dosyalar (*)")
        if not file_path:
            return
        try:
            with open(file_path, "rb") as img_file:
                img_bytes = img_file.read()
                ext = os.path.splitext(file_path)[1].lower()
                if ext == ".png":
                    prefix = "data:image/png;base64,"
                elif ext in [".jpg", ".jpeg"]:
                    prefix = "data:image/jpeg;base64,"
                elif ext == ".gif":
                    prefix = "data:image/gif;base64,"
                elif ext == ".bmp":
                    prefix = "data:image/bmp;base64,"
                else:
                    prefix = "data:image/unknown;base64,"
                b64_str = base64.b64encode(img_bytes).decode("utf-8")
                self.text_input.setPlainText(prefix + b64_str)
                self.add_to_history(prefix + b64_str)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Base64'e çevirirken hata oluştu:\n{e}")

    def decode_base64_to_image(self, b64_data):
        if "base64," in b64_data:
            b64_data = b64_data.split("base64,")[-1]
        ext = self.detect_image_type(b64_data)
        image_data = base64.b64decode(b64_data)
        return image_data, ext

    def detect_image_type(self, b64_data):
        if b64_data.startswith("/9j/"):
            return "jpg"
        elif b64_data.startswith("iVBOR"):
            return "png"
        else:
            return "jpg"

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "rb") as img_file:
                        img_bytes = img_file.read()
                        ext = os.path.splitext(file_path)[1].lower()
                        if ext == ".png":
                            prefix = "data:image/png;base64,"
                        elif ext in [".jpg", ".jpeg"]:
                            prefix = "data:image/jpeg;base64,"
                        elif ext == ".gif":
                            prefix = "data:image/gif;base64,"
                        elif ext == ".bmp":
                            prefix = "data:image/bmp;base64,"
                        else:
                            prefix = "data:image/unknown;base64,"
                        b64_str = base64.b64encode(img_bytes).decode("utf-8")
                        self.text_input.setPlainText(prefix + b64_str)
                        self.add_to_history(prefix + b64_str)
                except Exception as e:
                    QMessageBox.critical(self, "Hata", f"Base64'e çevirirken hata oluştu:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
