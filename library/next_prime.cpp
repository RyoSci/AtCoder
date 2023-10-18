#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <map>
#include <vector>
#define fi first
#define se second
#define rep(i, n) for (int i = 0; i < n; i++)
using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;
const int mod = 1000000007;

// "https://gist.github.com/snuke/de2cceaf9496610226253f23d9fbcc59"
// 引数1にそれ以上の素数、引数2に個数を指定する

map<ll, ll> in, pr;
vector<P> p;

ll rnd() { return (ll)rand() << 31 | rand(); }
ll mul(ll x, ll y, ll m) {
    ll res = 0;
    while (y) {
        if (y & 1) res = (res + x) % m;
        x = (x << 1) % m;
        y >>= 1;
    }
    return res;
}
ll jo(ll x, ll y, ll m) {
    ll res = 1;
    while (y) {
        if (y & 1) res = mul(res, x, m);
        y >>= 1;
        x = mul(x, x, m);
    }
    return res;
}
const int MRP = 100;
bool MillerRabin(ll x) {
    if (x <= 1) return false;
    if (x == 2) return true;
    if (!(x & 1)) return false;
    ll d = x - 1;
    while (!(d & 1)) d >>= 1;
    rep(ti, MRP) {
        ll a = rnd() % (x - 1) + 1;
        ll t = d;
        ll y = jo(a, d, x);
        while (t != x - 1 && y != 1 && y != x - 1) {
            y = mul(y, y, x);
            t <<= 1;
        }
        if (y != x - 1 && !(t & 1)) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    srand((unsigned)time(NULL));
    int cnt = 0;
    ll x = 1;
    if (argc > 1) sscanf(argv[1], "%lld", &x);
    int tm = 10;
    if (argc > 2) sscanf(argv[2], "%d", &tm);
    while (cnt < tm) {
        // ll x = rnd();
        if (MillerRabin(x)) {
            cout << x << endl;
            cnt++;
        }
        x++;
    }
    return 0;
}