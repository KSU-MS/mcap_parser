#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")] // hide console window on Windows in release

use eframe::egui;

mod gui;
mod parser;

fn main() -> Result<(), eframe::Error> {
    let mut guy = parser::ParserHandaler::test(
        String::from("/home/ctrl/comp_mcaps/KMS_data/accel/06_14_2024_09_39_26.mcap"),
        String::from("./output"),
    );

    guy.parse();

    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default()
            .with_inner_size([640.0, 240.0]) // wide enough for the drag-drop overlay text
            .with_drag_and_drop(true),
        ..Default::default()
    };
    eframe::run_native(
        "It parse the cap with the m",
        options,
        Box::new(|_cc| Box::<gui::ParserApp>::default()),
    )
}
