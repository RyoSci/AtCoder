#include <algorithm>
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
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int main() {
    // 入力を受け取る
    Int n;
    cin >> n;
    vector<P> a(n);
    for (Int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }
    vector<Int> b(n);
    for (Int i = 0; i < n; i++) cin >> b[i];
    sort(a.begin(), a.end());

    // 同じ組み合わせの数を数える
    map<P, Int> d;
    // bは負にしてから入れる
    vector<P> ab;
    rep(i, n) {
        if (d.count({a[i].first, b[a[i].second]})) {
            d[{a[i].first, b[a[i].second]}]++;
        } else {
            d[{a[i].first, b[a[i].second]}]++;
            ab.push_back({a[i].first, -b[a[i].second]});
        }
    }
    sort(ab.begin(), ab.end());

    // 調査済みのbiを入れるsetと答えの数を数える変数
    set<Int> tree;
    Int ans = 0;

    // setでbiの重複が削られるの防ぐために応急処置的に対応
    map<Int, Int> cnt;
    rep(i, n) { cnt[b[i]] = 1000000; }

    rep_e(i, ab) {
        Int ai = i.first;
        Int bi = -i.second;
        cout << d[{ai, bi}] << "\n";

        for (Int j = 0; j < d[{ai, bi}]; j++) {
            Int next = cnt[bi]--;
            tree.insert(bi * 1000000 + next);
        }
        auto iter = tree.lower_bound(bi * 1000000 + next);
        Int dis = distance(iter, tree.end());
        ans += dis;
    }
    cout << ans << "\n";

    return 0;
}