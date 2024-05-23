/*
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
*/
use std::{
    env,
    fs,
    path::{Path, PathBuf},
    process::Command,
    borrow::Cow,
};
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
struct Args {
    #[structopt()]
    files_or_texts: Vec<String>,
}

fn main() {
    let args = Args::from_args();

    let input = args.files_or_texts
        .iter()
        .map(|input| read_file(input).unwrap_or_else(|err| {
            eprintln!("Error reading {}: {}", input, err);
            String::new()
        }))
        .collect::<Vec<_>>()
        .join("\n");

    let output = generate_text(&input);
    println!("{}", output.text);
    write_results(&input, &output.text).unwrap();
}

fn read_file<P: AsRef<Path>>(file: P) -> Result<String, std::io::Error> {
    fs::read_to_string(file)
}

fn generate_text(input: &str) -> genai::GenerateContentResponse {
    let api_key = match env::var("GOOGLE_API_KEY") {
        Ok(api_key) => api_key,
        Err(_) => panic!("No GOOGLE_API_KEY environment variable set"),
    };
    genai::configure(api_key);

    let model = genai::GenerativeModel::new("gemini-pro");
    model.generate_content(&genai::GenerateContentRequest {
        prompt: Cow::Borrowed(input),
        content_type: genai::ContentType::Text,
    })
}

fn write_results(input: &str, output: &str) -> Result<(), std::io::Error> {
    let mut path = PathBuf::from("output.txt");

    // create file if it doesn't exist
    if !path.exists() {
        match Command::new("touch")
            .arg(&path)
            .output()
        {
            Ok(_) => println!("created output file"),
            Err(e) => Err(std::io::Error::new(std::io::ErrorKind::Other, e))?,
        }
    }

    fs::write(&path, format!("{}{}", input, output))
}
