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
    ll h, w;
    cin >> h >> w;
    ll ch, cw;
    cin >> ch >> cw;
    ll dh, dw;
    cin >> dh >> dw;
    vector<string> s(h);
    rep(i, h) cin >> s[i];

    ch--;
    cw--;
    dh--;
    dw--;

    deque<T> dq;
    dq.emplace_back(T(ch, cw, 0));
    vector<vector<ll>> cnt(h, vector<ll>(w, INF));
    cnt[ch][cw] = 0;

    vector<ll> di = {-1, 0, 1, 0};
    vector<ll> dj = {0, 1, 0, -1};

    while (dq.size() > 0) {
        auto [i, j, tmp] = dq.front();
        dq.pop_front();
        rep(k, 4) {
            ll ni = i + di[k];
            ll nj = j + dj[k];
            if (0 <= ni and ni < h and 0 <= nj and nj < w and
                s[ni][nj] == '.') {
                if (cnt[ni][nj] > cnt[i][j]) {
                    cnt[ni][nj] = cnt[i][j];
                    dq.emplace_front(T(ni, nj, tmp));
                }
            }
        }
        rep_s(k, -2, 3) {
            rep_s(l, -2, 3) {
                ll ni = i + k;
                ll nj = j + l;
                if (0 <= ni and ni < h and 0 <= nj and nj < w and
                    s[ni][nj] == '.' and cnt[ni][nj] > cnt[i][j] + 1) {
                    cnt[ni][nj] = cnt[i][j] + 1;
                    dq.emplace_back(T(ni, nj, cnt[ni][nj]));
                }
            }
        }
    }

    if (cnt[dh][dw] == INF)
        cout << -1 << "\n";
    else
        cout << cnt[dh][dw] << "\n";

    return 0;
}