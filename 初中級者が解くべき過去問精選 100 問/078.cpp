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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

int main() {
    // ll m, n;
    // cin >> m >> n;
    // ll k;
    // cin >> k;
    // vector<vector<char>> grid(m, vector<char>(n));
    // rep(i, m) {
    //     rep(j, n) { cin >> grid[i][j]; }
    // }
    // vector<vector<ll>> J(m, vector<ll>(n + 1, 0));
    // vector<vector<ll>> O(m, vector<ll>(n + 1, 0));
    // vector<vector<ll>> I(m, vector<ll>(n + 1, 0));
    // rep(i, m) {
    //     rep(j, n) {
    //         if (grid[i][j] == 'J')
    //             J[i][j + 1]++;
    //         else if (grid[i][j] == 'O')
    //             O[i][j + 1]++;
    //         else
    //             I[i][j + 1]++;
    //         J[i][j + 1] += J[i][j];
    //         O[i][j + 1] += O[i][j];
    //         I[i][j + 1] += I[i][j];
    //     }
    // }

    // ll jj, oo, ii;
    // ll a, b, c, d;
    // rep(i, k) {
    //     cin >> a >> b >> c >> d;
    //     a--;
    //     // b--;
    //     c--;
    //     // d--;
    //     jj = 0;
    //     oo = 0;
    //     ii = 0;
    //     rep_s(j, a, c + 1) {
    //         jj += J[j][d] - J[j][b - 1];
    //         oo += O[j][d] - O[j][b - 1];
    //         ii += I[j][d] - I[j][b - 1];
    //     }
    //     cout << jj << ' ' << oo << ' ' << ii << "\n";
    // }
    // TLEコード

    ll m, n;
    cin >> m >> n;
    ll k;
    cin >> k;
    vector<vector<char>> grid(m, vector<char>(n));
    rep(i, m) {
        rep(j, n) { cin >> grid[i][j]; }
    }
    vector<vector<ll>> J(m + 1, vector<ll>(n + 1, 0));
    vector<vector<ll>> O(m + 1, vector<ll>(n + 1, 0));
    vector<vector<ll>> I(m + 1, vector<ll>(n + 1, 0));
    rep(i, m) {
        rep(j, n) {
            if (grid[i][j] == 'J')
                J[i + 1][j + 1]++;
            else if (grid[i][j] == 'O')
                O[i + 1][j + 1]++;
            else
                I[i + 1][j + 1]++;
        }
    }
    rep(i, m) {
        rep(j, n) {
            // 横
            J[i + 1][j + 1] += J[i + 1][j];
            O[i + 1][j + 1] += O[i + 1][j];
            I[i + 1][j + 1] += I[i + 1][j];
        }
    }
    rep(i, m) {
        rep(j, n) {
            // 縦
            J[i + 1][j + 1] += J[i][j + 1];
            O[i + 1][j + 1] += O[i][j + 1];
            I[i + 1][j + 1] += I[i][j + 1];
        }
    }

    ll jj, oo, ii;
    ll a, b, c, d;
    rep(i, k) {
        cin >> a >> b >> c >> d;
        // a--;
        // b--;
        // c--;
        // d--;
        jj = J[c][d] - J[a - 1][d] - J[c][b - 1] + J[a - 1][b - 1];
        oo = O[c][d] - O[a - 1][d] - O[c][b - 1] + O[a - 1][b - 1];
        ii = I[c][d] - I[a - 1][d] - I[c][b - 1] + I[a - 1][b - 1];
        cout << jj << ' ' << oo << ' ' << ii << "\n";
    }

    return 0;
}