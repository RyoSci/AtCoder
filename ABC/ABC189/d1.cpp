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
    vector<string> s(n);
    rep(i, n) cin >> s[i];
    // 1こまで数がどんどん減っていくが、1この場合はtrueしかだめなので1通り
    ll ans = 1;
    // nこの塊が1でないとダメ
    rep_r(i, n - 1, -1) {
        // andの時は最後尾は1が必須でそれより手前のi+1この塊も1であるので、同条件で再スタート
        if (s[i] == "AND") continue;
        // orの時に最後尾が1ならそれより手前はなんでも良い、0ならそれより手前のi+1この塊は1であるので同条件で再スタート
        else
            ans += powl(2, i + 1);
    }
    cout << ans << "\n";
    return 0;
}