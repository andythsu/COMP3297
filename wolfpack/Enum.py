from enum import Enum


class UserRoleEnum(Enum):
    SCRUM_MASTER = 0
    PRODUCT_OWNER = 1
    DEVELOPER = 2
    @staticmethod
    def getNameByValue(val):
        val = int(val)
        if val == 0:
            return UserRoleEnum.SCRUM_MASTER
        elif val == 1:
            return UserRoleEnum.PRODUCT_OWNER
        elif val == 2:
            return UserRoleEnum.DEVELOPER
        else:
            raise Exception("value doesn't exist in UserRoleEnum class")


class PbiStatusEnum(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DONE = 2
    NOT_FINISHED = 3

    @staticmethod
    def getNameByValue(val):
        val = int(val)
        if val == 0:
            return "NOT_STARTED"
        elif val == 1:
            return "IN_PROGRESS"
        elif val == 2:
            return "DONE"
        elif val == 3:
            return "NOT_FINISHED"
        else:
            raise Exception("value doesn't exist in PbiStatusEnum class")


class SprintStatusEnum(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DONE = 2

    @staticmethod
    def getNameByValue(val):
        val = int(val)
        if val == 0:
            return 'NOT_STARTED'
        elif val == 1:
            return 'IN_PROGRESS'
        elif val == 2:
            return 'DONE'
        else:
            raise Exception("value doesn't exist in SprintStatusEnum class")


class SprintTaskStatusEnum(Enum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2

    @staticmethod
    def getNameByValue(val):
        val = int(val)
        if val == 0:
            return "TO_DO"
        elif val == 1:
            return "IN_PROGRESS"
        elif val == 2:
            return "DONE"
        else:
            raise Exception("value doesn't exist in SprintTaskStatusEnum class")


class SessionStorageEnum(Enum):
    U_ROLE = "u_role"
    U_ID = "u_id"

