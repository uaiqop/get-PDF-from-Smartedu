import json
import os
import pathlib


def _create_config_file(config_path, default_config_path):
    """
    如果没有config.json
    创建config.json，将默认配置写入，返回默认配置的字典
    :return:
    """
    # 创建文件对象
    with open(config_path, "w") as f:
        # 这个是默认配置文件
        with open(default_config_path, "r") as fd:
            # 读取默认配置文件
            default_config = fd.read()
            # 把默认配置里的内容转换为字典
            dic_data = json.loads(default_config)
        # 在写入config后返回默认配置的字典
        f.write(default_config)
        return dic_data


def _get(config_path):
    """
    获取配置文件
    :param config_path:
    :return: 用户配置字典，错误返回None
    """
    try:
        # 创建文件对象
        with open(config_path, "r") as f:
            # 获取字符串
            str_data = f.read()

            # 防止settings文件出错
            try:
                # 转换为字典
                dic_data = json.loads(str_data)
            except json.JSONDecodeError:
                # 转换字典失败的话，说明json文件出错，所以使用默认配置文件覆盖它
                return _create_config_file(config_path, "./default_config.json")
            # 返回
            return dic_data
    except OSError:
        # 转换字典失败的话，说明json文件出错，所以使用默认配置文件覆盖它
        return _create_config_file(config_path, "./default_config.json")


def get_download_dir(config_path):
    """
    获得下载目录
    :param config_path:
    :return:
    """
    # 获取用户目录
    home_dir = str(pathlib.Path.home())
    # 获取默认下载文件夹
    default_dir = fr"{home_dir}\Downloads"

    # 获取用户配置
    config = _get(config_path)
    # 检测是否成功获取配置
    if config is not None:
        # 获取下载目录key对应的value
        download_dir = config["download_dir"]
        # 检测value是否为空，如果是就以用户Downloads目录作为下载目录
        if download_dir != "":
            # 检测配置的下载目录是否存在
            # 返回配置的下载目录如果配置的下载目录存在，否则返回用户默认下载目录
            # 使用三元运算符，代码更加简洁
            return download_dir if os.path.exists(download_dir) else default_dir
        else:
            return default_dir
    else:
        return _create_config_file(config_path, "./default_config.json")
