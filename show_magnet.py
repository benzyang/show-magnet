import requests
from PIL import Image
from io import BytesIO
from IPython.display import display
import sys
import argparse


def whatslink(link, port=7895, showimage=False):
    url = "https://whatslink.info/api/v1/link"
    params = {
    "url": link
    }
    proxies = {
        "http": f"http://127.0.0.1:{port}",
        "https": f"http://127.0.0.1:{port}"
    }

    response = requests.get(url, params=params)
    data = response.json()
    # print(data)
    name = data["name"]
    count = data["count"]
    size = data["size"]
    formatted_size = "{:.2f} MB".format(size / 1024 / 1024) if size / 1024 / 1024 < 1000 else "{:.2f} GB".format(size / 1024 / 1024 / 1024)
    file_type = data["file_type"]
    screenshots = data["screenshots"]

    print("Resource Name: ", name)
    print("Number of Files: ", count)
    print("Total File Size: ", formatted_size)
    print('File Type: ', file_type)

    if showimage:
        for i in screenshots:
            image_url = i['screenshot']
            
            # 发送请求并获取图片数据
            response = requests.get(image_url)
            image_data = response.content

            # 将图片数据转换为Image对象
            image = Image.open(BytesIO(image_data))

            # 显示图片
            display(image)
        

# 创建参数解析器
parser = argparse.ArgumentParser(description='命令行参数示例')

# 添加参数选项
parser.add_argument('-p', '--port', type=int, help='端口号')
parser.add_argument('-u', '--url', type=str, help='链接')

# 解析命令行参数
args = parser.parse_args()

# 获取端口号和链接
port = args.port
url = args.url

# 检查参数
if url is None:
    print("请提供链接参数")
    exit(1)

if port is None:
    print("请提供端口号参数")
    exit(1)



whatslink(f'{url}', port)