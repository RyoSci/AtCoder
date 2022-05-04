// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
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
    ll h, w;
    cin >> h >> w;
    ll ans = INF;
    rep_s(i, 1, h) {
        // 並行に切る
        vector<ll> a;
        a.emplace_back(w * i);
        a.emplace_back(w * ((h - i) / 2));
        a.emplace_back(w * (h - i - (h - i) / 2));
        ll max_a = *max_element(a.begin(), a.end());
        ll min_a = *min_element(a.begin(), a.end());
        ans = min(ans, max_a - min_a);

        // 垂直に切る
        a.clear();
        a.emplace_back(w * i);
        a.emplace_back((h - i) * (w / 2));
        a.emplace_back((h - i) * (w - w / 2));
        max_a = *max_element(a.begin(), a.end());
        min_a = *min_element(a.begin(), a.end());
        ans = min(ans, max_a - min_a);
    }

    rep_s(j, 1, w) {
        // 並行に切る
        vector<ll> a;
        a.emplace_back(h * j);
        a.emplace_back(h * ((w - j) / 2));
        a.emplace_back(h * (w - j - (w - j) / 2));
        ll max_a = *max_element(a.begin(), a.end());
        ll min_a = *min_element(a.begin(), a.end());
        ans = min(ans, max_a - min_a);

        // 垂直に切る
        a.clear();
        a.emplace_back(h * j);
        a.emplace_back((w - j) * (h / 2));
        a.emplace_back((w - j) * (h - h / 2));
        max_a = *max_element(a.begin(), a.end());
        min_a = *min_element(a.begin(), a.end());
        ans = min(ans, max_a - min_a);
    }

    cout << ans << "\n";
    return 0;
}