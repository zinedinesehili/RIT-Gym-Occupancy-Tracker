import pandas as pd
import matplotlib.pyplot as plt

data_file = "synthetic_data.csv"
plot_file = "occupancy_plot.png"

occupancy_df = pd.read_csv(data_file)

xdata = [
    "06:00","06:30",
    "07:00","07:30",
    "08:00","08:30",
    "09:00","09:30",
    "10:00","10:30",
    "11:00","11:30",
    "12:00","12:30",
    "13:00","13:30",
    "14:00","14:30",
    "15:00","15:30",
    "16:00","16:30",
    "17:00","17:30",
    "18:00","18:30",
    "19:00","19:30",
    "20:00","20:30",
    "21:00","21:30",
    "22:00","22:30",
    "23:00"
]
# need to get the average for each hour
# here, I am going to add the occupancy of each interval to 
# that spot in the array, then get the average at the end
average_occupancy = [0] * 35 
line_counter = 0
for occupancy in occupancy_df['Occupancy']:
    average_occupancy[line_counter] += occupancy
    line_counter += 1
    if line_counter >= 35:
        line_counter = 0

num_days = len(occupancy_df) // 35

for occupancy in average_occupancy:
    occupancy = occupancy/num_days

plt.figure(figsize=(10, 5))
plt.plot(range(35), average_occupancy)  # numeric x so ticks behave nicely


hourly_tick_positions = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
hourly_tick_labels = [
    "6 AM","7 AM","8 AM","9 AM","10 AM","11 AM",
    "12 PM","1 PM","2 PM","3 PM","4 PM","5 PM",
    "6 PM","7 PM","8 PM","9 PM","10 PM","11 PM"
]

plt.xticks(hourly_tick_positions, hourly_tick_labels, rotation=45)
plt.xlabel("Time of Day")
plt.ylabel("Average Occupancy")
plt.title("Average Gym Occupancy by Time of Day")
plt.tight_layout()
plt.savefig(plot_file, dpi = 600, bbox_inches = 'tight')