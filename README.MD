# Bài tập môn truyền thông mạng máy tính chủ đề FEC

Thực thi file split.py chia file sample.png thành các gói kích cỡ bằng nhau vào thư mục split_output
```shell
python split.py
```
Thực thi file redundant.py kết hợp các gói dữ liệu tạo ra redundant file và thêm vào thư mục split_output
```shell
python redundant.py
```
Xóa một file bất kì trong thư mục split_output <em>bước này giả lập một lỗi trên đường truyền làm mất gói dữ liệu sau này thay thế bằng việc thực thi file tunnel.py</em>

Thực thi file concatenate.py thực hiện phát hiện mất mát một gói nào đó và dựa vào các gói còn lại để phục hổi, loại bỏ header của các gói và ghép chúng cho ra kết quả ở thư mục concatenate_output
```shell
python concatenate.py
```