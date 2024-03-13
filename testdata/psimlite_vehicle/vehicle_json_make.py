from faker import Faker
import Enum.UserEnum
from Enum import VehicleEnum
from common.log import log_info
from common.tools import get_today_timestamp
from config import *


fake = Faker("en_US")


def vehicle_json_make(vehicle_request):
    log_info('start vehicle_json_make')
    json_dict = vehicle_json_maker()
    """
    id字段
    """
    if vehicle_request.id == "EXEMPTFIELD":
        del json_dict["id"]
    elif vehicle_request.id is not None:
        json_dict.update({"id": vehicle_request.id})
    """
    platePrefixType字段
    """
    if vehicle_request.platePrefixType == "EXEMPTFIELD":
        del json_dict["platePrefixType"]
    elif vehicle_request.platePrefixType is not None:
        json_dict.update({"platePrefixType": vehicle_request.platePrefixType})
    """
    plateNumber字段
    """
    if vehicle_request.plateNumber == "EXEMPTFIELD":
        del json_dict["plateNumber"]
    elif vehicle_request.plateNumber is not None:
        json_dict.update({"plateNumber": vehicle_request.plateNumber})
    """
    vehicleType字段
    """
    if vehicle_request.vehicleType == "EXEMPTFIELD":
        del json_dict["vehicleType"]
    elif vehicle_request.vehicleType is not None:
        json_dict.update({"vehicleType": vehicle_request.vehicleType})
    """
    billingPolicyId字段
    """
    if vehicle_request.billingPolicyId == "EXEMPTFIELD":
        del json_dict["billingPolicyId"]
    elif vehicle_request.billingPolicyId is not None:
        json_dict.update({"billingPolicyId": vehicle_request.billingPolicyId})

    """
    driverName字段
    """
    if vehicle_request.driverName == "EXEMPTFIELD":
        del json_dict["driverName"]
    elif vehicle_request.driverName is not None:
        json_dict.update({"driverName": vehicle_request.driverName})
    """
    Remarks字段
    """
    if vehicle_request.remarks == "EXEMPTFIELD":
        del json_dict["remarks"]
    elif vehicle_request.remarks is not None:
        json_dict.update({"remarks": vehicle_request.remarks})
    """
    tagIds字段
    """
    if vehicle_request.tagIds == "EXEMPTFIELD":
        del json_dict["tagIds"]
    elif vehicle_request.tagIds is not None:
        json_dict.update({"tagIds": vehicle_request.tagIds})

    """
    isPermanent字段
    """
    if vehicle_request.isPermanent == "EXEMPTFIELD":
        del json_dict["isPermanent"]
    elif vehicle_request.isPermanent is not None:
        json_dict.update({"isPermanent": vehicle_request.isPermanent})
    """
    validityStartTime字段
    """
    if vehicle_request.validityStartTime == "EXEMPTFIELD":
        del json_dict["validityStartTime"]
    elif vehicle_request.validityStartTime is not None:
        json_dict.update({"validityStartTime": vehicle_request.validityStartTime})
    """
    validityEndTime字段
    """
    if vehicle_request.validityEndTime == "EXEMPTFIELD":
        del json_dict["validityEndTime"]
    elif vehicle_request.validityEndTime is not None:
        json_dict.update({"validityEndTime": vehicle_request.validityEndTime})
    """
    accessCodeId字段
    """
    if vehicle_request.accessCodeId == "EXEMPTFIELD":
        del json_dict["accessCodes"]
    elif vehicle_request.accessCodeId is not None:
        json_dict['accessCodes'][0].update({"accessCodeId": vehicle_request.accessCodeId})

    """
    accessCodeIsPermanent字段
    """
    if vehicle_request.accessCodeIsPermanent == "EXEMPTFIELD":
        del json_dict["accessCodes"]
    elif vehicle_request.accessCodeIsPermanent is not None:
        json_dict['accessCodes'][0].update({"isPermanent": vehicle_request.accessCodeIsPermanent})
    """
    accessCodeStartTime字段
    """
    if vehicle_request.accessCodeStartTime == "EXEMPTFIELD":
        del json_dict["accessCodes"]
    elif vehicle_request.accessCodeStartTime is not None:
        json_dict['accessCodes'][0].update({"startTime": vehicle_request.accessCodeStartTime})

    """
    accessCodeEndTime字段
    """
    if vehicle_request.accessCodeEndTime == "EXEMPTFIELD":
        del json_dict["accessCodes"]
    elif vehicle_request.accessCodeEndTime is not None:
        json_dict['accessCodes'][0].update({"endTime": vehicle_request.accessCodeEndTime})
    log_info('end vehicle_json_make')
    return json_dict



def vehicle_json_maker():
    """
    staff json生成
    :param user_request:
    :return:
    """
    json_dict = {}
    json_dict.update({"id": None})
    json_dict.update({"platePrefixType": Enum.VehicleEnum.platePrefixType.Other.value})
    json_dict.update({"plateNumber": fake.random_letter()+str(fake.random_int())})
    json_dict.update({"vehicleType": Enum.VehicleEnum.vehicleType.Car.name})
    json_dict.update({"driverName": fake.name()})
    json_dict.update({"billingPolicyId": billingPolicyId})
    json_dict.update({"disabled": False})
    json_dict.update({"tagIds": []})
    json_dict.update({"driverId": None})
    json_dict.update({"remarks": fake.catch_phrase()})
    json_dict.update({"isPermanent": True})
    json_dict.update({"validityStartTime": get_today_timestamp()[0]})
    json_dict.update({"validityEndTime": None})
    json_dict.update({"attachments": []})
    json_dict.update({"accessCodes": [
        {
            "accessCodeId": vehicleAccessCodeId,
            "startTime": get_today_timestamp()[0],
            "endTime": None,
            "isPermanent": True,
            "disabled": False
        }
    ]})


    return json_dict
