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
using lli = long long;
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        string s;
        cin >> s;
        ll i = n - 1;
        string code = "abcdefgfijklmnopqrstuvwxyz";
        string ans = "";
        while (i > -1) {
            if (s[i] == '0') {
                string t = s[i - 2];
                t += s[i - 1];
                ll tmp = stoll(t);
                ans += code[tmp - 1];
                i -= 3;
            } else {
                string t = s[i - 1];
                ll tmp = stoll(t);
                ans += code[tmp - 1];
                i -= 2;
            }
        }
        reverse(ans.begin(), ans.end());
        cout << ans << "\n";
    }
    return 0;
}