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
        ll a, b;
        cin >> a >> b;
        vector<char> c(a + b);
        if (a > b) {
            ll i = 0;
            while (a > 0 || b > 0) {
                if (a > 0) {
                    c[i] = '0';
                    i++;
                    a--;
                }
                if (b > 0) {
                    c[i] = '1';
                    i++;
                    b--;
                }
            }
        } else {
            ll i = 0;
            while (a > 0 || b > 0) {
                if (b > 0) {
                    c[i] = '1';
                    i++;
                    b--;
                }
                if (a > 0) {
                    c[i] = '0';
                    i++;
                    a--;
                }
            }
        }
        for (auto a : c) cout << a << "";
        cout << endl;
    }
    return 0;
}