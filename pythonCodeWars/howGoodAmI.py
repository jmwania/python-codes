# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You got an array with your colleges' points. Now calculate the average to your points!

# Return True if you're better, else False!
def better_than_average(class_points, your_points):
  sum = 0
  for point in class_points:
    sum += point
  class_average = sum/len(class_points)
  
  return True if your_points > class_average else False