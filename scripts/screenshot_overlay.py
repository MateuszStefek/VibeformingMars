import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint, QRect
from mss import mss
from PIL import Image

class ScreenshotOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gemini Screenshot Tool")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Initial size and position
        self.setGeometry(100, 100, 400, 300)
        
        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # Top bar (Draggable)
        self.top_bar = QWidget()
        self.top_bar.setFixedHeight(30)
        self.top_bar.setStyleSheet("background-color: black; color: white;")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(5, 0, 5, 0)
        
        self.capture_btn = QPushButton("CAPTURE")
        self.capture_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border: none;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.capture_btn.clicked.connect(self.capture_screenshot)
        
        self.status_label = QLabel("Position me and click CAPTURE")
        self.status_label.setStyleSheet("font-size: 10px; color: white;")
        
        self.close_btn = QPushButton("X")
        self.close_btn.setFixedWidth(30)
        self.close_btn.setStyleSheet("background-color: #e74c3c; color: white; border: none;")
        self.close_btn.clicked.connect(self.close)
        
        self.top_bar_layout.addWidget(self.capture_btn)
        self.top_bar_layout.addWidget(self.status_label)
        self.top_bar_layout.addStretch()
        self.top_bar_layout.addWidget(self.close_btn)
        
        # Central area (Transparent with border)
        self.center_area = QWidget()
        self.center_area.setStyleSheet("""
            QWidget {
                background-color: rgba(52, 152, 219, 100);
                border: 2px solid #3498db;
            }
        """)
        
        self.layout.addWidget(self.top_bar)
        self.layout.addWidget(self.center_area)
        self.setLayout(self.layout)
        
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def capture_screenshot(self):
        self.hide()
        # Small delay to ensure window is hidden
        QApplication.processEvents()
        
        try:
            geom = self.geometry()
            # On some systems, we need to adjust for screen scaling
            with mss() as sct:
                monitor = {
                    "top": geom.top(),
                    "left": geom.left(),
                    "width": geom.width(),
                    "height": geom.height()
                }
                sct_img = sct.grab(monitor)
                output = "/home/mateusz/.gemini/tmp/tf/gemini_screenshot.png"
                img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
                img.save(output)
                self.status_label.setText(f"Saved: {os.path.basename(output)}")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)[:20]}")
        finally:
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotOverlay()
    window.show()
    sys.exit(app.exec_())
