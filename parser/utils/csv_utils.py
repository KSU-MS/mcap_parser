import csv


def write_csv_TVN(file_name, data):
    with open(file_name + ".csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        topics = ["Time", "Name", "Value"]
        writer.writerow(topics)

        for point in data:
            for val in point:
                writer.writerow(val)


def write_csv_OMNI(file_name, data, topics):
    with open(file_name + ".csv", mode="w", newline="") as file:
        # Set some gizmos up
        writer = csv.writer(file)
        mod_data = []

        # Add time to the header of the file
        topics.insert(0, "Time")
        writer.writerow(topics)

        for point in data:
            mod_row = []  # Make a holder for this row
            mod_row.append(point[0][0])  # Get the timestamp
            for topic in topics:
                if point[0][1] != topic:  # append None if not the correct signal
                    mod_row.append(None)
                else:
                    for val in point:  # append the values if the first signal is right
                        mod_row.append(val[2])
            mod_data.append(mod_row)  # Add to the final csv

        for row in mod_data:
            writer.writerow(row)
