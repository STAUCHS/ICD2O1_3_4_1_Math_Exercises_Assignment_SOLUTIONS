#-------------------------------------------------------------------------
# Name:         Hours
# Purpose:		Calculates the number of days and hours given the total hours
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Get the number of hours from user
hours = int(input("Enter the number of hours: "))

# Calculate the days and remaining hours
days = hours // 24
leftover_hours = hours % 24

# Output the days and remaining hours
print(hours, "hours = ", days, "day(s) and", leftover_hours, "hour(s).")