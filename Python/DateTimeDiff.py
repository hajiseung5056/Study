from datetime import datetime

def diff(sStartTime):
    now = datetime.now()
    past = datetime.strptime(sStartTime,"%Y%m%d %H%M%S")

    diff = now - past
    return diff
