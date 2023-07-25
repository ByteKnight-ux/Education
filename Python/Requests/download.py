import requests, os, time
from tqdm import tqdm

# without using stream feature
def one_time_download():
    # URL = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622.exe'
    URL = 'https://e7.pngegg.com/pngimages/631/343/png-clipart-circle-n-carpet-cleaning-upland-green-dot-corporation-others-rectangle-grass.png'
    response = requests.get(URL)
    with open(os.path.basename(URL), 'wb') as f:
        f.write(response.content)

# using stream feature
def chunks_download():
    URL = 'https://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-community-8.0.33.0.msi'
    response = requests.get(URL, stream=True)

    if response.status_code == 200:

        FILENAME = os.path.basename(URL)
        FILESIZE = int(response.headers['content-length'])

        CHUNKSIZE = 1024
        downloadSize = 0

        with open(FILENAME, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNKSIZE):
                f.write(chunk)
                downloadSize += len(chunk)
                progress = round((downloadSize / FILESIZE) * 100, 2)
                print(f'Progress: {progress} %')
        print('Download Complete')

one_time_download()
# chunks_download()