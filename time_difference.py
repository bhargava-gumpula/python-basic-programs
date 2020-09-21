def time_difference(start, end):
   start_time = start.split(':')
   end_time = end.split(':')
   total_hours = int(end_time[0]) - int(start_time[0])
   total_minutes = int(end_time[1]) - int(start_time[1])
   return total_hours, total_minutes

start = raw_input("Start Time:")
end = raw_input("End time:")
total_hours, total_minutes = time_difference(start, end)
print ("You have read for %d hours and %d minutes") % (total_hours, total_minutes)
