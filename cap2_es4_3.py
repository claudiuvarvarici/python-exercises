def r():
	start_time = '6:00'
	time_easy_mile = 495
	time_tempo_mile = 432
	hour_to_seconds=int(start_time[0])*3600
	minutes_to_seconds=int(start_time[2:])*60
	seconds=hour_to_seconds+minutes_to_seconds
	final_time = seconds + time_easy_mile + 3*time_tempo_mile + time_easy_mile
	final_partial_minutes = str(final_time/3600)
	final_minutes = float(final_partial_minutes[1:3])*60
	print('Start time:', start_time)
	end_time = str(final_time//3600)+':'+str(int(final_minutes))
	print('Finish time:', end_time)
r()