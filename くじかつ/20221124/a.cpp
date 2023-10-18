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
    ll n;
    cin >> n;
    vector<string> s(n);
    for (ll i = 0; i < n; i++) cin >> s[i];

    set<string> t;
    bool ok = true;
    rep(i, n) {
        t.insert(s[i]);
        bool tmp = false;
        rep_e(c, "HDCS") if (c == s[i][0]) tmp = true;
        if (!tmp) ok = false;

        tmp = false;
        rep_e(c, "A23456789TJQK") if (c == s[i][1]) tmp = true;
        if (!tmp) ok = false;
    }
    if (ok and t.size() == n)
        cout << "Yes"
             << "\n";
    else
        cout << "No"
             << "\n";
    return 0;
}