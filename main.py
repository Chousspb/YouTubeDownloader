from pytube import YouTube
import time
from dotenv import load_dotenv
import os
os.environ["SSL_CERT_FILE"] = "/private/etc/ssl/cert.pem"


start = time.time()

load_dotenv()

video = os.getenv("TEXT")
link = video
yt = YouTube(link).streams.get_highest_resolution().download('/Users/Admin/Documents/YoutubeDownloads')


print("Видео успешно загружено")

end = time.time() - start
print(f"Выполнено за: {end:.2f} секунд")
