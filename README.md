使用文档：
```python
import json
import allure
from base.base_test import BaseTest
from common.log import log_info
from common.tools import ENV, c_id, m_id
from config import PSIMLiteHOST, billingPolicyId, DefaultEndTime, vehicleAccessCodeName, \
    PSIMLiteUSER
import Enum.VehicleEnum
from testdata.psimlite_vehicle.vehicle_json_make import vehicle_json_make
from testdata.psimlite_vehicle.vehicle_model import VehicleCreate

@allure.feature(next(m_id) + 'vehicle_0011_Vehicle新增')
class Test_vehicle_0011(BaseTest):
    request_json = None
    VehicleId = None
    vehicleacname = None

    @classmethod
    def setup_class(cls):
        cls.request_json = vehicle_json_make(VehicleCreate().build())

    @classmethod
    def setup_method(cls, method):
        log_info(f'------------------执行请求:{method.__name__}-------------------')

    @classmethod
    def teardown_method(cls, method):
        log_info(f'------------------结束请求:{method.__name__}-------------------')

    @classmethod
    @allure.story(next(c_id) + '新增Vehicle')
    def test_add_vehicle(cls):
        url = PSIMLiteHOST + "/api/v1/Vehicle/Create"
        payload = json.dumps(cls.request_json)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 提取变量
        cls.VehicleId = cls.extract_value("data")
        log_info(f'cls.VehicleId={cls.VehicleId}')
        cls.wait(10)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal("code", 200)
        cls.assert_equal("success", True)

    @classmethod
    @allure.story(next(c_id) + '新增Vehicle-查询Vehicle，验证数据保存成功')
    def test_verify_vehicle(cls):
        url = PSIMLiteHOST + f"/api/v1/Vehicle/GetById/{cls.VehicleId}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        cls.RunRequest("GET", url, headers=headers)
        # 提取变量
        cls.vehicleacname = cls.extract_value("data.accessCodes[*].accessCodeName")
        log_info(f'cls.vehicleacname={cls.vehicleacname}')
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal("code", 200)
        cls.assert_equal("success", True)
        cls.assert_equal('data.billingPolicyId', billingPolicyId)
        cls.assert_equal('data.disabled', False)
        cls.assert_equal('data.driverName', cls.request_json['driverName'])
        cls.assert_equal('data.validityStartTime', cls.request_json['validityStartTime'])
        cls.assert_equal('data.validityEndTime', DefaultEndTime)
        cls.assert_equal('data.isPermanent', True)
        cls.assert_equal('data.plateNumber', cls.request_json['plateNumber'])
        cls.assert_equal('data.platePrefixType', cls.request_json['platePrefixType'])
        cls.assert_equal('data.remarks', cls.request_json['remarks'])
        cls.assert_equal('data.accessCodes[0].accessCodeId', cls.request_json['accessCodes'][0]['accessCodeId'])
        cls.assert_equal('data.accessCodes[0].accessCodeName', vehicleAccessCodeName)
        cls.assert_equal('data.accessCodes[0].startTime', cls.request_json['accessCodes'][0]['startTime'])
        cls.assert_equal('data.accessCodes[0].endTime', DefaultEndTime)
        cls.assert_equal('data.accessCodes[0].isPermanent', True)
        cls.assert_equal('data.accessCodes[0].disabled', False)
        cls.assert_equal('data.accessCodes[0].status', Enum.VehicleEnum.Status.Enabled.value)
        cls.assert_equal('data.accessCodes[0].operatorName', PSIMLiteUSER)
        cls.assert_equal('data.status', Enum.VehicleEnum.Status.Enabled.value)
        cls.assert_equal('data.vehicleType', cls.request_json['vehicleType'])
```