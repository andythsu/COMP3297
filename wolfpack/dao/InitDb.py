from wolfpack.Enum import UserRoleEnum, PbiStatusEnum, SprintStatusEnum, SprintTaskStatusEnum
from wolfpack.dao import UserDao, ProjectDao, ProductBacklogItemDao, SprintBacklogDao, SprintTaskDao
import datetime


def init():
    print("populating scrum master table...")
    jack_id = UserDao.insert(name="Jack", role=UserRoleEnum.SCRUM_MASTER)

    print("populating project table...")
    project_1 = ProjectDao.insert(title="project 1", description="this is project 1", scrumMasterId=jack_id)
    project_2 = ProjectDao.insert(title="project 2", description="this is project 2", scrumMasterId=jack_id)

    print("populating developer table...")
    tom_id = UserDao.insert(name="Tom", role=UserRoleEnum.DEVELOPER, projectId=project_1)

    print("populating pbi for project 1...")
    project_1_pbi_1 = ProductBacklogItemDao.insert(
        size=6,
        priority=2,
        status=PbiStatusEnum.IN_PROGRESS.value,
        userStory="hello HK",
        projectId=project_1)
    project_1_pbi_2 = ProductBacklogItemDao.insert(
        size=5,
        priority=1,
        status=PbiStatusEnum.NOT_STARTED.value,
        userStory="hello world",
        projectId=project_1)

    print("populating sprints for project 1...")
    project_1_sprint = SprintBacklogDao.insert(
        name="sprint 1",
        startDate=datetime.date.today(),
        endDate=datetime.date.today() + datetime.timedelta(days=14),
        maxHours=50,
        status=SprintStatusEnum.IN_PROGRESS.value,
        projectId=project_1
    )

    print("populating sprint task for project 1 sprint 1 pbi 1...")
    project_1_sprint_1_pbi_1_task_1 = SprintTaskDao.insert(
        title="sprint task 1",
        description="sprint task description",
        status=SprintTaskStatusEnum.TO_DO.value,
        effortHours=5,
        sprintId=project_1_sprint,
        developerId=tom_id,
        pbiId=project_1_pbi_1
    )

    print("done populating all tables")



