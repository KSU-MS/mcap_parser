/// Preview hovering files:
pub fn preview_files_being_dropped(ctx: &egui::Context) {
    // Get some of the basic imports
    use egui::*;
    use std::fmt::Write as _;

    // Start doing things once someone starts to hover some files over the window
    if !ctx.input(|i| i.raw.hovered_files.is_empty()) {
        // Basic text element = window info stuffs
        let text = ctx.input(|i| {
            let mut text = "Dropping files:\n".to_owned();

            // Show every valid file name being dragged
            for file in &i.raw.hovered_files {
                if let Some(path) = &file.path {
                    write!(text, "\n{}", path.display()).ok();
                } else if !file.mime.is_empty() {
                    write!(text, "\n{}", file.mime).ok();
                } else {
                    text += "\n???";
                }
            }

            // Return the text
            text
        });

        // Dont worry about these guys they are just some styling stuffs and drawing the box
        let painter =
            ctx.layer_painter(LayerId::new(Order::Foreground, Id::new("file_drop_target")));

        let screen_rect = ctx.screen_rect();
        painter.rect_filled(screen_rect, 0.0, Color32::from_black_alpha(192));
        painter.text(
            screen_rect.center(),
            Align2::CENTER_CENTER,
            text, // This is where the text object goes
            TextStyle::Heading.resolve(&ctx.style()),
            Color32::WHITE,
        );
    }
}
