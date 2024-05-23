```rust
use std::{fs, io::Write};
use regex::Regex;

const TIME_REGEX: &str = "\\d{1,2}:\\d{1,2} \\wM";
const REPEAT_REGEX: &str = "(\\w+ \\d{1,2}:\\d{1,2} \\wM)$";
const TO_REMOVE_REGEX: &str = "(\\w+ \\d{1,2}:\\d{1,2} \\wM)\\s+\\((\\w+ \\d{1,2}:\\d{1,2} \\wM)\\)";

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = fs::read_to_string("wtt.txt")?;
    let mut contents = contents.replace(" ", "");
    contents = contents.replace("\n", "");

    let re = Regex::new(TIME_REGEX)?;
    let re2 = Regex::new(REPEAT_REGEX)?;
    let re3 = Regex::new(TO_REMOVE_REGEX)?;

    for cap in re.captures_iter(&contents) {
        let start = &cap[0];
        if re2.is_match(start) {
            contents = contents.replace(start, &start[..start.len() - 3]);
        }
    }

    for cap in re3.captures_iter(&contents) {
        contents = contents.replace(&cap[1], &cap[2]);
    }

    contents = contents.replace(" ", "\n");

    let mut file = fs::File::create("fixed.txt")?;
    file.write_all(contents.as_bytes())?;

    Ok(())
}
```
