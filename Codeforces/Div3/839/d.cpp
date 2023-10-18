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
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        vector<ll> b = a;
        ll x = -1;
        sort(b.begin(), b.end());
        if (b == a) x = 0;
        reverse(b.begin(), b.end());
        if (b == a) x = 1e9;

        if (x != -1)
            cout << x << "\n";
        else {
            ll min_i = 0;
            rep(i, n) if (a[i] < a[min_i]) min_i = i;

            ll max_i = 0;
            rep(i, min_i) if (a[i] > a[max_i]) max_i = i;
            x = (a[max_i] + a[min_i] + 1) / 2;

            rep(i, n) {
                a[i] -= x;
                a[i] = abs(a[i]);
            }
            // cout << x << "\n";
            // for (auto a : a) cout << a << " ";
            // cout << endl;

            bool tmp = true;
            rep(i, n - 1) if (a[i] > a[i + 1]) tmp = false;
            if (tmp)
                cout << x << "\n";
            else
                cout << -1 << "\n";
        }
    }
    return 0;
}