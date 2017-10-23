
import acp_times
#use the website and transfer info. Change the Date from website in string and the open time
#and also the checkpoint if different but test different chckpoint meters
assert acp_times.open_time(400, 1000, '2013-09-30T15:34:00.000-07:00') ==  "2013-10-01T03:42:00.000-07:00"


assert acp_times.open_time(200, 600, '2013-09-30T15:34:00.000-07:00') ==  "2013-09-30T21:27:00.000-07:00"

assert acp_times.open_time(200, 600, '2017-12-12T15:34:00.000-07:00') ==  "2017-13-30T10:20:00.000-07:00"
