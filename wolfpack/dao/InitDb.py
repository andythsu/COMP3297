from wolfpack.models import ScrumMaster, Developer


def init():
    ScrumMaster(name="Jack", role="SM").save()
    ScrumMaster(name="Tom", role="SM").save()


init()
