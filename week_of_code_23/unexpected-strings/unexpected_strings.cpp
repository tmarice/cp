#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define MOD 1000000007
typedef long long ll;

bool check_key(char *c, ll len, ll key_len) {
	bool ret = true;

	for (int i = 1; i < len / key_len; ++i)
		ret &= (memcmp(c, c + i*key_len, key_len) == 0);

	return ret;
}

ll get_key_len(char *c, ll len) {
	for (ll key_len = 1; key_len <= len/2; ++key_len)
		if (len % key_len == 0)
			if (check_key(c, len, key_len))
				return key_len;

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
