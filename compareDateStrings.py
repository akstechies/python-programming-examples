# Assuming date1 and date2 are in mm-dd-yyyy format as strings
date1_str = "08-25-2023"
date2_str = "09-15-2023"

# Convert date strings to yyyy-mm-dd format
date1_yyyy_mm_dd = date1_str[6:] + '-' + date1_str[:5]
date2_yyyy_mm_dd = date2_str[6:] + '-' + date2_str[:5]

# Compare the dates as strings
if date1_yyyy_mm_dd > date2_yyyy_mm_dd:
    latest_date = date1_str
else:
    latest_date = date2_str

print("The latest date is:", latest_date)
