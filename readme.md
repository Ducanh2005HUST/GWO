# Grey Wolf Optimizer (GWO) – Applied to Communication Systems

## Project Structure
- `gwo.py` – Thuật toán GWO gốc + hình minh hoạ vectors Alpha/Beta/Delta.
- `mgwo.py` – Biến thể mGWO.
- `problem_comm.py` – Bài toán truyền thông (tối ưu SINR).
- `utils_plot.py` – Vẽ đường hội tụ.
- `main.py` – File chạy toàn bộ project so sánh GWO

## Visualization
- Minh hoạ hướng di chuyển của sói.
- Đồ thị hội tụ GWO vs mGWO.

## Communication Application
Ví dụ tối ưu công suất P để tối đa SINR:
\[
SINR = \frac{P h^2}{\sigma^2 + I}
\]
GWO minimize → dùng hàm fitness = -SINR.
