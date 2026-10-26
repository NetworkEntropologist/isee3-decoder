
from datetime import timedelta

def format_number(number:str) -> int:
    """Remove thousand separator from numbers"""

    if ',' in number:
        return int(number.replace(',',''))

    return int(number)

def mission_time(time:str) -> timedelta:
    """Convert a string time to a mission time offset"""

    sign = -1 if time.startswith("-") else 1
    _time_components = time.lstrip("+-").split(":")
    if len(_time_components) > 3:
        return sign * timedelta(hours=int(_time_components[0]), minutes=int(_time_components[1]), seconds=float(_time_components[2]))
    else:
        return sign * timedelta(hours=0, minutes=int(_time_components[0]), seconds=float(_time_components[1]))

def regular_time(td: timedelta, decimals: int = 2) -> str:
    """Convert a mission time offset to a time string"""

    total = td.total_seconds()
    sign = '-' if total < 0 else ''
    total = abs(total)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{sign}{int(h):02d}:{int(m):02d}:{s:0{3 + decimals}.{decimals}f}"
