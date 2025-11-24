import time as time
import datetime as datetime


def print_time_sec():
    sec_current = time.time()
    print(
        f"Seconds since January 1, 1970: {sec_current:,.4f} "
        f"or {sec_current:.2e} in scientific notation"
    )


def print_date():
    date_today = datetime.date.today()
    print(f"{date_today:%B %d %Y}")


print_time_sec()
print_date()