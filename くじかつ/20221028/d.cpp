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
    string s;
    cin >> s;
    string t;
    cin >> t;
    ll n = s.size();
    ll m = t.size();

    vector<string> ans;
    rep(l, n) {
        string tmp = "";
        bool flag = true;
        rep(i, l) {
            if (s[i] == '?')
                tmp += 'a';
            else
                tmp += s[i];
        }
        if (l + m > n) continue;
        rep_s(i, l, l + m) {
            if (s[i] == '?' or s[i] == t[i - l])
                tmp += t[i - l];
            else {
                flag = false;
                break;
            }
        }
        rep_s(i, l + m, n) {
            if (s[i] == '?')
                tmp += 'a';
            else
                tmp += s[i];
        }
        if (flag) ans.emplace_back(tmp);
    }

    if (ans.size() == 0)
        cout << "UNRESTORABLE"
             << "\n";
    else {
        sort(ans.begin(), ans.end());
        cout << ans[0] << "\n";
    }

    return 0;
}