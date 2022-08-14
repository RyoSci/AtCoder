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
    vector<string> s(h);
    for (ll i = 0; i < h; i++) cin >> s[i];
    vector<vector<mint>> tot(h, vector<mint>(w, 0));

    vector<vector<mint>> tate(h, vector<mint>(w, 0));
    vector<vector<mint>> yoko(h, vector<mint>(w, 0));
    vector<vector<mint>> nana(h, vector<mint>(w, 0));

    tot[0][0] = 1;
    tate[0][0] = 1;
    yoko[0][0] = 1;
    nana[0][0] = 1;

    rep(i, h) rep(j, w) {
        if (i == 0 and j == 0) continue;
        if (s[i][j] == '#') {
            tot[i][j] = 0;
            tate[i][j] = 0;
            yoko[i][j] = 0;
            nana[i][j] = 0;
            continue;
        }
        if (i - 1 >= 0) {
            tot[i][j] += tate[i - 1][j];
            tate[i][j] += tate[i - 1][j];
        }
        if (j - 1 >= 0) {
            tot[i][j] += yoko[i][j - 1];
            yoko[i][j] += yoko[i][j - 1];
        }
        if (i - 1 >= 0 and j - 1 >= 0) {
            tot[i][j] += nana[i - 1][j - 1];
            nana[i][j] += nana[i - 1][j - 1];
        }

        tate[i][j] += tot[i][j];
        yoko[i][j] += tot[i][j];
        nana[i][j] += tot[i][j];
    }

    cout << tot[h - 1][w - 1].val() << "\n";
    // rep(i, h) {
    //     for (auto a : tot[i]) cout << a.val() << " ";
    //     cout << endl;
    // }
    return 0;
}