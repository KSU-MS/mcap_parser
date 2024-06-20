// Import anything needed
mod mcap_tools;

// An enum for the diffrent output types
pub enum OutputFormats {
    LegacyOmni,
}

// A struct to hold all the basic data needed to parse
pub struct ParserHandaler {
    mcaps: Vec<String>,
    output_dir: String,
    giga_output: bool,
    format: OutputFormats,
}

// The functions for our struct
impl ParserHandaler {
    pub fn init(
        mcap_list: Vec<Option<String>>,
        target_dir: Option<String>,
        is_giga: bool,
        target_format: OutputFormats,
    ) -> Self {
        // Get the output directory and if it isn't real assume ./output
        let target = target_dir.unwrap_or_else(|| String::from("./output"));

        // Make a list for the good mcaps to go into
        let mut list: Vec<String> = Vec::new();

        // Go thru each file and see if they are real and end with .mcap
        for cap in mcap_list {
            if cap.is_some() {
                list.push(cap.unwrap())
            }
        }

        // Return the cleaned up data
        return ParserHandaler {
            mcaps: list,
            output_dir: target,
            giga_output: is_giga,
            format: target_format,
        };
    }

    pub fn test(mcap_target: String, target_dir: String) -> Self {
        let fake_list = vec![mcap_target];

        return ParserHandaler {
            mcaps: fake_list,
            output_dir: target_dir,
            giga_output: true,
            format: OutputFormats::LegacyOmni,
        };
    }

    pub fn parse(self) {
        for cap in self.mcaps {
            mcap_tools::parse_mcap(cap)
        }
    }
}
