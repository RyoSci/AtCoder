// #define _GLIBCXX_DEBUG
#include <algorithm>
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll k, n;
        cin >> k >> n;

        ll can;
        rep_s(i, 1, n) {
            if (n - 1 - i * (i + 1) / 2 >= k - i - 1)
                can = i;
            else
                break;
        }

        // cout << can << "\n";
        vector<ll> a;
        a.emplace_back(1);
        ll now = 1;
        rep(i, min(can, k - 1)) {
            a.emplace_back(a.back() + now);
            now++;
        }

        while (a.size() < k) a.emplace_back(a.back() + 1);

        for (auto a : a) cout << a << " ";
        cout << endl;
    }
    return 0;
}