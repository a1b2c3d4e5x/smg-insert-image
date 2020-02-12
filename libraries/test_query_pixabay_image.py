
from query_pixabay_image import query_image

def query(keyword):
    print("[keyword]: {}".format(keyword))
    image_url = query_image(keyword)
    print("    [url]: {}".format(image_url))
    return image_url

if __name__ == '__main__':

    array = ['dog', '香腸', '維生素']
    for keyword in array:
        query(keyword)
