
from libraries.query_pixabay_image import query_image
import argparse 
import json

def _process_command():
    parser = argparse.ArgumentParser()
    # 關鍵字
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--json', type=str, help='input json string.')
    group.add_argument('--file', type=str, help='input file path of json string.')

    return parser.parse_args()

def _read_json_from_file(path):
    try:
        f = open(path, 'r')
    except IOError:
        print('failed to open file: {}'.format(path))
        return ''
    else:
        with f:
            return f.read()

def insert_images_from_string(json_string):
    try:
        json_object = json.loads(json_string)

        for frame in json_object['frames']:
            image_url = query_image(frame['keyword'])

            print('[keyword]: {}'.format(frame['keyword']))
            print('    [url]: {}\n'.format(image_url))

            frame.update({'picture': image_url})

        return json.dumps(json_object)

    except json.JSONDecodeError as jex:
        print('Failed to insert images: {}'.format(jex))
        return json_string

def insert_images_from_file(json_file):
    json_string = _read_json_from_file(json_file)
    return insert_images_from_string(json_string)

if __name__ == '__main__':
    args = _process_command()

    json_string = ''
    if not args.file:
        json_string = args.json
    else:
        json_string = _read_json_from_file(args.file)

    if not json_string:
        print('error: Input empty.')
        exit(-1)

    result = insert_images_from_string(json_string)
    print(result)

    exit(0)
    

