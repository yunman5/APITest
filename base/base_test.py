# base_test.py
import inspect

import allure
import json
import requests
import time
import jmespath
import pytest

from common.log import log_info


class BaseTest:
    response_json = None
    response = None

    @staticmethod
    def RunRequest(method, url, headers, payload=()):
        """
        发起请求
        :param method:请求方法
        :param url:请求url
        :param headers:请求头
        :param payload:请求参数
        :return:
        """
        log_info(f'🏄URL: {url}')
        log_info(f'🌐headers: {headers}')
        log_info(f'🌐payload: {payload}')
        log_info(f'🌐method: {method}')
        response = requests.request(method=method, url=url, headers=headers, data=payload, verify=False)
        log_info(f'🌐response status_code: {response.status_code}')
        if response.status_code == 200:
            log_info(f'🌐response: {response.text}')
            BaseTest.response_json = response.json()
            BaseTest.response = response
            return response
        else:
            BaseTest.response = response
            return response

    @staticmethod
    def assert_status_code(expected_code: int):
        """
        返回码断言
        :param expected_code:预期返回码
        :return:
        """
        log_info(f'------------------🔎返回码断言-------------------')
        status_code = BaseTest.response.status_code
        log_info(f'status_code: {status_code}')
        log_info(f'expected_code: {expected_code}')
        assert status_code == expected_code, f"Expected status code: {expected_code}, Actual status code: {response.status_code}"

    @staticmethod
    def assert_response_time(max_time: int):
        """
        返回时间断言
        :param max_time:最大响应时间
        :return:
        """
        log_info(f'------------------🔎返回时间断言-------------------')
        response_time = BaseTest.response.elapsed.total_seconds()
        log_info(f'response_time: {response_time}(s)')
        log_info(f'max_time: {max_time}(s)')
        assert response_time < max_time, f"Response time exceeds maximum allowed time of {max_time} seconds"

    @staticmethod
    def assert_equal(jmes_path, expected_value, msg=None):
        """
        jmes_path断言
        :param msg:断言失败提示
        :param jmes_path:jmes_path路径
        :param expected_value:期望值
        :return:
        """
        log_info(f'------------------🔎返回Json断言-------------------')
        actual_value = jmespath.search(jmes_path, BaseTest.response_json)
        log_info(f'jmes_path: {jmes_path}')
        log_info(f'expected_value: {expected_value}({type(expected_value).__name__})')
        log_info(f'actual_value: {actual_value}({type(actual_value).__name__})')
        if msg is not None:
            assert actual_value == expected_value, f"{msg}"
        assert actual_value == expected_value, f"断言失败"

    @staticmethod
    def extract_value(jmes_path):
        """
        根据jmes_path提取参数
        :param jmes_path:jmes_path路径
        :return:
        """
        log_info(f'------------------🎨提取变量-------------------')
        value = jmespath.search(jmes_path, BaseTest.response_json)
        log_info(f'jmes_path: {jmes_path}')
        log_info(f'value: {value}')
        return value


    @staticmethod
    def wait(seconds: int):
        """
        等待
        :param seconds:等待时间
        :return:
        """
        log_info(f'------------------⏰️等待{seconds}秒-------------------')
        time.sleep(seconds)
