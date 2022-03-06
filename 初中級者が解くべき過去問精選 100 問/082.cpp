// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

vector<string> split(string str, char del) {
    int first = 0;
    int last = str.find_first_of(del);

    vector<string> result;

    while (first < str.size()) {
        string subStr(str, first, last - first);

        result.push_back(subStr);

        first = last + 1;
        last = str.find_first_of(del, first);

        if (last == string::npos) {
            last = str.size();
        }
    }

    return result;
}

ll total = 24 * 60 * 60;
vector<ll> table(total);

int main() {
    vector<ll> res;

    while (1) {
        ll n;
        cin >> n;
        if (n == 0) break;

        // 初期化
        rep(i, total) { table[i] = 0; }

        rep(i, n) {
            // 時刻受け取り
            string st, en;
            cin >> st >> en;
            auto st_v = split(st, ':');
            auto en_v = split(en, ':');
            ll hs, ms, ss;
            ll he, me, se;
            hs = stoll(st_v[0]) * 60 * 60;
            ms = stoll(st_v[1]) * 60;
            ss = stoll(st_v[2]);

            he = stoll(en_v[0]) * 60 * 60;
            me = stoll(en_v[1]) * 60;
            se = stoll(en_v[2]);

            table[hs + ms + ss]++;
            table[he + me + se]--;
        }
        rep_s(i, 1, total) { table[i] += table[i - 1]; }
        ll ans = 0;
        rep(i, total) { ans = max(ans, table[i]); }
        res.push_back(ans);
    }
    rep_e(ans, res) { cout << ans << "\n"; }
    return 0;
}