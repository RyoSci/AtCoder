#define _GLIBCXX_DEBUG
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

ll n = 30;

// 次の方向
vector<vector<ll>> to0 = {
    {1, 0, -1, -1}, {3, -1, -1, 0}, {-1, -1, 3, 2}, {-1, 2, 1, -1},
    {1, 0, 3, 2},   {3, 2, 1, 0},   {2, -1, 0, -1}, {-1, 3, -1, 1},
};
vector<vector<ll>> to1 = {
    {3, -1, -1, 0}, {-1, -1, 3, 2}, {-1, 2, 1, -1}, {1, 0, -1, -1},
    {3, 2, 1, 0},   {1, 0, 3, 2},   {-1, 3, -1, 1}, {2, -1, 0, -1},
};
vector<vector<ll>> to2 = {
    {-1, -1, 3, 2}, {-1, 2, 1, -1}, {1, 0, -1, -1}, {3, -1, -1, 0},
    {1, 0, 3, 2},   {3, 2, 1, 0},   {2, -1, 0, -1}, {-1, 3, -1, 1},
};
vector<vector<ll>> to3 = {
    {-1, 2, 1, -1}, {1, 0, -1, -1}, {3, -1, -1, 0}, {-1, -1, 3, 2},
    {3, 2, 1, 0},   {1, 0, 3, 2},   {-1, 3, -1, 1}, {2, -1, 0, -1},
};

// 入力グリッド
vector<vector<ll>> t(n, vector<ll>(n));

// 左上右下
vector<ll> di = {0, -1, 0, 1};
vector<ll> dj = {-1, 0, 1, 0};

vector<ll> ans1(n *n, 0);

ll cal(ll i, ll j, vector<vector<ll>> &seen) {
    // (si, sj) のタイルに sd
    // 方向のタイルから侵入した状態からスタートして環状線の長さを求める
    ll si = i;
    ll sj = j;
    // 初回は右に進む
    ll d = 0;
    ll sd = d;
    ll length = 0;

    while (1) {
        ll d2;
        if (ans1[i * 30 + j] == 0) {
            d2 = to0[t[i][j]][d];

        } else if (ans1[i * 30 + j] == 1) {
            d2 = to1[t[i][j]][d];

        } else if (ans1[i * 30 + j] == 2) {
            d2 = to2[t[i][j]][d];

        } else if (ans1[i * 30 + j] == 3) {
            d2 = to3[t[i][j]][d];
        }
        if (d2 == -1) return 0;
        i += di[d2];
        j += dj[d2];
        if (i < 0 || i >= 30 || j < 0 || j >= 30) return 0;
        seen[i][j] = 1;
        d = (d2 + 2) % 4;
        length += 1;
        if (i == si && j == sj && d == sd) return length;
    }
}

ll solve(void) {
    vector<vector<ll>> seen(n, vector<ll>(n, 0));
    vector<ll> length;

    rep(i, n) {
        rep(j, n) {
            if (seen[i][j] == 1) continue;
            seen[i][j] = 1;
            length.push_back(cal(i, j, seen));
        }
    }
    sort(length.begin(), length.end());
    reverse(length.begin(), length.end());
    if (length.size() < 2)
        return 0;
    else
        return length[0] * length[1];
}

int main() {
    // 入力受け取り
    rep(i, n) {
        string l;
        cin >> l;
        rep(j, n) { t[i][j] = l[j] - '0'; }
    }

    vector<ll> ans(n * n, 0);

    rep(i, n * n) { ans1[i] = 0; }
    rep(i, n * n) { ans[i] = 0; }
    ll res = solve();

    ll m = 9;
    // vector<vector<ll>> t2;

    rep(i, 65 * 1e2) {
        // rep(i, n * n) {
        //      ans1[i] = 0; }

        // 乱数で回転させる
        // 中央付近を探索する
        ll x = rand() % 30;
        ll y = rand() % 30;
        // ll x = rand() % 20 + 5;
        // ll y = rand() % 20 + 5;

        // 良かった場合はそのまま、悪くなった場合は元に戻す
        ll d = rand() % 4;
        ans1[x * 30 + y] = d;
        ll tmp = solve();
        if (res < tmp) {
            ans = ans1;
            res = tmp;
        } else {
            ans1 = ans;
        }

        // 乱数を取得して、そのエリアの16マスの回転を全探索
        // rep(j, powl(4, m)) {
        //     rep(k, m) {
        //         ll d = (j >> k & 3);
        //         ans1[x * 30 + y] = d;
        //     }
        //     ll tmp = solve();
        //     if (res < tmp) {
        //         ans = ans1;
        //         res = tmp;
        //     }
        // }

        // // ２つの小エリアに対してそのエリアの回転を全部試す
        // rep(j, 1<<2){
        //     if(j>>0 & 1){

        //     }
        //     if(j>>1 & 1){

        //     }
        // }
    }

    // cout << res << "\n";
    string s = "";
    rep_e(e, ans) { s += to_string(e); }
    cout << s << "\n";
    return 0;
}