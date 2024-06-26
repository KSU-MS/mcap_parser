from mcap.reader import make_reader
from mcap_protobuf.decoder import DecoderFactory


def parse_mcap(file):
    # Open the mcap and setup the protobuf decoder
    reader = make_reader(file, decoder_factories=[DecoderFactory()])

    # Setup an array to hold the parsed data and names
    data = []
    topics = []

    # Iterate over each message appending the parts we care about to our array
    for (
        schema,
        channel,
        message,
        proto_msg,
    ) in reader.iter_decoded_messages():
        field_names = [field.name for field in proto_msg.DESCRIPTOR.fields]
        topic_data = []

        # This goes over each feild for the topic
        for name in field_names:
            if name not in topics:
                topics.append(name)

            topic_data.append(
                [
                    message.log_time,
                    name,
                    getattr(proto_msg, name),
                ]
            )

        data.append(topic_data)

    # Return everything
    return data, topics
