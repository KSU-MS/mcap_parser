import sys
from parser.parse_man import parse_folder


def main():
    parse_folder(sys.argv[1])

    # Make a file to yeet shit in and init a csv writer
    # filename = Path(sys.argv[1]).stem + ".csv"
    # with open(filename, mode="w", newline="") as file:
    #     writer = csv.writer(file)
    #
    #     writer.writerow(topics)
    #
    #     # TODO: Basically the reason why this guy is so fucking slow is that it iterates thru the entire
    #     # bloody mcap looking for one message, fills out that collum, and then goes back to the start, needless
    #     # to say re-reading the same file around 160 or however many diffrent signals you have is going to take
    #     # a minute, so instead ill write something that just iterates msg by msg, logging everything with a
    #     # comical amount of comas and want to kill my self
    #     for topic in topics:
    #         msg_dict = {}
    #         # for schema, channel, message, proto_msg in reader.iter_decoded_messages(
    #         #     topics=[topic]
    #         # ):
    #         #     res = [f.name for f in proto_msg.DESCRIPTOR.fields]
    #         #     for name in res:
    #         #         if name not in msg_dict:
    #         #             msg_dict[name] = []
    #         #         signal_data = [
    #         #             message.log_time,
    #         #             getattr(proto_msg, name),
    #         #         ]  # No need for res[name], as name is already the field name
    #         #         msg_dict[name].append(signal_data)
    #         # writer.writerow(msg_dict)
    #         for schema, channel, message, proto_msg in reader.iter_decoded_messages(
    #             topics=[topic]
    #         ):
    #             res = [f.name for f in proto_msg.DESCRIPTOR.fields]
    #             print(message)


if __name__ == "__main__":
    main()