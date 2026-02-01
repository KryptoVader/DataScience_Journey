import requests
from tqdm import tqdm

url = "https://download-cdn.jetbrains.com/python/pycharm-2025.1.3.1.exe"
r = requests.get(url, stream=True)

fileSize = int(r.headers['content-length'])
progress_bar = tqdm(total=fileSize, unit='iB',unit_scale=True)
with open('pycharm.exe','wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        progress_bar.update(len(chunk))
        f.write(chunk)
progress_bar.close()  