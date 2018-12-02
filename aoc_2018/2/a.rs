use std::io::{self, Read};


fn main() {
	let mut input = String::new();
	let stdin = io::stdin();
	let mut handle = stdin.lock();

	handle.read_to_string(&mut input).expect("please input something");

	let split = input.split_whitespace();
	let mut twos = 0;
	let mut threes = 0;
	for s in split {
		let mut letters: [u8; 26] = [0; 26];
		for c in s.chars() {
			let x: i32 = c as i32 - 'a' as i32;
			letters[x] += 1;
		}

		for i in 0..26 {
			if letters[i] == 2 {
				twos += 1;
			}
			if letters[i] == 3 {
				threes += 1;
			}
		}

	}

	println!("{}", twos * threes);

}