use std::io::{self, Read};
use std::collections::HashSet;


fn main() {
	let mut freq = String::new();
	let stdin = io::stdin();
	let mut handle = stdin.lock();
	let mut seen_sums = HashSet::new();

	handle.read_to_string(&mut freq).expect("please input something");

	let mut sum = 0;
	seen_sums.insert(sum);
	let mut b = false;

	loop {
		let split = freq.split_whitespace();
		for s in split {
			let t: i32 = s.trim().parse().expect("");
			sum += t;

			if !seen_sums.insert(sum) {
				println!("{}", sum);
				b = true;
				break;
			}
		}

		if b {
			break;
		}
	}

}