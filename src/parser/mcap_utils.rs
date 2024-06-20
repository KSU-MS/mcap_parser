use mcap;
use std::{fs::File, io::Read};

pub fn parse_mcap(file_path: &String) -> (Vec<u64>, Vec<String>, Vec<(String, f64)>) {
    // Open the file from our path
    let file = File::open(file_path);

    // Make some buffers to throw the outputs into
    let mut buffer = Vec::new(); // buffer for the file
    let mut times: Vec<u64> = Vec::new();
    let mut groups: Vec<String> = Vec::new();
    let mut outputs: Vec<(String, f64)> = Vec::new();

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

    let mut num: u16 = 0;

    // Print every message for debug lol
    for msg in messages.unwrap() {
        if num <= 3 {
            println!("data: {:?}", msg.unwrap());
        }

        num += 1;
    }

    return (times, groups, outputs);
}
