# Hướng dẫn sử dụng CenterNet

## Các chức năng chính:
1. Train CenterNet
2. Train TinyDetector

## CenterNet
* Làm theo hướng dẫn trong ReadMe
* Đọc các note hỗ trợ trong Documents(JupyterNotebook for setup)

## Tiny Detector
* Sẽ note sau.

## Setup Dataset 
* Đọc noteCenterNet.docx
* Với dataset sử dụng trong AIC20 thì đó là abc.py nằm trong đường dẫn: "/home/xv/Documents/CenterNet2/src/lib/datasets/dataset/abc.py"

## Setup Inference
* Đã đi phần in kết quả đã inference ra màn hình (đọc note sẽ thấy)
* Đọc noteCenterNet.docx
* Có nhiều file demo.py được dùng cho các mục đích khác nhau:
1. demo.py: xuất output theo định dạng .pkl - format default của CenterNet.
2. demo_2.py: xuất output theo định dạng json, hãy đọc bên trong sẽ thấy cấu trúc file json. Lưu ý là bạn có thể chỉnh lại tùy thich.
3. demo_videos.py: Inference chỉ áp dụng được cho thư mục chứa các file video và inference trên toàn bộ video đó. Chú ý: đã tắt đi phần tạo video kết quả. Muốn sử dụng lại hãy vào và xem code. (và xóa các #).
4. demo_avideo.py: Inference cho 1 video với tên được set bên trong. Chú ý: đã tắt đi phần tạo video kết quả. Muốn sử dụng lại hãy vào và xem code. (và xóa các #).
5. demo_x_ROIs.py: Tương tự như demo_x.py nhưng áp dụng cho tập Region of interests images (trong AIC20).