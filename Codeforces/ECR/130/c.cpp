// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
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
    ll q;
    cin >> q;
    rep(i, q) {
        ll n;
        cin >> n;
        vector<char> s(n), t(n);
        string ss, tt;
        cin >> ss >> tt;
        rep(i, n) {
            s[i] = ss[i];
            t[i] = tt[i];
        }
        bool ans = true;
        vector<ll> d(3, 0);
        ll j = 0;
        rep(i, n) {
            j = max(j, i);
            while (j < n && s[j] != t[i]) {
                d[s[j] - 'a']++;
                j++;
            }
            if (j == n) {
                ans = false;
                break;
            }
            if (t[i] == 'a') {
                if (d[1] == 0 && d[2] == 0) {
                    d[0] = max(0, d[0] - 1);
                    continue;
                } else {
                    ans = false;
                    break;
                }
            } else if (t[i] == 'b') {
                if (d[2] == 0) {
                    swap(s[i], s[j]);
                    d[0] = max(0, d[0] - 1);
                    continue;
                } else {
                    ans = false;
                    break;
                }
            } else if (t[i] == 'c') {
                if (d[0] == 0) {
                    swap(s[i], s[j]);
                    d[1] = max(0, d[1] - 1);
                    continue;
                } else {
                    ans = false;
                    break;
                }
            }
        }
        cout << (ans ? "YES" : "NO") << "\n";
    }
    return 0;
}