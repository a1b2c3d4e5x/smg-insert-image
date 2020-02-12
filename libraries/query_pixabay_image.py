
from pixabay import Image
import argparse 
import time
import json
import os

# Pixabay API Key
PIXABAY_API_KEY = '[YOUR_PIXABAY_API_KEY]'

def _process_command():
    parser = argparse.ArgumentParser()
    # 關鍵字
    parser.add_argument('--keyword', type=str, required=True, help='Search word.')
    return parser.parse_args()

def _search_image_from_pixabay(keyword):
    # https://github.com/momozor/python-pixabay
    # https://pixabay.com/api/docs/

    # image operations
    image = Image(PIXABAY_API_KEY)

    # custom image search
    result = image.search(
        q = keyword,
        lang = 'zh',
        page = 1,
        per_page = 3,
        image_type='photo',
        orientation = 'all', # "all", "horizontal", "vertical"
        order = 'popular', # "popular", "latest"
        safesearch = 'true')

    return result

def _get_image_url_from_pixabay_json(pixabay_json):
    try:
        json_string = json.dumps(pixabay_json)
        json_dict = json.loads(json_string)

        if 0 == len(json_dict['hits']):
            # hardcode default background
            return 'https://pixabay.com/get/57e0d2414954aa14ea9d827dc52b3f7e1622dfe05b507449702e7ad3/black-1072366.jpg'

        return json_dict['hits'][0]['largeImageURL']
    except ValueError:
        return ''

def query_image(keyword):
    # 取得 pixabay json 查詢結果
    pixabay_result = _search_image_from_pixabay(keyword)
    #print(" [result]: {}".format(pixabay_result))

    # 取得圖片網址
    image_url = _get_image_url_from_pixabay_json(pixabay_result)

    return image_url

# sample: python3 main.py --keyword dog
if __name__ == '__main__':
    # 參數處理
    args = _process_command()
    print("[keyword]: {}".format(args.keyword))

    image_url = query_image(args.keyword)
    print("    [url]: {}".format(image_url))

