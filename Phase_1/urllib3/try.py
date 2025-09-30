import urllib3
from tqdm import tqdm

http = urllib3.PoolManager()

URL = "https://download-cdn.jetbrains.com/python/pycharm-2025.1.3.1.exe"
file = http.request('GET', url=URL, preload_content = False)

file_size = int(file.headers['Content-Length'])
progress_bar = tqdm(total=file_size, unit='iB', unit_scale=True)

with open('pycharm.exe', 'wb') as f:
    while True:
        chunk = file.read(1024)
        if not chunk:
            break
        progress_bar.update(len(chunk))
        f.write(chunk)
        
progress_bar.close()
file.release_conn()