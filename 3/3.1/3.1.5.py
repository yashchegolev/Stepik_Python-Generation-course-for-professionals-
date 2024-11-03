from datetime import date
def get_min_max(dates):
    if len(dates) > 0:
        return tuple([min(dates), max(dates)])
    else:
        return tuple()
