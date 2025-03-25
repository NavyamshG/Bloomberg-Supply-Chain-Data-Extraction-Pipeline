# Bloomberg Supply Chain Data Automated Extraction Tool

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Automation-Success-green)
![OCR](https://img.shields.io/badge/OCR-PaddleOCR-yellow)

This project automates the extraction of **supplier and customer** screenshots for publicly traded companies by simulating GUI interactions and using OCR to analyze UI flow. The screenshots are organized year-wise for each company, making it useful for **supply chain tracking, visual auditing**, or **data analysis from platforms like Bloomberg**.

---

## 🖼️ Preview

<img src="bbox_preview.png" width="800" alt="bbox preview"/>

---

## 🛠️ Features

- 📂 **Auto-generates folder structures** per ticker and year
- 🖱️ **Simulates mouse/keyboard input** to navigate GUI apps
- 📸 **Captures scrolling screenshots** for both *Suppliers* and *Customers*
- 📅 **Supports annual snapshots** from 2018 to 2023
- 🧠 **Detects UI end-of-list** using image comparison
- 🔤 **PaddleOCR ready** for future integration of text extraction from screenshots

---

## 🧩 Project Structure

```
├── main.py                    # Entry point for user input and flow control
├── folder_structure.py        # Creates dynamic folder structure for tickers
├── screenshot_capture.py      # Core logic for screenshot automation
├── requirements.txt           # Dependencies
├── bbox_preview.png           # Preview image used for scroll-end detection
```

---

## 💻 How It Works

1. **User inputs a ticker**
2. Tool creates directory structure:
   ```
   Companies/
     └── TICKER/
         ├── Suppliers/
         │   └── 2018, 2019, ..., 2023/
         └── Customers/
             └── 2018, 2019, ..., 2023/
   ```
3. GUI automation navigates to relevant tabs and captures screenshots
4. `is_at_end()` detects when scrolling ends based on screen image comparison
5. Images saved and named with timestamps

---

## 📦 Installation

```bash
git clone https://github.com/your-username/supply-chain-screenshot-tool.git
cd supply-chain-screenshot-tool
pip install -r requirements.txt
```

---

## ▶️ Running the Tool

```bash
python main.py
```

You’ll be prompted to enter a ticker (e.g., `AAPL`, `TSLA`). The tool will start folder creation and screenshot automation.

---

## 🧠 Dependencies

- `pyautogui` – GUI automation
- `opencv-python` – image processing
- `paddleocr` & `paddlepaddle` – OCR engine
- `Pillow`, `numpy`, `pandas`, `pygetwindow`, `pywinauto`

---

## 📌 Notes

- Run the script on the **same screen resolution** as it was recorded on (1920x1080 recommended).
- Ensure the Bloomberg or source UI is open and active during runtime.
- You may need to adjust `pyautogui.click()` coordinates based on your screen.

---



## 🚧 Future Enhancements

- OCR post-processing for supplier/customer name extraction
- CSV export of OCR results
- GUI interface for non-technical users
- Integration with other data sources or financial APIs

---
