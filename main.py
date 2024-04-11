# Can't compare offset-naive and offset-aware datetimes

from datetime import datetime
import pytz

tz = pytz.timezone('America/New_York')

utc = pytz.UTC

dt_aware = datetime(2024, 9, 20, 12, 0, 0, tzinfo=tz).replace(tzinfo=utc)

dt_naive = datetime(2024, 9, 30, 9, 30, 0).replace(tzinfo=utc)

if dt_aware > dt_naive:
    print('dt_aware is greater than dt_naive')
else:
    print('dt_aware is not greater than dt_naive')