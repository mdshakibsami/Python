from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time
df = current_datetime.strftime("%d/%m/%y")
tf = current_datetime.strftime("%H:%M:%S")
print( tf ,df )
