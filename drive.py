# -*- coding: utf-8 -*-
import requests
import os
import time

download_url = "https://drive.usercontent.google.com/xxxxxxxxx"

def download_file(url):
    print("開始下载文件...")

    response = requests.get(url, stream=True)

    if response.headers.get('Content-Type') == 'text/html':
        print("下载失敗，可能文件不存在或沒有權限。")
        return

    total_size = int(response.headers.get('Content-Length', 0))
    print(f"檔案總大小: {total_size / (1024 * 1024):.2f} MB")

    file_name = "downloaded_file.bin" 
    with open(file_name, 'wb') as file:
        downloaded_size = 0
        chunk_size = 1024 * 1024
        for chunk in response.iter_content(chunk_size=chunk_size):
            file.write(chunk)
            downloaded_size += len(chunk)
            print(f"下载進度: {downloaded_size / (1024 * 1024):.2f} MB / {total_size / (1024 * 1024):.2f} MB ({downloaded_size / total_size * 100:.2f}%)", end='\r') 

    print(f"\n下載完成, 文件已保存為: {file_name}")

    os.remove(file_name)
    print(f"已刪除檔案: {file_name}")

if __name__ == "__main__":
    while True:
        download_file(download_url)
        print("等待300秒後繼續下載...")
        time.sleep(300)
