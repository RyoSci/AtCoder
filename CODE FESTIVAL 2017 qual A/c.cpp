#define _GLIBCXX_DEBUG
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
    vector<string> a(h);
    rep(i, h) cin >> a[i];

    vector<ll> nums(26);
    rep(i, h) rep(j, w) { nums[a[i][j] - 'a']++; }

    vector<ll> needed(5);
    if (h % 2 == 0 && w % 2 == 0) {
        needed[4] += h * w / 4;
    } else if (h % 2 == 1 && w % 2 == 1) {
        needed[4] += (h - 1) * (w - 1) / 4;
        needed[2] += (h - 1) / 2;
        needed[2] += (w - 1) / 2;
        needed[1] += 1;
    } else {
        if (h % 2 == 0) swap(h, w);
        needed[4] += (h - 1) * w / 4;
        needed[2] += w / 2;
    }

    vector<ll> cnt(5);
    rep(i, 26) {
        ll use = nums[i] / 4;
        cnt[4] += use;
        use = nums[i] % 4 / 2;
        cnt[2] += use;
        use = nums[i] % 2;
        cnt[1] += use;
    }

    if (cnt[4] >= needed[4]) {
        cnt[2] += (cnt[4] - needed[4]) * 2;
    } else {
        cout << "No"
             << "\n";
        return 0;
    }
    if (cnt[2] >= needed[2]) {
        cnt[1] += (cnt[2] - needed[2]) * 2;
    } else {
        cout << "No"
             << "\n";
        return 0;
    }
    if (cnt[1] != needed[1]) {
        cout << "No"
             << "\n";
        return 0;
    }
    cout << "Yes"
         << "\n";
    return 0;
}