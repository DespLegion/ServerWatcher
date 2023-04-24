from datetime import timedelta


def format_timedelta(delta: timedelta) -> str:
    """Formats a timedelta duration to [N days] %H:%M:%S format"""
    seconds = int(delta.total_seconds())

    secs_in_a_day = 86400
    secs_in_a_hour = 3600
    secs_in_a_min = 60

    days, seconds = divmod(seconds, secs_in_a_day)
    hours, seconds = divmod(seconds, secs_in_a_hour)
    minutes, seconds = divmod(seconds, secs_in_a_min)

    # time_fmt = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    time_fmt = f"{hours:02d}:{minutes:02d}"

    if days > 0:
        # suffix = "s" if days > 1 else ""
        return f"{days}d {time_fmt}"

    return time_fmt
