## Install required dependencies
Install `tesseract-ocr` in your system:
```
winget install --id "UB-Mannheim.TesseractOCR"
```
Install Python Libraries (in same directory):
```
pip install -r requirements.txt
```
A New training data is also present in the program directory, move this data into `C:/Program Files/Tesseract-OCR` and replace with file already exists there.

A Sample Image is also present in the program directory

To run the sample
```
python ./captcha_solver.py
```

Email: swami.ganesh@proton.me