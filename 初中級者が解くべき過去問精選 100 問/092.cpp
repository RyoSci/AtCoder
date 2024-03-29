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
    while (1) {
        ll h;
        cin >> h;
        if (h == 0) break;
        vector<vector<ll>> s(5, vector<ll>(h));
        rep(i, h) {
            rep(j, 5) { cin >> s[j][h - 1 - i]; }
        }

        ll ans = 0;
        while (1) {
            bool is_finish = true;
            vector<P> del;
            rep(i, h) {
                ll cnt = 1;
                rep(j, 5 - 1) {
                    // 隣同士の連結数を計算
                    if (s[j].size() > i && s[j + 1].size() > i &&
                        s[j][i] == s[j + 1][i])
                        cnt++;
                    else {
                        if (cnt >= 3) {
                            rep(k, cnt) del.push_back(make_pair(j - k, i));
                            is_finish = false;
                            ans += cnt * s[j][i];
                        }
                        cnt = 1;
                    }
                }
                if (cnt >= 3) {
                    rep(k, cnt) { del.push_back(make_pair(4 - k, i)); }
                    is_finish = false;
                    ans += cnt * s[4][i];
                }
            }
            if (is_finish)
                break;
            else {
                reverse(del.begin(), del.end());
                rep_e(e, del) {
                    ll j, i;
                    tie(j, i) = e;
                    s[j].erase(s[j].begin() + i);
                }
            }
        }

        cout << ans << "\n";
        // rep(i, 5) {
        //     for (auto a : s[i]) cout << a << " ";
        //     cout << endl;
        // }
    }
    return 0;
}