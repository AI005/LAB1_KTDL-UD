Cach chay chuong trinh: (Ubuntu)

1. --- Liệt kê các cột bị thiếu dữ liệu.
[python3 main.py "file name" -method=list-missing-col]
ex: $ python3 main.py house-prices.csv -method=list-missing-col


2. --- Đếm số dòng bị thiếu dữ liệu.
[python3 main.py "file name" -method=get-number-missing-row]
ex: $ python3 main.py house-prices.csv -method=get-number-missing-row


3. ---Điền giá trị bị thiếu bằng phương pháp mean, median (cho thuộc tính numeric) và mode
(cho thuộc tính categorical). Lưu ý: khi tính mean, median hay mode các bạn bỏ qua giá
trị bị thiếu.
[python3 main.py "filename" -method=file-mising-value [--mean, --mode, --median] [$all, "col_name"] "filename_out"]
ex:
    #điền tất cá các ô trống bằng giá trị mean
    $ python3 main.py house-prices.csv -method=fill-missing-value --mean @all new_house-prices.csv

    #điền tất cá các ô trống bằng giá trị mode của cột Electrical
    $ python3 main.py house-prices.csv -method=fill-missing-value --mode Electrical new_house-prices.csv


4. ---Xóa các dòng bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các dòng bị
thiếu hơn 50% giá trị các thuộc tính).
[python3 main.py "filename" -method=remove-row-missing "percent" "filename_out"]
ex: $ python3 main.py house-prices.csv -method=remove-row-missing 0.5 new_house-prices.csv


5. ---Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các cột bị thiếu
giá trị thuộc tính ở hơn 50% số mẫu).
[python3 main.py "filename" -method=remove-col-missing "percent" "filename_out"]
ex: $ python3 main.py house-prices.csv -method=remove-col-missing 0.5 new_house-prices.csv


6. ---Xóa các mẫu bị trùng lặp.
[python3 main.py "filename" -method=remove-duplicate "filename_out"]
ex: $ python3 main.py house-prices.csv -method=remove-duplicate new_house-prices.csv

7. ---Chuẩn hóa một thuộc tính numeric bằng phương pháp min-max và Z-score.
[python3 main.py "filename" -method=normalize-min-max "_min" "_max" "col_name" "filename_out"]
[python3 main.py "filename" -method=normalize-z-score "col_name" "filename_out"]
ex:
    $ python3 main.py house-prices.csv -method=normalize-min-max 0 1 Electrical new_house-prices.csv
    $ python3 main.py house-prices.csv -method=normalize-z-score Electrical new_house-prices.csv


8. ---Tính giá trị biểu thức thuộc tính: ví dụ đối với một tập dữ liệu có chứa 2 thuộc tính width
và height thì biểu thức width ∗ height sẽ trả về tập dữ liệu cũ với một thuộc tính mới có
giá trị ở mỗi mẫu là tích của thuộc tính width và height trong mẫu tương ứng, với điều
kiện cả 2 giá trị width và height đều không bị thiếu, trong trường hợp bị thiếu thì giá trị
biểu thức coi như bị thiếu. Lưu ý: biểu thức có thể có nhiều thuộc tính và nhiều phép toán
bao gồm cộng, trừ, nhân, chia.