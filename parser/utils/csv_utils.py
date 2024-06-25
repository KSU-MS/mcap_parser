import csv


def write_csv_TVN(file_name, data):
    with open(file_name + ".csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        topics = ["Time", "Name", "Value"]
        writer.writerow(topics)

        for point in data:
            writer.writerow(point)


# def write_csv_OMNI(file_name, data, topics):
#     with open(file_name + ".csv", mode="w", newline="") as file:
#         writer = csv.writer(file)
#
#         writer.writerow(topics)
#
#         for point in data:
#             writer.writerow(point)
