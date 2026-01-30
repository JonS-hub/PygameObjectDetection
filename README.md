
# 🛰️  Object Tracking & Trajectory Mapping (YOLO11)

This project provides a dual-layer visualization for real-time object tracking using **YOLO11** and **Supervision**. It maps object movements simultaneously on a video feed and a digital canvas.

<img width="1470" height="644" alt="normal" src="https://github.com/user-attachments/assets/8cc04541-c389-4fd9-a05f-ef2ae64c4896" />

## 📖 Overview / Genel Bakış

### 🇺🇸 English
This application processes video streams to identify and track objects (specifically persons). It utilizes a hybrid visualization approach:
* **OpenCV Layer:** Displays the raw video with high-end corner annotations and unique tracking IDs.
* **Pygame Layer:** Generates an abstract map showing the real-time movement trajectories (trails) of each detected object.

### 🇹🇷 Türkçe
Bu uygulama, video akışlarını analiz ederek nesneleri (özellikle kişileri) tanımlar ve takip eder. Hibrit bir görselleştirme yaklaşımı sunar:
* **OpenCV Katmanı:** Orijinal videoyu estetik köşe çerçeveleri ve benzersiz takip kimlikleri (ID) ile sunar.
* **Pygame Katmanı:** Tespit edilen her nesnenin gerçek zamanlı hareket yörüngelerini (izlerini) çizen soyut bir harita oluşturur.

<img width="1275" height="753" alt="detection" src="https://github.com/user-attachments/assets/7678c70a-0e24-4060-8ee3-a3e7e6593699" />


## 🚀 Key Features / Öne Çıkan Özellikler

* **YOLO11 Intelligence:** High-accuracy person tracking using the latest Ultralytics model.
* **Trajectory Mapping:** Historical path tracking for every unique ID using a dynamic buffer.
* **Dual-Window Sync:** Perfect synchronization between CV2 video frames and Pygame surfaces.
* **Performance Optimization:** Frame-skipping logic to maintain high FPS during heavy processing.
* **Data Management:** Efficient detection handling powered by the `supervision` library.

<img width="1273" height="754" alt="PygameScreen" src="https://github.com/user-attachments/assets/09d2729c-7574-4cce-9628-a4d4b662e9e3" />


## 🛠️ Tech Stack / Kullanılan Teknolojiler

| Component | Technology |
| :--- | :--- |
| **Model** | YOLO11s (Ultralytics) |
| **Vision** | OpenCV & Supervision |
| **Graphics** | Pygame (Trajectory Canvas) |
| **Language** | Python 3.x |

<img width="1919" height="799" alt="Screenshot_3" src="https://github.com/user-attachments/assets/3ae70762-b333-4312-871c-cce8f6d710dd" />


## 📦 Installation / Kurulum

```bash
# Install required libraries / Gerekli kütüphaneleri kurun
pip install ultralytics supervision opencv-python pygame numpy

🖥️ How to Use / Nasıl Kullanılır?
Prepare Video: Ensure your input file is named person.mp4 in the root directory.

Run Script: Execute the following command:

Bash
python main.py
Controls: Press 'q' to quit the OpenCV window or close the Pygame interface.

📊 Logic Flow / İşleyiş Mantığı
Detect: YOLO11 locates objects in the frame.

Track: ByteTrack assigns a persistent ID to each detection.

Record: Central coordinates are stored in a track_history dictionary.

Visualize: The path is drawn as a continuous line on the Pygame canvas.
