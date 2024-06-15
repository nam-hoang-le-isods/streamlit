# Import essential libraries
import streamlit as st
import numpy as np

def main():
    # st.sidebar.slider: thanh trượt để người dùng có thể điều chỉnh giá trị 
    # số lần lặp lại của thuật toán fractal
    # name - min - max - default value - step
    iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
    # khoảng cách giữa các phần tử fractal 
    # min - max - default
    separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

    # Thanh tiến trình 
    progress_bar = st.sidebar.progress(0)

    # Khung chương trình 
    frame_text = st.sidebar.empty()
    # Ảnh fractal 
    image = st.empty()

    # default values 
    m, n, s = 960, 640, 400
    # m - width 
    # n - height 
    # s - scale factor -> xác định phạm vi tọa độ 

    # Tạo ra một số lượng giá trị từ -2.4 tới 2.4, sau đó reshape về vector (1, 960)
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    # làm tương tự với biển y
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

    # Cho frame và giá trị chạy tuwf0 tới 4pi 
    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        # Giá trị cho thanh progress
        progress_bar.progress(frame_num / 100)
        frame_text.text("Frame %i/100" % (frame_num + 1))

        # Performing some fractal wizardry.
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # Update the image placeholder by calling the image() function on it.
        image.image(1.0 - (N / N.max()), use_column_width=True)

    # Xóa trạng thái
    progress_bar.empty()
    frame_text.empty()

    # Rerun
    st.button("Re-run")

if __name__ == "__main__":
    main()
