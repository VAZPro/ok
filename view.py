import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def watch_video(video_url, watch_time):
    """
    Hàm tự động mở video TikTok và xem trong khoảng thời gian nhất định.
    """
    try:
        # Khởi chạy trình duyệt
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Ẩn trình duyệt nếu không cần xem trực tiếp
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Mở link video TikTok
        print(f"🔗 Đang mở video: {video_url}")
        driver.get(video_url)

        # Chờ tải trang và giả lập "xem video"
        print(f"👀 Đang xem video trong {watch_time} giây...")
        time.sleep(watch_time)

        print(f"✅ Xem xong video: {video_url}")
        driver.quit()
    except Exception as e:
        print(f"❌ Lỗi khi xem video: {str(e)}")


def main():
    """
    Bot chính để tự động tìm kiếm và xem video TikTok.
    """
    try:
        # Hỏi người dùng nhập danh sách link
        print("Nhập danh sách link video TikTok (mỗi link cách nhau bởi dấu phẩy):")
        user_input = input("➡ ")
        video_links = [link.strip() for link in user_input.split(",") if link.strip()]

        if not video_links:
            print("❌ Lỗi: Bạn chưa nhập bất kỳ link nào!")
            return

        # Hỏi thời gian xem mỗi video
        watch_time = int(input("Nhập thời gian xem mỗi video (giây): "))

        # Thực hiện xem từng video
        print("\n🚀 Bắt đầu xem video...\n")
        for video_url in video_links:
            watch_video(video_url, watch_time)

        print("\n✅ Hoàn tất xem tất cả video!")
    except ValueError:
        print("❌ Lỗi: Vui lòng nhập số hợp lệ!")
    except KeyboardInterrupt:
        print("\n❌ Đã dừng bot theo yêu cầu.")


if __name__ == "__main__":
    main()
