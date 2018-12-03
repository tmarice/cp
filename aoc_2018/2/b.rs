use std::io::{self, Read};


fn main() {
	let mut input = String::new();
	let stdin = io::stdin();
	let mut handle = stdin.lock();

	handle.read_to_string(&mut input).expect("please input something");

	let split = input.split_whitespace();
	let mut v = Vec::new();
	for s in split {
		let chars: Vec<char> = s.chars().collect();
		v.push(chars);
	}

	let n = v.len();
	let mut result = String::new();

	for i in 0..n-1 {
		for j in i+1..n {

			let mut diff = 0;
			let str_a = &v[i as usize];
			let str_b = &v[j as usize];
			let d = v[i as usize].len();

			for k in 0..d {
				if str_a[k] != str_b[k] {
					diff += 1;
				}
			}
			if diff == 1 {
				for k in 0..d {
					if str_a[k] == str_b[k] {
						result.push(str_a[k]);
					}
				}
			}
		}
	}

	println!("{}", result);

}