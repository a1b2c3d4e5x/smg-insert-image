
from insert_images import insert_images_from_string, insert_images_from_file
import json
import os

# ex: python3 insert_images.py --file sample.json
# ex: python3 insert_images.py --string "{...}"
if __name__ == '__main__':
    
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

    # sample 1
    json_string = json.dumps(payload)
    result1 = insert_images_from_string(json_string)
    print('[RESULT1]: {}\n\n'.format(result1))

    #sample 2
    result2 = insert_images_from_file('sample.json')
    print('[RESULT2]: {}\n\n'.format(result2))

    exit(0)
    

