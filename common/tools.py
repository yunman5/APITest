import base64
import hashlib
import os
import random
from datetime import datetime
import urllib3
from dotenv import set_key, load_dotenv
from common.log import log_info
from config import project_path, env_variables

# 禁用安全验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def md5value(key):
    """
    md5加密
    :param key:
    :return:
    """
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    return input_name.hexdigest().upper()


def get_all_filenames_sorted_by_mtime(folder_path):
    """
    获取指定路径内文件名
    :param folder_path:
    :return:
    """
    filenames = []
    for filename in os.listdir(folder_path):
        # 判断路径是否为文件
        if os.path.isfile(os.path.join(folder_path, filename)):
            filenames.append(filename)
    # 按照修改时间排序文件名
    filenames.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    return filenames


def get_random_pic_base64():
    """
    获取随机头像base64
    :param file_path:
    :return:
    """
    picpath = 'datafactory/resource/headpic/'
    allpiclist = get_all_filenames_sorted_by_mtime(picpath)
    luckynum = random.randint(0, len(allpiclist) - 1)
    with open(picpath + allpiclist[luckynum], 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')


def get_today_timestamp():
    # 获取当前日期
    current_date = datetime.now().date()

    # 构造当天 00:00 的时间
    start_of_day = datetime.combine(current_date, datetime.min.time())

    # 构造当天 23:59 的时间
    end_of_day = datetime.combine(current_date, datetime.max.time())

    # 将时间转换为时间戳（单位：毫秒）
    start_timestamp = int(start_of_day.timestamp() * 1000)
    end_timestamp = int(end_of_day.timestamp() * 1000)
    return start_timestamp, end_timestamp


def set_psim_token(token):
    # 更新指定键的值
    set_key(project_path + '\\.env', 'psim_token', 'Bearer ' + token, quote_mode="never")
    log_info("已在" + project_path + '\\.env，位置设置psim_token，token为 Bearer ' + token)


def set_psimlite_token(token):
    # 更新指定键的值
    set_key(project_path + '\\.env', 'psimlite_token', 'Bearer ' + token, quote_mode="never")
    log_info("已在" + project_path + '\\.env，位置设置psimlite_token，token为 Bearer ' + token)


def ENV(key):
    """
    获取.env文件，指定键值
    :param key:
    :return:
    """
    return env_variables.get(key)


def module_id():
    """
    测试模块编号
    :return:
    """
    for i in range(1, 1000):
        id = 'Module_' + str(i).zfill(3) + '_'
        yield id


m_id = module_id()


def case_id():
    """
        测试模块编号
        :return:
        """
    for i in range(1, 10000):
        id = str(i).zfill(4) + '_'
        yield id


c_id = case_id()
