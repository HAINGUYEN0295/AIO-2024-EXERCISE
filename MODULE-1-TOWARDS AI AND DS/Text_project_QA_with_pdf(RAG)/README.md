
# README

## Mô tả dự án

Dự án này triển khai một chatbot dựa trên Retrieval-Augmented Generation (RAG) bằng cách sử dụng framework Chainlit. Chatbot này được thiết kế để cung cấp các câu trả lời chính xác và phù hợp bằng cách kết hợp thông tin từ nhiều nguồn dữ liệu khác nhau.

## Cấu trúc dự án

File `rag_chatbot_by_chainlit.ipynb` chứa các bước sau:

1. **Cài đặt thư viện cần thiết**
   - Sử dụng `!pip install` để cài đặt các thư viện như `transformers`, `torch`, `chainlit`, và các phụ thuộc khác.

2. **Thiết lập cấu hình và tải mô hình**
   - Sử dụng thư viện `transformers` để tải các mô hình tiền huấn luyện từ Hugging Face.
   - Tạo cấu hình cho mô hình RAG.

3. **Xây dựng chức năng của chatbot**
   - Triển khai các hàm xử lý dữ liệu đầu vào và đầu ra cho chatbot.
   - Tạo pipeline cho RAG để kết hợp truy xuất thông tin và sinh câu trả lời.

4. **Chạy ứng dụng Chainlit**
   - Sử dụng lệnh `!chainlit run app.py` để chạy ứng dụng và triển khai chatbot.

## Hướng dẫn sử dụng

### Yêu cầu hệ thống

- Python 3.7 trở lên

### Cài đặt

1. **Clone repository**


2. **Cài đặt các thư viện cần thiết**


3. **Chạy ứng dụng**

   Mở file `rag_chatbot_by_chainlit.ipynb` bằng Jupyter Notebook hoặc Jupyter Lab và chạy tuần tự các cell. Đảm bảo rằng bạn đã cài đặt và cấu hình đúng các thư viện cần thiết.

## Đóng góp

Nếu bạn muốn đóng góp cho dự án, hãy fork repository này và tạo pull request. Chúng tôi hoan nghênh các ý tưởng và cải tiến mới.

## Giấy phép
None

## Liên hệ

Nếu bạn có bất kỳ câu hỏi hoặc góp ý nào, vui lòng liên hệ qua email: [nguyenhai95bkdn@hmail.com].
