import csv
from datetime import datetime

from matplotlib import pyplot as plt        # pip install matplotlib

filename = 'data/Grafton_NH_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        # The date is in column 2.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        # The high temperature is in column 3.
        high = int(row[3]) - int(row[4])
        highs.append(high)
        low = int(row[4])
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-poster')
fig, ax = plt.subplots()
ax.bar(dates, bottom=lows, height=highs)

# Format plot.
plt.title("Daily Temperature Ranges", fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()