// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
using namespace atcoder;
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    vector<string> s(3);
    for (ll i = 0; i < 3; i++) cin >> s[i];
    set<char> cnt;
    rep(i, 3) rep_e(c, s[i]) cnt.insert(c);

    if (cnt.size() > 10) {
        cout << "UNSOLVABLE"
             << "\n";
        return 0;
    }

    string alphabets = "";
    rep_e(c, cnt) alphabets += c;

    vector<ll> a(10, 0);
    rep(i, 10) a[i] = i;

    do {
        map<char, char> d;
        rep(i, cnt.size()) d[alphabets[i]] = a[i] + '0';

        // rep_e(e, d) { cout << e.first << ' ' << e.second << "\n"; }

        vector<string> t = s;
        bool flag = false;
        rep(i, 3) {
            rep(j, t[i].size()) t[i][j] = d[t[i][j]];
            if (t[i][0] == '0') flag = true;
        }
        if (flag) continue;

        vector<ll> tt(3, 0);

        rep(i, 3) tt[i] = stoll(t[i]);

        // rep(i, 3) cout << tt[i] << "\n";

        if (tt[0] + tt[1] == tt[2]) {
            cout << tt[0] << "\n";
            cout << tt[1] << "\n";
            cout << tt[2] << "\n";
            return 0;
        }

    } while (next_permutation(a.begin(), a.end()));

    cout << "UNSOLVABLE"
         << "\n";
    return 0;
}