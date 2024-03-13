"""
每个字段后跟的是，每种用户类型对应的传的参数
用户类型为：All、staff、visitor、vendor、tenant
参数为：0（不传），1（必传），2（可能会传）
"""


class Vehicle:
    def __init__(self, id=None,vehicleType=None, platePrefixType=None, plateNumber=None, parkingMode= None, billingPolicyId=None,
                 driverName = None, validityStartTime: int = None,validityEndTime: int = None,disabled : bool= None,
                 isPermanent: bool = None,remarks=None, tagIds=None, accessCodeId=None,accessCodeIsPermanent=None,accessCodeStartTime=None,accessCodeEndTime=None):
        self.id = id
        self.platePrefixType = platePrefixType
        self.plateNumber = plateNumber
        self.vehicleType = vehicleType
        self.parkingMode = parkingMode
        self.billingPolicyId = billingPolicyId
        self.driverName = driverName
        self.validityStartTime = validityStartTime
        self.validityEndTime = validityEndTime
        self.isPermanent = isPermanent
        self.remarks = remarks
        self.tagIds = tagIds
        self.disabled = disabled
        self.accessCodeId = accessCodeId
        self.accessCodeIsPermanent = accessCodeIsPermanent
        self.accessCodeStartTime = accessCodeStartTime
        self.accessCodeEndTime = accessCodeEndTime

    def __str__(self):
        return (f"Vehicle(id={self.id},vehicleType={self.vehicleType}, platePrefixType={self.platePrefixType}, "
                f"plateNumber={self.plateNumber},validityStartTime={self.validityStartTime}, "
                f"validityEndTime={self.validityEndTime}, isPermanent={self.isPermanent}, parkingMode={self.parkingMode},"
                f"billingPolicyId={self.billingPolicyId}, driverName={self.driverName},"
                f"remarks={self.remarks}, tagIds={self.tagIds}, disabled={self.disabled}"
)


class VehicleCreate:
    def __init__(self):
        self.vehicle = Vehicle()

    def withid(self, id):
        self.vehicle.id = id
        return self

    def withvehicleType(self, vehicleType):
        self.vehicle.vehicleType = vehicleType
        return self

    def withplatePrefixType(self, platePrefixType: int):
        self.vehicle.platePrefixType = platePrefixType
        return self

    def withplateNumber(self, plateNumber: list):
        self.vehicle.plateNumber = plateNumber
        return self

    def withparkingMode(self, parkingMode):
        self.vehicle.parkingMode = parkingMode
        return self

    def withbillingPolicyId(self, billingPolicyId):
        self.vehicle.billingPolicyId = billingPolicyId
        return self

    def withdriverName(self, driverName):
        self.vehicle.driverName = driverName
        return self

    def withValidityStartTime(self, validityStartTime: int):
        self.vehicle.validityStartTime = validityStartTime
        return self

    def withValidityEndTime(self, validityEndTime: int):
        self.vehicle.validityEndTime = validityEndTime
        return self

    def withIsPermanent(self, isPermanent: bool):
        self.vehicle.isPermanent = isPermanent
        return self

    def withdisabled(self, disabled):
        self.vehicle.disabled = disabled
        return self

    def withRemarks(self, remarks):
        self.vehicle.remarks = remarks
        return self

    def withTagIds(self, tagIds: list):
        self.vehicle.tagIds = tagIds
        return self

    def withaccessCodeId(self, accessCodeId):
        self.vehicle.accessCodeId = accessCodeId
        return self

    def withaccessCodeIsPermanent(self, accessCodeIsPermanent: int):
        """
        user AC是否永久
        :param accessCodeIsPermanent: 是否永久
        :return:
        """
        self.vehicle.accessCodeIsPermanent = accessCodeIsPermanent
        return self

    def withaccessCodeStartTime(self, accessCodeStartTime: int):
        """
        user AC开始时间
        :param accessCodeStartTime: AC开始时间戳
        :return:
        """
        self.vehicle.accessCodeStartTime = accessCodeStartTime
        return self

    def withaccessCodeEndTime(self, accessCodeEndTime: int):
        """
        user AC结束时间
        :param accessCodeEndTime: AC结束时间戳
        :return:
        """
        self.vehicle.accessCodeEndTime = accessCodeEndTime
        return self



    def build(self):
        return self.vehicle
