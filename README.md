# Boundary_Extraction
對圖片做Boundary Extraction，使其能找出物件的邊界。

## 環境需求
- python 3.6+
- Pillow 8.0.1
### PIP 安裝 requirements.txt 的套件
```
pip install -r requirements.txt
```
## Demo
```
python boundary_extraction.py
```
## 結果說明
- ErosionImage.jpg : 將黑白圖片做Erosion
- BoundaryExtractionImage.jpg : 將黑白圖片減去ErosionImage
