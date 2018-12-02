use std::io::{self, Read};


fn main() {
	let mut freq = String::new();
	let stdin = io::stdin();
	let mut handle = stdin.lock();

	handle.read_to_string(&mut freq).expect("please input something");

	let split = freq.split_whitespace();

	let mut sum = 0;
	for s in split {
		let t: i32 = s.trim().parse().expect("");
		sum += t
	}

	println!("{}", sum);
}