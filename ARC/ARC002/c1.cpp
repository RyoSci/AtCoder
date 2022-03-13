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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n;
    cin >> n;
    string s;
    cin >> s;
    s += "Z";
    vector<string> sc;
    rep_e(c, "ABXY") {
        rep_e(d, "ABXY") {
            string tmp = "";
            tmp += c;
            tmp += d;
            sc.push_back(tmp);
        }
    }

    ll ans = INF;
    ll m = sc.size();
    rep(i, m) {
        string l = sc[i];
        rep(j, m) {
            string r = sc[j];
            bool not_skip = true;
            vector<ll> dp(n + 1, 0);
            // 編集距離なので貪欲に前から置換が最小コストにならない場合があるのでdpで状態を管理して探索
            // dp[i]=i文字絵までを見てコマンドL、Rを使って良い時の最小コマンド数
            rep_s(k, 1, n + 1) {
                // 前から見ていって一致するならその段階でショートカットコマンド使って良い、後に取っておくメリットはない。
                // ショートカット使うならば、次の文字は判定に使ってはだめ
                if (not_skip &&
                    (s.substr(k - 1, 2) == l || s.substr(k - 1, 2) == r)) {
                    dp[k] = dp[k - 1];
                    not_skip = false;
                } else {
                    dp[k] = dp[k - 1] + 1;
                    not_skip = true;
                }
            }
            ans = min(ans, dp[n]);
        }
    }

    cout << ans << "\n";
    return 0;
}