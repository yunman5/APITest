from faker import Faker
import Enum.UserEnum
from Enum import UserEnum
from common.log import log_info
from common.tools import get_today_timestamp
from config import DefaultDepartmentId, DefaultAccessCodeId, DefaultDCSAccessZoneIds, DefaultStartDCSAutoZoneId, \
    DefaultEndDCSAutoZoneId, DefaultZoneId, DefaultTenantCompanyId
from datafactory.card import card_Get
from datafactory.picUtil import picBase64_Get

fake = Faker("en_US")


def user_json_make(user_request):
    log_info('start user_json_make')
    if user_request.userType == "staff":
        json_dict = staff_json_maker()
    elif user_request.userType == "visitor":
        json_dict = visitor_json_maker()
    elif user_request.userType == "vendor":
        json_dict = vendor_json_maker()
    elif user_request.userType == "tenant":
        json_dict = tenant_json_maker()
    else:
        return 'Error,用户类型错误'

    """
    name字段
    """
    if user_request.name == "EXEMPTFIELD":
        del json_dict["name"]
    elif user_request.name is not None:
        json_dict.update({"name": user_request.name})
    """
    tagIds字段
    """
    if user_request.tagIds == "EXEMPTFIELD":
        del json_dict["tagIds"]
    elif user_request.tagIds is not None:
        json_dict.update({"tagIds": user_request.tagIds})
    """
    areaCode字段
    """
    if user_request.areaCode == "EXEMPTFIELD":
        del json_dict["areaCode"]
    elif user_request.areaCode is not None:
        json_dict.update({"areaCode": user_request.areaCode})
    """
    enableState字段
    """
    if user_request.enableState == "EXEMPTFIELD":
        del json_dict["enableState"]
    elif user_request.enableState is not None:
        json_dict.update({"enableState": user_request.enableState})
    """
    pin字段
    """
    if user_request.pin == "EXEMPTFIELD":
        del json_dict["pin"]
    elif user_request.pin is not None:
        json_dict.update({"pin": user_request.pin})
    """
    contact字段
    """
    if user_request.contact == "EXEMPTFIELD":
        del json_dict["contact"]
    elif user_request.contact is not None:
        json_dict.update({"contact": user_request.contact})
    """
    Email字段
    """
    if user_request.email == "EXEMPTFIELD":
        del json_dict["email"]
    elif user_request.email is not None:
        json_dict.update({"email": user_request.email})
    """
    Remarks字段
    """
    if user_request.remarks == "EXEMPTFIELD":
        del json_dict["remarks"]
    elif user_request.remarks is not None:
        json_dict.update({"remarks": user_request.remarks})
    """
    cardIds字段
    """
    if user_request.cardIds == "EXEMPTFIELD":
        del json_dict["cardIds"]
    elif user_request.cardIds is not None:
        json_dict.update({"cardIds": user_request.cardIds})
    """
    isPermanent字段
    """
    if user_request.isPermanent == "EXEMPTFIELD":
        del json_dict["isPermanent"]
    elif user_request.isPermanent is not None:
        json_dict.update({"isPermanent": user_request.isPermanent})
    """
    validityType字段
    """
    if user_request.validityType == "EXEMPTFIELD":
        del json_dict["validityType"]
    elif user_request.validityType is not None:
        json_dict.update({"validityType": user_request.validityType})
    """
    validityStartTime字段
    """
    if user_request.validityStartTime == "EXEMPTFIELD":
        del json_dict["validityStartTime"]
    elif user_request.validityStartTime is not None:
        json_dict.update({"validityStartTime": user_request.validityStartTime})
    """
    validityEndTime字段
    """
    if user_request.validityEndTime == "EXEMPTFIELD":
        del json_dict["validityEndTime"]
    elif user_request.validityEndTime is not None:
        json_dict.update({"validityEndTime": user_request.validityEndTime})
    """
    faceFileBase64字段
    """
    if user_request.faceFileBase64 == "EXEMPTFIELD":
        del json_dict["faceFileBase64"]
    elif user_request.faceFileBase64 is not None:
        json_dict.update({"faceFileBase64": user_request.faceFileBase64})
    """
    profilePhotoBase64字段
    """
    if user_request.profilePhotoBase64 == "EXEMPTFIELD":
        del json_dict["profilePhotoBase64"]
    elif user_request.profilePhotoBase64 is not None:
        json_dict.update({"profilePhotoBase64": user_request.profilePhotoBase64})
    """
    faceFileId字段
    """
    if user_request.faceFileId == "EXEMPTFIELD":
        del json_dict["faceFileId"]
    elif user_request.faceFileId is not None:
        json_dict.update({"faceFileId": user_request.faceFileId})
    """
    dcsProfileId字段
    """
    if user_request.dcsProfileId == "EXEMPTFIELD":
        del json_dict["dcsProfileId"]
    elif user_request.dcsProfileId is not None:
        json_dict.update({"dcsProfileId": user_request.dcsProfileId})
    """
    dcsAccessZoneIds字段
    """
    if user_request.dcsAccessZoneIds == "EXEMPTFIELD":
        del json_dict["dcsAccessZoneIds"]
    elif user_request.dcsAccessZoneIds is not None:
        json_dict.update({"dcsAccessZoneIds": user_request.dcsAccessZoneIds})
    """
    startDCSAutoZoneId字段
    """
    if user_request.startDCSAutoZoneId == "EXEMPTFIELD":
        del json_dict["startDCSAutoZoneId"]
    elif user_request.startDCSAutoZoneId is not None:
        json_dict.update({"startDCSAutoZoneId": user_request.startDCSAutoZoneId})
    """
    endDCSAutoZoneId字段
    """
    if user_request.endDCSAutoZoneId == "EXEMPTFIELD":
        del json_dict["endDCSAutoZoneId"]
    elif user_request.endDCSAutoZoneId is not None:
        json_dict.update({"endDCSAutoZoneId": user_request.endDCSAutoZoneId})
    """
    departmentId字段
    """
    if user_request.departmentId == "EXEMPTFIELD":
        del json_dict["departmentId"]
    elif user_request.departmentId is not None:
        json_dict.update({"departmentId": user_request.departmentId})
    """
    company字段
    """
    if user_request.company == "EXEMPTFIELD":
        del json_dict["company"]
    elif user_request.company is not None:
        json_dict.update({"company": user_request.company})
    """
    defaultZoneIds字段
    """
    if user_request.defaultZoneIds == "EXEMPTFIELD":
        del json_dict["defaultZoneIds"]
    elif user_request.defaultZoneIds is not None:
        json_dict.update({"defaultZoneIds": user_request.defaultZoneIds})
    """
    accessCodeId字段
    """
    if user_request.accessCodeId == "EXEMPTFIELD":
        del json_dict["addUserAccessCodeRelations"]
    elif user_request.accessCodeId is not None:
        json_dict['addUserAccessCodeRelations'][0].update({"accessCodeId": user_request.accessCodeId})

    """
    accessCodeIsPermanent字段
    """
    if user_request.accessCodeIsPermanent == "EXEMPTFIELD":
        del json_dict["addUserAccessCodeRelations"]
    elif user_request.accessCodeIsPermanent is not None:
        json_dict['addUserAccessCodeRelations'][0].update({"isPermanent": user_request.accessCodeIsPermanent})
    """
    accessCodeStartTime字段
    """
    if user_request.accessCodeStartTime == "EXEMPTFIELD":
        del json_dict["addUserAccessCodeRelations"]
    elif user_request.accessCodeStartTime is not None:
        json_dict['addUserAccessCodeRelations'][0].update({"startTime": user_request.accessCodeStartTime})

    """
    accessCodeEndTime字段
    """
    if user_request.accessCodeEndTime == "EXEMPTFIELD":
        del json_dict["addUserAccessCodeRelations"]
    elif user_request.accessCodeEndTime is not None:
        json_dict['addUserAccessCodeRelations'][0].update({"endTime": user_request.accessCodeEndTime})
    log_info('end user_json_make')
    return json_dict



def staff_json_maker():
    """
    staff json生成
    :param user_request:
    :return:
    """
    json_dict = {}
    json_dict.update({"userType": Enum.UserEnum.UserType.staff.value})
    json_dict.update({"name": fake.name()})
    json_dict.update({"tagIds": []})
    json_dict.update({"areaCode": "+65"})
    json_dict.update({"contact": fake.msisdn()})
    json_dict.update({"email": fake.free_email()})
    json_dict.update({"remarks": fake.catch_phrase()})
    json_dict.update({"enableState": UserEnum.EnableState.enabled.value})
    json_dict.update({"pin": "4321"})
    json_dict.update({"cardIds": [card_Get(0,'new')['cardid']]})
    json_dict.update({"isPermanent": True})
    json_dict.update({"validityType": 0})
    json_dict.update({"validityStartTime": get_today_timestamp()[0]})
    json_dict.update({"validityEndTime": None})
    json_dict.update({"faceFileBase64": picBase64_Get()})
    json_dict.update({"profilePhotoBase64": picBase64_Get()})
    json_dict.update({"dcsProfile": None})
    json_dict.update({"dcsAccessZoneIds": DefaultDCSAccessZoneIds})
    json_dict.update({"startDCSAutoZoneId": DefaultStartDCSAutoZoneId})
    json_dict.update({"endDCSAutoZoneId": DefaultEndDCSAutoZoneId})
    json_dict.update({"attachments": []})
    json_dict.update({"transferSourceUserId": None})
    json_dict.update({"addUserCustomizeManageDtos": []})
    json_dict.update({"createFingerprints": []})
    json_dict.update({"departmentId": DefaultDepartmentId})
    json_dict.update({"defaultZoneIds": DefaultZoneId})
    json_dict.update({"addUserAccessCodeRelations": [
        {
            "accessCodeId": DefaultAccessCodeId,
            "startTime": get_today_timestamp()[0],
            "endTime": None,
            "isPermanent": True,
            "enableState": 0,
            "userAccessCodeSource": 0
        }
    ]})
    json_dict.update({"addIdentityCards": [
        {
            "type": 1,
            "no": fake.vin(),
            "canIdentify": True
        }
    ]})

    return json_dict


def visitor_json_maker():
    json_dict = {}
    json_dict.update({"userType": Enum.UserEnum.UserType.visitor.value})
    json_dict.update({"name": fake.name()})
    json_dict.update({"tagIds": []})
    json_dict.update({"company": fake.company()})
    json_dict.update({"accessRule": 1})
    json_dict.update({"areaCode": "+65"})
    json_dict.update({"contact": fake.msisdn()})
    json_dict.update({"email": fake.free_email()})
    json_dict.update({"remarks": fake.catch_phrase()})
    json_dict.update({"enableState": UserEnum.EnableState.enabled.value})
    json_dict.update({"pin": "1234"})
    json_dict.update({"cardIds": [card_Get(1,'new')['cardid']]})
    json_dict.update({"faceFileBase64": picBase64_Get()})
    json_dict.update({"profilePhotoBase64": picBase64_Get()})
    json_dict.update({"dcsProfile": None})
    json_dict.update({"dcsAccessZoneIds": DefaultDCSAccessZoneIds})
    json_dict.update({"startDCSAutoZoneId": DefaultStartDCSAutoZoneId})
    json_dict.update({"endDCSAutoZoneId": DefaultEndDCSAutoZoneId})
    json_dict.update({"attachments": []})
    json_dict.update({"transferSourceUserId": None})
    json_dict.update({"addUserCustomizeManageDtos": []})
    json_dict.update({"createFingerprints": []})
    json_dict.update({"defaultZoneIds": DefaultZoneId})
    json_dict.update({"addUserAccessCodeRelations": [
        {
            "accessCodeId": DefaultAccessCodeId,
            "startTime": get_today_timestamp()[0],
            "endTime": get_today_timestamp()[1],
            "enableState": 0,
            "hostId": None,
        }
    ]})
    json_dict.update({"addIdentityCards": [
        {
            "type": 1,
            "no": fake.vin(),
            "canIdentify": True
        }
    ]})
    return json_dict


def vendor_json_maker():
    """
    vendor json生成
    :param user_request:
    :return:
    """
    json_dict = {}
    json_dict.update({"userType": Enum.UserEnum.UserType.vendor.value})
    json_dict.update({"name": fake.name()})
    json_dict.update({"tagIds": []})
    json_dict.update({"accessRule": 1})
    json_dict.update({"areaCode": "+65"})
    json_dict.update({"contact": fake.msisdn()})
    json_dict.update({"email": fake.free_email()})
    json_dict.update({"remarks": fake.catch_phrase()})
    json_dict.update({"enableState": UserEnum.EnableState.enabled.value})
    json_dict.update({"validityType": 0})
    json_dict.update({"validityStartTime": get_today_timestamp()[0]})
    json_dict.update({"validityEndTime": None})
    json_dict.update({"isPermanent": True})
    json_dict.update({"pin": "1234"})
    json_dict.update({"cardIds": [card_Get(2,'new')['cardid']]})
    json_dict.update({"faceFileBase64": picBase64_Get()})
    json_dict.update({"profilePhotoBase64": picBase64_Get()})
    json_dict.update({"dcsProfile": None})
    json_dict.update({"dcsAccessZoneIds": DefaultDCSAccessZoneIds})
    json_dict.update({"endDCSAutoZoneId": DefaultStartDCSAutoZoneId})
    json_dict.update({"endDCSAutoZoneId": DefaultEndDCSAutoZoneId})
    json_dict.update({"attachments": []})
    json_dict.update({"transferSourceUserId": None})
    json_dict.update({"addUserCustomizeManageDtos": []})
    json_dict.update({"createFingerprints": []})
    json_dict.update({"defaultZoneIds": DefaultZoneId})
    json_dict.update({"addUserAccessCodeRelations": [
        {
            "accessCodeId": DefaultAccessCodeId,
            "startTime": 1699672260000,
            "endTime": None,
            "isPermanent": True,
            "enableState": 0,
            "userAccessCodeSource": 0
        }
    ]})
    json_dict.update({"addIdentityCards": [
        {
            "type": 1,
            "no": fake.vin(),
            "canIdentify": True
        }
    ]})
    return json_dict


def tenant_json_maker():
    """
    tenant json生成
    :param user_request:
    :return:
    """
    json_dict = {}
    json_dict.update({"userType": Enum.UserEnum.UserType.tenant.value})
    json_dict.update({"name": fake.name()})
    json_dict.update({"enableState": UserEnum.EnableState.enabled.value})
    json_dict.update({"tagIds": []})
    json_dict.update({"areaCode": "+65"})
    json_dict.update({"contact": fake.msisdn()})
    json_dict.update({"email": fake.free_email()})
    json_dict.update({"remarks": fake.catch_phrase()})
    json_dict.update({"pin": "1234"})
    json_dict.update({"cardIds": [card_Get(3,'new')['cardid']]})
    json_dict.update({"isPermanent": True})
    json_dict.update({"validityType": 0})
    json_dict.update({"validityStartTime": get_today_timestamp()[0]})
    json_dict.update({"validityEndTime": None})
    json_dict.update({"faceFileBase64": picBase64_Get()})
    json_dict.update({"profilePhotoBase64": picBase64_Get()})
    json_dict.update({"dcsProfile": None})
    json_dict.update({"dcsAccessZoneIds": DefaultDCSAccessZoneIds})
    json_dict.update({"startDCSAutoZoneId": DefaultStartDCSAutoZoneId})
    json_dict.update({"endDCSAutoZoneId": DefaultEndDCSAutoZoneId})
    json_dict.update({"attachments": []})
    json_dict.update({"transferSourceUserId": None})
    json_dict.update({"addUserCustomizeManageDtos": []})
    json_dict.update({"createFingerprints": []})
    json_dict.update({"tenantCompanyId": DefaultTenantCompanyId})
    json_dict.update({"defaultZoneIds": DefaultZoneId})
    json_dict.update({"addUserAccessCodeRelations": [
        {
            "accessCodeId": DefaultAccessCodeId,
            "startTime": get_today_timestamp()[0],
            "endTime": None,
            "isPermanent": True,
            "enableState": 0,
            "userAccessCodeSource": 0
        }
    ]})
    json_dict.update({"addIdentityCards": [
        {
            "type": 1,
            "no": fake.vin(),
            "canIdentify": True
        }
    ]})

    return json_dict
