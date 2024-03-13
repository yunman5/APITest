"""
每个字段后跟的是，每种用户类型对应的传的参数
用户类型为：All、staff、visitor、vendor、tenant
参数为：0（不传），1（必传），2（可能会传）
"""


class User:
    def __init__(self, userType: str, name=None, enableState=None, dcsAccessZoneIds: list = None, endDCSAutoZoneId=None,
                 validityType: int = None, validityStartTime: int = None,
                 validityEndTime: int = None,
                 isPermanent: bool = None, tenantCompanyId=None,
                 company=None, profilePhotoBase64=None, profilePhotoFileId=None, areaCode=None, contact=None, pin=None,
                 email=None, remarks=None, tagIds=None, cardIds: list = None, accessRule=None,
                 dcsProfileId=None, defaultZoneIds: list = None, startDCSAutoZoneId=None,
                 replacementId=None, isCovering=None, transferSourceUserId=None, faceFileBase64=None, faceFileId=None,
                 departmentId=None, accessCodeId=None,accessCodeIsPermanent=None,accessCodeStartTime=None,accessCodeEndTime=None):
        self.name = name
        self.defaultZoneIds = defaultZoneIds  # All 1
        self.validityType = validityType  # All 1
        self.validityStartTime = validityStartTime  # All 1
        self.validityEndTime = validityEndTime  # All 1
        self.isPermanent = isPermanent  # All 1
        self.tenantCompanyId = tenantCompanyId  # staff 0/visitor 0/vendor 0/tenant 1
        self.company = company  # staff 0/visitor 0/vendor 0/tenant 1
        self.departmentId = departmentId  # staff 1/visitor 2/vendor 2/tenant 0
        self.faceFileBase64 = faceFileBase64  # All 1
        self.faceFileId = faceFileId
        self.profilePhotoBase64 = profilePhotoBase64  # All 1
        self.profilePhotoFileId = profilePhotoFileId  # All 1
        self.areaCode = areaCode  # All 1
        self.contact = contact  # All 1
        self.pin = pin  # All 1
        self.email = email  # All 1
        self.remarks = remarks  # All 1
        self.enableState = enableState  # All 1
        self.tagIds = tagIds  # All 1
        self.cardIds = cardIds  # All 1
        self.userType = userType  # All 1
        self.accessRule = accessRule  # staff 0/visitor 1/vendor 0/tenant 0
        self.dcsProfileId = dcsProfileId  # All 1
        self.startDCSAutoZoneId = startDCSAutoZoneId  # All 1
        self.endDCSAutoZoneId = endDCSAutoZoneId  # All 1
        self.dcsAccessZoneIds = dcsAccessZoneIds  # All 1
        self.isCovering = isCovering  # All 0
        self.transferSourceUserId = transferSourceUserId  # All 0
        self.replacementId = replacementId  # All 0
        self.accessCodeId = accessCodeId  # All 0
        self.accessCodeIsPermanent = accessCodeIsPermanent  # All 0
        self.accessCodeStartTime = accessCodeStartTime  # All 0
        self.accessCodeEndTime = accessCodeEndTime  # All 0

    def __str__(self):
        return (f"User(name={self.name}, userType={self.userType}, "
                f"validityType={self.validityType},validityStartTime={self.validityStartTime}, "
                f"validityEndTime={self.validityEndTime}, isPermanent={self.isPermanent}, tenantCompanyId={self.tenantCompanyId}, "
                f"company={self.company}, profilePhotoBase64={self.profilePhotoBase64}, profilePhotoFileId={self.profilePhotoFileId}, "
                f"areaCode={self.areaCode}, contact={self.contact}, pin={self.pin}, email={self.email}, remarks={self.remarks}, "
                f"enableState={self.enableState}, tagIds={self.tagIds}, cardIds={self.cardIds}, accessRule={self.accessRule}, "
                f"dcsProfileId={self.dcsProfileId}, startDCSAutoZoneId={self.startDCSAutoZoneId}, endDCSAutoZoneId={self.endDCSAutoZoneId}, "
                f"dcsAccessZoneIds={self.dcsAccessZoneIds}, replacementId={self.replacementId}, isCovering={self.isCovering}, "
                f"transferSourceUserId={self.transferSourceUserId}, faceFileBase64={self.faceFileBase64}, faceFileId={self.faceFileId}, "
                f"departmentId={self.departmentId},")


class UserCreate:
    def __init__(self, userType: str):
        self.user = User(userType)

    def withName(self, Name):
        self.user.name = Name
        return self

    def withEnableState(self, EnableState: int):
        self.user.enableState = EnableState
        return self

    def withDcsAccessZoneIds(self, DcsAccessZoneIds: list):
        self.user.dcsAccessZoneIds = DcsAccessZoneIds
        return self

    def withEndDCSAutoZoneId(self, EndDCSAutoZoneId):
        self.user.endDCSAutoZoneId = EndDCSAutoZoneId
        return self

    def withDefaultZoneIds(self, DefaultZoneIds):
        self.user.DefaultZoneIds = DefaultZoneIds
        return self

    def withvalidityType(self, validityType: int):
        self.user.validityType = validityType
        return self

    def withValidityStartTime(self, validityStartTime: int):
        self.user.validityStartTime = validityStartTime
        return self

    def withValidityEndTime(self, validityEndTime: int):
        self.user.validityEndTime = validityEndTime
        return self

    def withIsPermanent(self, isPermanent: bool):
        self.user.isPermanent = isPermanent
        return self

    def withTenantCompanyId(self, tenantCompanyId):
        self.user.tenantCompanyId = tenantCompanyId
        return self

    def withCompany(self, company):
        self.user.company = company
        return self

    def withDepartmentId(self, departmentId):
        self.user.departmentId = departmentId
        return self

    def withFaceFileBase64(self, faceFileBase64):
        self.user.faceFileBase64 = faceFileBase64
        return self

    def withFaceFileId(self, faceFileId):
        self.user.faceFileId = faceFileId
        return self

    def withProfilePhotoBase64(self, profilePhotoBase64):
        self.user.profilePhotoBase64 = profilePhotoBase64
        return self

    def withProfilePhotoFileId(self, profilePhotoFileId):
        self.user.profilePhotoFileId = profilePhotoFileId
        return self

    def withAreaCode(self, areaCode):
        self.user.areaCode = areaCode
        return self

    def withContact(self, contact):
        self.user.contact = contact
        return self

    def withPin(self, pin):
        self.user.pin = pin
        return self

    def withEmail(self, email):
        self.user.email = email
        return self

    def withRemarks(self, remarks):
        self.user.remarks = remarks
        return self

    def withTagIds(self, tagIds: list):
        self.user.tagIds = tagIds
        return self

    def withCardIds(self, cardIds: list):
        self.user.cardIds = cardIds
        return self

    def withAccessRule(self, accessRule):
        self.user.accessRule = accessRule
        return self

    def withDcsProfileId(self, dcsProfileId):
        self.user.dcsProfileId = dcsProfileId
        return self

    def withStartDCSAutoZoneId(self, startDCSAutoZoneId):
        self.user.startDCSAutoZoneId = startDCSAutoZoneId
        return self

    def withIsCovering(self, isCovering):
        self.user.isCovering = isCovering
        return self

    def withTransferSourceUserId(self, transferSourceUserId):
        self.user.transferSourceUserId = transferSourceUserId
        return self

    def withReplacementId(self, replacementId):
        self.user.replacementId = replacementId
        return self

    def withaccessCodeId(self, accessCodeId):
        self.user.accessCodeId = accessCodeId
        return self

    def withaccessCodeIsPermanent(self, accessCodeIsPermanent: int):
        """
        user AC是否永久
        :param accessCodeIsPermanent: 是否永久
        :return:
        """
        self.user.accessCodeIsPermanent = accessCodeIsPermanent
        return self

    def withaccessCodeStartTime(self, accessCodeStartTime: int):
        """
        user AC开始时间
        :param accessCodeStartTime: AC开始时间戳
        :return:
        """
        self.user.accessCodeStartTime = accessCodeStartTime
        return self

    def withaccessCodeEndTime(self, accessCodeEndTime: int):
        """
        user AC结束时间
        :param accessCodeEndTime: AC结束时间戳
        :return:
        """
        self.user.accessCodeEndTime = accessCodeEndTime
        return self



    def build(self):
        return self.user
