import csv


def write_csv_TVN(file_name, data, output):
    with open(output + file_name + ".csv", mode="w", newline="", buffering=1) as file:
        # Open the file
        writer = csv.writer(file)

        # Ram fuckery prevention
        # buffer = []
        # buf_size = 500

        # Write the header
        topics = ["Time", "Name", "Value"]
        writer.writerow(topics)

        # Iterate thru everything
        for point in data:
            for val in point:
                writer.writerow(val)

                # buffer.append(val)

                # Clear buf if too buff
                # if len(buffer) >= buf_size:
                #     writer.writerows(buffer)
                #     file.flush()
                #     buffer.clear()

        file.flush()


def write_csv_OMNI(file_name, data, topics, output):
    with open(output + file_name + ".csv", mode="w", newline="", buffering=1) as file:
        # Open the guy
        writer = csv.writer(file)

        # Ram fuckery prevention
        # buffer = []
        # buf_size = 500

        # Add time to the header of the file
        topics.insert(0, "Time")
        writer.writerow(topics)

        # Iterate thru the data
        for point in data:
            mod_row = []  # Make a holder for this row
            mod_row.append(point[0][0])  # Get the timestamp
            for topic in topics:
                if point[0][1] != topic:  # append None if not the correct signal
                    mod_row.append(None)
                else:
                    for val in point:  # append the values if the first signal is right
                        mod_row.append(val[2])

            writer.writerow(mod_row)

            # buffer.append(mod_row)

            # Clear buf if too buff
            # if len(buffer) >= buf_size:
            #     writer.writerows(buffer)
            #     file.flush()
            #     buffer.clear()

        file.flush()
