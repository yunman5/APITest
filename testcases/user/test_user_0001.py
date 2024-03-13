import json

import allure

from base.base_test import BaseTest
from common.log import log_info
from common.tools import ENV, c_id, m_id
from config import PSIMLiteHOST, billingPolicyId, DefaultEndTime, vehicleAccessCodeName, \
    PSIMLiteUSER, DataCheckHOST, vehicleAccessCodeId, DefaultAccessCodeName, DefaultDCSAccessZoneIds, \
    DefaultAccessCodeId, C3Controller, X82ReaderCheckHOST
import Enum.UserEnum
from testdata.psimlite_user.user_json_make import user_json_make
from testdata.psimlite_user.user_model import UserCreate


@allure.feature(next(m_id) + 'user_0001_Staff新增')
class Test_user_0001(BaseTest):
    request_json = None

    UserId = None
    useracname = None
    useryitucardno = None
    usercsncardno = None

    @classmethod
    def setup_class(cls):
        cls.request_json = user_json_make(UserCreate("staff").build())

    @classmethod
    def setup_method(cls, method):
        log_info(f'------------------执行请求:{method.__name__}-------------------')

    @classmethod
    def teardown_method(cls, method):
        log_info(f'------------------结束请求:{method.__name__}-------------------')

    @classmethod
    @allure.story(next(c_id) + '新增staff')
    def test_add_staff(cls):
        url = PSIMLiteHOST + "/api/v1/User/Create"
        payload = json.dumps(cls.request_json)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 提取变量
        cls.UserId = cls.extract_value("data")
        log_info(f'cls.UserId={cls.UserId}')
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal("code", 200)
        cls.assert_equal("success", True)
        cls.wait(10)

    @classmethod
    @allure.story(next(c_id) + '新增staff-查询staff，验证数据保存成功')
    def test_staff_verify(cls):
        url = PSIMLiteHOST + f"/api/v1/User/GetById?id={cls.UserId}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        cls.RunRequest("GET", url, headers=headers)
        # 提取变量
        cls.useracname = cls.extract_value("data.userAccessCodeRelationResults[*].accessCodeName")
        cls.useryitucardno = cls.extract_value("data.cards[0].cardExtensionBaseDtos[?type==\'YITU\'].no|[0]")
        cls.usercsncardno = cls.extract_value("data.cards[0].cardExtensionBaseDtos[?type==\'CSN\'].no|[0]")
        log_info(f'cls.useracname={cls.useracname}')
        log_info(f'cls.useryitucardno={cls.useryitucardno}')
        log_info(f'cls.usercsncardno={cls.usercsncardno}')
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('success', True, '断言失败')
        cls.assert_equal('data.name', cls.request_json['name'], '断言失败')
        cls.assert_equal('data.userType', 0, '断言失败')
        cls.assert_equal('data.identifyCards[0].no', cls.request_json['addIdentityCards'][0]['no'], '断言失败')
        cls.assert_equal('data.identifyCards[0].type', cls.request_json['addIdentityCards'][0]['type'], '断言失败')
        cls.assert_equal('data.validityStartTime', cls.request_json['validityStartTime'], '断言失败')
        cls.assert_equal('data.validityEndTime', DefaultEndTime, '断言失败')
        cls.assert_equal('data.isPermanent', True, '断言失败')
        cls.assert_equal('data.contact', cls.request_json['contact'], '断言失败')
        cls.assert_equal('data.email', cls.request_json['email'], '断言失败')
        cls.assert_equal('data.operator', PSIMLiteUSER, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].accessCodeId',
                         cls.request_json['addUserAccessCodeRelations'][0]['accessCodeId'], '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].accessCodeName', DefaultAccessCodeName, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].validityStartTime',
                         cls.request_json['addUserAccessCodeRelations'][0]['startTime'], '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].validityEndTime', DefaultEndTime, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].isPermanent', True, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].enableState', 0, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].status', Enum.UserEnum.Status.Enabled.value,
                         '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].operatorName', PSIMLiteUSER, '断言失败')
        cls.assert_equal('data.userAccessCodeRelationResults[0].isTemp', False, '断言失败')
        cls.assert_equal('data.status', Enum.UserEnum.Status.Enabled.value, '断言失败')
        cls.assert_equal('data.areaCode', cls.request_json['areaCode'], '断言失败')
        cls.assert_equal('data.remarks', cls.request_json['remarks'], '断言失败')
        cls.assert_equal('data.enableState', Enum.UserEnum.EnableState.enabled.value, '断言失败')
        cls.assert_equal('data.company', None, '断言失败')
        cls.assert_equal('data.departmentId', cls.request_json['departmentId'], '断言失败')
        cls.assert_equal('data.tenantCompanyId', None, '断言失败')
        cls.assert_equal('data.pin', cls.request_json['pin'], '断言失败')
        cls.assert_equal('data.cards[0].id', cls.request_json['cardIds'][0], '断言失败')
        cls.assert_equal('data.cards[0].status', 0, '断言失败')
        cls.assert_equal('data.isSingleEntry', False, '断言失败')
        cls.assert_equal('data.dcsProfile', None, '断言失败')
        cls.assert_equal('data.dcsAccessZones[*].id', DefaultDCSAccessZoneIds, '断言失败')
        cls.assert_equal('data.startDCSAutoZone.id', cls.request_json['startDCSAutoZoneId'], '断言失败')
        cls.assert_equal('data.endDCSAutoZone.id', cls.request_json['endDCSAutoZoneId'], '断言失败')
        cls.assert_equal('data.dcsOperatorName', PSIMLiteUSER, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-ZKT下发验证')
    def test_staff_verify_ZKT(cls):
        url = DataCheckHOST + "/datacheck/ZKT/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('Id', cls.UserId, '断言失败')
        cls.assert_equal('CardNo', cls.usercsncardno, '断言失败')
        cls.assert_equal('StartTime', cls.request_json["validityStartTime"], '断言失败')
        cls.assert_equal('EndTime', DefaultEndTime, '断言失败')
        cls.assert_equal('IsExpires', False, '断言失败')
        cls.assert_equal('Name', cls.request_json["name"], '断言失败')
        cls.assert_equal('EnableState', 0, '断言失败')
        cls.assert_equal('IsDeleted', False, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].AccessCodeId', DefaultAccessCodeId, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].IsExpires', False, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].EnableState', 0, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].Name', DefaultAccessCodeName, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-ZKT Controller下发验证')
    def test_staff_verify_ZKT_Controller(cls):
        cls.wait(60)
        url = DataCheckHOST + "/datacheck/C3Controller/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "C3IP": C3Controller,
            "CardNum": cls.usercsncardno
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(5)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('data[0].CardNo', cls.usercsncardno, '断言失败')
        cls.assert_equal('data[0].EndTime', '0', '断言失败')
        cls.assert_equal('data[0].StartTime', '0', '断言失败')
        cls.assert_equal('data[0].Password', cls.request_json["pin"], '断言失败')
        cls.assert_equal('msg', 'C3中有对应卡', '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-Park下发验证')
    def test_staff_verify_Park_DB(cls):
        url = DataCheckHOST + "/datacheck/Park/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('Id', cls.UserId, '断言失败')
        cls.assert_equal('IsDeleted', False, '断言失败')
        cls.assert_equal('CardNumber', cls.useryitucardno, '断言失败')
        cls.assert_equal('IsDeleted', False, '断言失败')
        cls.assert_equal('IsEnabled', True, '断言失败')
        cls.assert_equal('Name', cls.request_json['name'], '断言失败')
        cls.assert_equal('ValidTime', cls.request_json['validityStartTime'], '断言失败')
        cls.assert_equal('InvalidTime', DefaultEndTime, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].AccessCodeId',
                      cls.request_json['addUserAccessCodeRelations'][0]['accessCodeId'], '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].ValidTime',
                      cls.request_json['addUserAccessCodeRelations'][0]['startTime'], '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].InvalidTime', DefaultEndTime, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].IsDeleted', False, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].IsEnalbled', True, '断言失败')
        cls.assert_equal('UserAccessCodeRelations[0].Name', DefaultAccessCodeName, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-Park系统下发验证')
    def test_staff_verify_Park_system(cls):
        url = DataCheckHOST + "/datacheck/ParkSystem/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('Id', cls.UserId, '断言失败')
        cls.assert_equal('username', cls.request_json['name'], '断言失败')
        cls.assert_equal('useracname[0]', DefaultAccessCodeName, '断言失败')
        cls.assert_equal('usercardno', cls.useryitucardno, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-模拟X82Reader用户数据验证')
    def test_staff_verify_x82(cls):
        url = X82ReaderCheckHOST + "/datacheck/X82Reader/User/Auth"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '新增staff-Box下发验证')
    def test_staff_verify_box(cls):
        url = DataCheckHOST + "/datacheck/Box/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('Id', cls.UserId, '断言失败')
        cls.assert_equal('IsDeleted', False, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff')
    def test_staff_delete(cls):
        url = PSIMLiteHOST + "/api/v1/User/Delete"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        payload = json.dumps([cls.UserId])
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('success', True, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-查询staff，验证是否删除成功')
    def test_staff_verify2(cls):
        url = PSIMLiteHOST + f"/api/v1/User/GetById?id={cls.UserId}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ENV("psimlite_token"),
        }
        cls.RunRequest("GET", url, headers=headers)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 400, '断言失败')
        cls.assert_equal('message', 'Not found user', '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-ZKT下发验证')
    def test_staff_verify_ZKT2(cls):
        url = DataCheckHOST + "/datacheck/ZKT/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('IsDeleted', True, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-C3 Controller用户删除查询')
    def test_staff_verify_ZKT_Controller2(cls):
        cls.wait(60)
        url = DataCheckHOST + "/datacheck/C3Controller/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "C3IP": C3Controller,
            "CardNum": cls.usercsncardno
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(5)
        # 响应Json断言
        cls.assert_equal('code', 500, '断言失败')
        cls.assert_equal('msg','C3无对应卡', '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-Park下发验证')
    def test_staff_verify_Park_DB2(cls):
        url = DataCheckHOST + "/datacheck/Park/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 200, '断言失败')
        cls.assert_equal('IsDeleted', True, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-Park系统用户数据验证')
    def test_staff_verify_Park_system2(cls):
        url = DataCheckHOST + "/datacheck/ParkSystem/query"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 500, '断言失败')

    @classmethod
    @allure.story(next(c_id) + '删除staff-x82 Reader用户通行验证')
    def test_staff_verify_x822(cls):
        url = X82ReaderCheckHOST + "/datacheck/X82Reader/User/Auth"
        headers = {
            'Content-Type': 'application/json',
        }
        payload = json.dumps({
            "UserId": cls.UserId
        })
        cls.RunRequest("POST", url, headers=headers, payload=payload)
        # 响应码及时间断言
        cls.assert_status_code(200)
        cls.assert_response_time(3)
        # 响应Json断言
        cls.assert_equal('code', 500, '断言失败')
        cls.assert_equal('res', '权限验证不通过，已上传FR通行记录', '断言失败')