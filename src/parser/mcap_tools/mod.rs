use mcap;
use std::{fs::File, io::Read};

pub fn parse_mcap(file_path: String) {
    // Open the file from our path
    let file = File::open(file_path);

    // Make a buffer to throw the output into
    let mut buffer = Vec::new();

    // Put the file into our buffer
    file.unwrap().read_to_end(&mut buffer).unwrap();

    // Convert the vec buffer into an array refrence
    let byte_slice: &[u8] = &buffer;

    // Get a new vec of all the messages from the raw bytes and ingnore if it doesn't have the end
    // magic bytes
    let messages = mcap::MessageStream::new_with_options(
        byte_slice,
        mcap::read::Options::IgnoreEndMagic.into(),
    );

    // Print every message for debug lol
    for msg in messages.unwrap() {
        println!("{:?}", msg.unwrap());
    }
}
