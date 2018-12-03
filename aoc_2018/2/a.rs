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
			let mut x: u8= c as u8 - 'a' as u8;
			letters[x as usize] += 1;
		}

		/*
		println!("{}", s);
		println!("{:#?}", letters);
		break;
		*/

		for i in 0..26 {
			if letters[i] == 2 {
				twos += 1;
				break;
			}
		}
		
		for i in 0..26 {
			if letters[i] == 3 {
				threes += 1;
				break;
			}
		}

	}

	println!("{}", twos * threes);

}