#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/5 15:05
Email : adamyue@163.com
'''
import os
import time
from concurrent.futures import ProcessPoolExecutor
from urllib.request import urlopen, Request
def download_img(url:str):
    site_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(site_url) as response:
        img_data = response.read()
    if not img_data:
        raise ConnectionError(f'Cannot load the specified image from {url}')

    img_file_name = os.path.basename(url)
    with open(img_file_name, 'wb') as f:
        f.write(img_data)

    return f'Downloaded: {img_file_name} from {url}'

def main():
    with ProcessPoolExecutor() as executor:
        urls = [
            'https://cdn.pixabay.com/photo/2021/09/28/13/14/cat-6664412_1280.jpg',
            'https://cdn.pixabay.com/photo/2022/11/10/00/38/creative-7581718_640.jpg',
            'https://cdn.pixabay.com/photo/2022/11/19/11/53/rose-7601873_640.jpg',
            'https://cdn.pixabay.com/photo/2022/10/18/12/05/clouds-7530090_640.jpg',
        ]

        results = executor.map(download_img, urls)
        for result in results:
            print(result)

if __name__ == '__main__':
    main()
