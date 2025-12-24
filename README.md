Đ# 📄 ĐỒ ÁN HỌC MÁY NÂNG CAO  
## Nhận diện ký tự văn bản tiếng Việt sử dụng VietOCR

---

## 📌 Thông tin chung
- **Tên đề tài:** Nhận diện ký tự quang học (Optical Character Recognition – OCR) cho văn bản tiếng Việt  
- **Môn học:** Học máy nâng cao  
- **Giảng viên hướng dẫn:** Nguyễn Đình Quý  
- **Lớp:** 67CS  
- **Năm học:** 2025  

### 👥 Nhóm thực hiện (Nhóm 11)
- Lê Đình Chính – 0169867  
- **Đỗ Đại Nghĩa – 1500167**  
- Nguyễn Xuân Hoàng  

---

## 📖 1. Giới thiệu đề tài
Nhận diện ký tự quang học (OCR – Optical Character Recognition) là một bài toán quan trọng trong lĩnh vực **Thị giác máy tính**, cho phép máy tính trích xuất nội dung văn bản từ hình ảnh.  

Với sự phát triển của **học sâu**, các mô hình OCR hiện đại đã đạt được độ chính xác cao, đặc biệt đối với các ngôn ngữ có dấu như **tiếng Việt**.  

Trong đồ án này, nhóm tập trung **nghiên cứu, huấn luyện và đánh giá mô hình VietOCR**, đồng thời **so sánh hiệu quả giữa mô hình fine-tune và mô hình pre-trained gốc**.

---

## 🎯 2. Mục tiêu
- Hiểu rõ kiến trúc và nguyên lý hoạt động của mô hình **VietOCR**
- Huấn luyện mô hình OCR cho văn bản tiếng Việt
- Tiền xử lý ảnh nhằm cải thiện độ chính xác nhận diện
- Triển khai hệ thống OCR hoàn chỉnh (Inference)
- Đánh giá và so sánh mô hình huấn luyện với mô hình pre-trained

---

## 🧠 3. Cơ sở lý thuyết

### 3.1 VietOCR
VietOCR là mô hình OCR mã nguồn mở, được thiết kế tối ưu cho tiếng Việt, dựa trên kiến trúc **Encoder – Decoder**.

**Kiến trúc chính:**
- **Backbone (CNN – VGG):** Trích xuất đặc trưng không gian từ ảnh
- **Encoder:** Chuyển đặc trưng ảnh thành biểu diễn chuỗi
- **Decoder (Seq2Seq):** Sinh chuỗi ký tự đầu ra

👉 **Kiến trúc sử dụng trong đồ án:** `vgg_seq2seq`

---

### 3.2 Tesseract OCR
Trong đồ án này, **Tesseract không được dùng để nhận diện nội dung văn bản**, mà được sử dụng để:
- Phát hiện vùng văn bản
- Tách ảnh thành **từng dòng văn bản**
- Giảm độ dài chuỗi đầu vào cho VietOCR

---

## 🏗️ 4. Pipeline hệ thống


Ảnh đầu vào
   ↓
Tiền xử lý ảnh
   ↓
Tesseract OCR (tách dòng)
   ↓
VietOCR (nhận diện từng dòng)
   ↓
Ghép kết quả → Văn bản đầu ra

---

## 📊 5. Dataset
- Dữ liệu gồm các ảnh chứa **văn bản tiếng Việt**
- Nguồn: sách, tài liệu in, chữ viết tay
- Tổng số ảnh: **~4000 ảnh**

### Phân chia dữ liệu
- **Train:** 80% (~3200 ảnh)
- **Validation:** 20% (~800 ảnh)

### Định dạng annotation (.txt)

train/17.jpg|PHƯỜNG ĐÔNG XUYÊN, THÀNH PHỐ LONG XUYÊN, TỈNH AN GIANG

---

## ⚙️ 6. Huấn luyện mô hình

### Cấu hình chính
- Kiến trúc: `vgg_seq2seq`
- Batch size: 16
- Learning rate: 0.0001
- Số bước huấn luyện: 10,000 iters
- Sử dụng GPU (CUDA)

### Theo dõi huấn luyện
- **Train loss:** giảm ổn định
- **Validation loss:** dao động nhẹ
- **Accuracy theo ký tự:** ~88–89%
- **Accuracy theo chuỗi đầy đủ:** thấp hơn do chuỗi dài và ảnh phức tạp

---

## 🧪 7. Đánh giá mô hình

**Chỉ số sử dụng:** CER (Character Error Rate)

| Mô hình     | CER    |
|-------------|--------|
| Pre-trained | ~7.07% |
| Fine-tuned  | ~6.59% |

👉 Mô hình huấn luyện lại cho thấy **độ chính xác được cải thiện**, đặc biệt với các từ tiếng Việt có dấu và từ đặc thù.

---

## 🖥️ 8. Triển khai (Inference)
- Giao diện đơn giản sử dụng **Tkinter**
- Thư viện: Pillow, pytesseract, VietOCR

### Các bước chính
1. Load ảnh
2. Tiền xử lý (grayscale, threshold, resize)
3. Tách dòng bằng Tesseract
4. Nhận diện từng dòng bằng VietOCR
5. Hiển thị kết quả văn bản

---

## ⚠️ 9. Hạn chế
- Accuracy chuỗi đầy đủ chưa cao với ảnh dài
- Phụ thuộc vào chất lượng tách dòng của Tesseract
- Dataset chưa đa dạng hoàn toàn về font và nhiễu

---

## 🚀 10. Hướng phát triển
- Mở rộng dataset
- Fine-tune thêm với Transformer
- Áp dụng data augmentation
- Tối ưu pipeline tiền xử lý ảnh

---

## 📦 11. Lưu ý về repository
Do kích thước lớn, **dataset và model weight (.pth) không được đẩy đầy đủ lên GitHub**.

Repo chủ yếu phục vụ:
- Code
- Cấu hình
- Demo inference
