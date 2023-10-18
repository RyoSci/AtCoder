#include <bits/stdc++.h>
using namespace std;

ll pow_ll(ll x, ll n) {
    ll ret = 1;
    while (n > 0) {
        if (n & 1) ret *= x;  // n の最下位bitが 1 ならば x^(2^i) をかける
        x *= x;
        n >>= 1;  // n を1bit 左にずらす
    }
    return ret;
}

// modバージョン
#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;

ll pow_mod(ll x, ll n) {
    ll ret = 1;
    while (n > 0) {
        if (n & 1) ret = ret * x % MOD;  // n の最下位bitが 1 ならば x^(2^i)
        をかける
        x = x * x % MOD;
        n >>= 1;  // n を1bit 左にずらす
    }
    return ret;
}

int main() {
    ll x, n;
    cin >> x >> n;
    cout << pow(x, n) << endl;
    return 0;
}