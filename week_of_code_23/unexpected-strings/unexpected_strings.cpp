#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define MOD 1000000007
typedef long long ll;


ll get_key_len(char *c, ll len) {
	if (len % 2) {
		for (ll i = 0; i < len - 1; ++i)
			if (c[i] != c[i + 1])
				return len;
		return 1;
	}

	ll half = len / 2;

	if (memcmp(c, c + half, half) == 0) 
		return get_key_len(c, half);
	else
		return len;
}


int main() {
	char c[1000000] = {0};
	ll m;

	/* scanf("%s", c); */
	/* scanf("%lld", &m); */

	cin >> c >> m;

	ll len = strlen(c);

	ll key_len = get_key_len(c, len);

	ll result = (m / key_len) % MOD;

	cout << result << endl;

	return 0;
}
