def minutes_to_seconds(value2):
  minutes = value2
  seconds = minutes*60
  #print(seconds)
  return seconds

def hours_to_seconds(value1):
  hours = value1
  seconds = hours*3600
  #print(seconds)
  return seconds

def time_to_seconds(value1, value2, value3):
  seconds = hours_to_seconds(value1) + minutes_to_seconds(value2) + value3
  print(seconds)