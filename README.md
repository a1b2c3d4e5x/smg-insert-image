#Description

##Input
```
{
    "title": "xxxxx",
    "content":"yyyyy",
    "frames": [
        {
            "sentence": "some sentence 1",
            "keyword": "keyword 1"
        }, {
            "sentence": "some sentence 2",
            "keyword":"keyword 2"
        }, {
            "sentence": "some sentence 3",
            "keyword":"keyword 3"
        }
    ]
}
```

##Output
```
{
    "title": "xxxxx",
    "content":"yyyyy",
    "frames": [
        {
            "sentence": "some sentence 1",
            "keyword": "keyword 1",
            "picture": "https://pixabay.com/get/aaa.jpg"
        }, {
            "sentence": "some sentence 2",
            "keyword":"keyword 2",
            "picture": "https://pixabay.com/get/bbb.jpg"
        }, {
            "sentence": "some sentence 3",
            "keyword":"keyword 3",
            "picture": "https://pixabay.com/get/ccc.jpg"
        }
    ]
}
```

##Usage
###Replacing your pixabay api key in ./libraries/PIXABAY_API_KEY file.

##Run
```
python3 insert_images.py --file sample.json
```
```
python3 insert_images.py --json "{...}"
```
```
from insert_images import insert_images_from_file

    result = insert_images_from_file('sample.json')
    print('[RESULT]: {}\n\n'.format(result))
    
```


```
from insert_images import insert_images_from_string
import json

payload = {
        'title': '感冒時怎麼吃，才能快點好？',
        'content': '醫生說感冒時要吃清淡點，難道平常愛吃的，生病就都不能吃了嗎？到底怎麼吃，感冒才能快點好？',
        'frames': [
            {
                'sentence': '1.以最少量、濃縮的飲食獲取最高熱量',
                'keyword': '高熱量'
            }, {
                'sentence': '2.選擇高品質蛋白質，增加身體修復能力。',
                'keyword': '蛋白質'
            }, {
                'sentence': '3.以流質食物為主，減少腸胃消化負擔。',
                'keyword': '腸胃'
            }
        ]
    }

    json_string = json.dumps(payload)
    result = insert_images_from_string(json_string)
    print('[RESULT]: {}\n\n'.format(result))
```

##Note
###Images from https://pixabay.com

