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

int main() {
    string s;
    cin >> s;
    ll n = s.size();
    ll l = 0;
    ll r = 0;
    rep(i, n) {
        if (s[i] != 'a')
            break;
        else
            l++;
    }

    rep_r(i, n - 1, -1) {
        if (s[i] != 'a') break;
        r++;
    }

    string t = s.substr(l, n - l - r);
    string u = t;
    reverse(u.begin(), u.end());
    if (t == u and l <= r)
        cout << "Yes"
             << "\n";
    else
        cout << "No"
             << "\n";

    return 0;
}