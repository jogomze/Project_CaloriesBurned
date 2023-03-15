#The following equation estimates the average calories burned for a person when exercising, which is based on a scientific journal article
#calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368
#Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output the average calories burned for a person.


age = float(input("\nWhat is your age?\n"))

weight = float(input("\nWhat is your weight (lbs)?\n"))

heartRate = float(input("\nWhat is your heart rate during exercise (BPM)?\n"))

time = float(input("\nFor how long did you exercise (minutes)?\n"))


calories = float(((age * 0.2757) + (weight * 0.03295) + (heartRate * 1.0781) - 75.4991) * time / 8.368)

print(f"You burned: {calories:.2f} calories")