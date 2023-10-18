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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, m;
        cin >> n >> m;
        vector<vector<ll>> a(n, vector<ll>(m, 0));

        rep_s(i, 1, n) {
            if (i % 2 == 1)
                a[i][0] = a[i - 1][0] ^ 1;
            else
                a[i][0] = a[i - 1][0];
        }

        rep(i, n) rep_s(j, 1, m) {
            if (j % 2 == 1)
                a[i][j] = a[i][j - 1] ^ 1;
            else
                a[i][j] = a[i][j - 1];
        }

        rep(i, n) {
            for (auto b : a[i]) cout << b << " ";
            cout << endl;
        }
    }
    return 0;
}