from datetime import datetime

def get_runtime(starttime):
    now = datetime.now()
    past = datetime.strptime(starttime,"%Y%m%d %H%M%S")

    runtime = now - past
    str_runtime = str(runtime)
    
    return str_runtime