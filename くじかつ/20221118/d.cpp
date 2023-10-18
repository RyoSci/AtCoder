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
#define INF (1L << 60)
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

int n;

set<string> ans;

void f(ll i, string num) {
    ll sev = 0, fiv = 0, thr = 0;
    rep_e(c, num) {
        if (c == '7') sev = 1;
        if (c == '5') fiv = 1;
        if (c == '3') thr = 1;
    }
    if (num.size() != 0) {
        int tmp = stoi(num);
        if (n >= tmp and sev * fiv * thr == 1) ans.insert(num);
    }
    if (i == 9) return;
    string tmp_s = "357";
    rep_e(c, tmp_s) {
        string nxt = num;
        nxt += c;
        f(i + 1, nxt);
    }
}

int main() {
    cin >> n;
    string s = "";
    f(0, s);

    cout << ans.size() << "\n";
    return 0;
}