import re
import requests
import json


def _get_contentId(url: str):
    rule = "contentId=(.*?)&catalogType="
    try:
        result = re.findall(rule, url)[0]
    except IndexError:
        return None
    return result


def get_pdf_url(url: str):
    """
    获得pdf文件的下载链接
    :param url: 教材链接
    :return: pdf文件的下载链接
    """
    result = _get_contentId(url)
    if result is not None:
        pdf_url = f"https://r3-ndr.ykt.cbern.com.cn/edu_product/esp/assets/{result}.pkg/pdf.pdf"
        return pdf_url
    else:
        return None


def get_pdf_name(url: str):
    result = _get_contentId(url)
    if result is not None:
        json_data = requests.get(f"https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{result}.json")
        json_data = json_data.text
        dic_data = json.loads(json_data)
        return dic_data["title"]
    else:
        return None

