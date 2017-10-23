import arrow
import acp_times
#use the website and transfer info. Change the Date from website in string and the open time
#and also the checkpoint if different but test different chckpoint meters


#print("THE RESULT" ,acp_times.open_time(400, 1000, '2013-09-30T15:34:00.000-07:00'))
assert arrow.get(acp_times.open_time(400, 1000, '2013-09-30T15:34:00.000-07:00')) ==  arrow.get("2013-10-01T03:42:00-07:00")
#print("THE RESULT" , (acp_times.close_time(400, 1000, '2013-09-30T15:34:00.000-07:00')))
assert arrow.get(acp_times.close_time(400, 1000, '2013-09-30T15:34:00.000-07:00')) ==  arrow.get("2013-10-01T18:14:00-07:00")

print("Open time", acp_times.open_time(900, 1000, '2013-09-30T00:00:00.000-07:00'))
assert arrow.get(acp_times.open_time(900, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-01T05:31:00-07:00")
print("Close time", acp_times.close_time(900, 1000, '2013-09-30T00:00:00.000-07:00'))
assert arrow.get(acp_times.close_time(900, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-02T18:15:00-07:00")
##assert acp_times.open_time(200, 600, '2013-09-30T15:34:00.000-07:00') ==  "2013-09-30T21:27:00-07:00"
##assert acp_times.close_time(200, 600, '2013-09-30T15:34:00.000-07:00') ==  "2013-10-01T03:42:00-07:00"


#control longer than allowed
assert acp_times.open_time(900, 600, '2013-09-30T00:00:00.000-07:00') == ""
assert acp_times.close_time(900, 600, '2013-09-30T00:00:00.000-07:00') == ""

#fence post
#200
assert arrow.get(acp_times.open_time(200, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-09-30T05:53:00-07:00")
assert arrow.get(acp_times.close_time(200, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-09-30T13:20:00-07:00")
#400
assert arrow.get(acp_times.open_time(400, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-09-30T12:08:00-07:00")
assert arrow.get(acp_times.close_time(400, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-01T02:40:00-07:00")
#600
assert arrow.get(acp_times.open_time(600, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-09-30T18:48:00-07:00")
assert arrow.get(acp_times.close_time(600, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-01T16:00:00-07:00")
#1000
assert arrow.get(acp_times.open_time(1000, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-01T09:05:00-07:00")
assert arrow.get(acp_times.close_time(1000, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-03T03:00:00-07:00")


#control > brevet 
assert arrow.get(acp_times.open_time(1005, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-01T09:05:00-07:00")
assert arrow.get(acp_times.close_time(1005, 1000, '2013-09-30T00:00:00.000-07:00')) ==  arrow.get("2013-10-03T03:00:00-07:00")




