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

    vector<ll> div;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            div.emplace_back(i);
            if (n / i != i) div.emplace_back(n / i);
        }
    }

    sort(div.begin(), div.end());

    set<ll> ans;
    rep_e(d, div) {
        if (d == 1) continue;
        ll m = n;
        while (m % d == 0) {
            m /= d;
        }

        if (m % d == 1) ans.insert(d);
    }

    n--;
    div.clear();
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            div.emplace_back(i);
            if (n / i != i) div.emplace_back(n / i);
        }
    }
    sort(div.begin(), div.end());

    n++;
    rep_e(d, div) {
        if (n % d == 1) ans.insert(d);
    }

    cout << ans.size() << "\n";
    // for (auto a : ans) cout << a << " ";
    // cout << endl;

    return 0;
}