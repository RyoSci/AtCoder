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
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

// union by size + path having
class UnionFind {
   public:
    vector<Int> par;  // 各元の親を表す配列
    vector<Int> siz;  // 素集合のサイズを表す配列(1 で初期化)

    // Constructor
    UnionFind(Int sz_) : par(sz_), siz(sz_, 1LL) {
        for (Int i = 0; i < sz_; ++i) par[i] = i;  // 初期では親は自分自身
    }
    void init(Int sz_) {
        par.resize(sz_);
        siz.assign(sz_, 1LL);  // resize だとなぜか初期化されなかった
        for (Int i = 0; i < sz_; ++i) par[i] = i;  // 初期では親は自分自身
    }

    // Member Function
    // Find
    Int root(Int x) {  // 根の検索
        while (par[x] != x) {
            x = par[x] = par[par[x]];  // x の親の親を x の親とする
        }
        return x;
    }

    // Union(Unite, Merge)
    bool merge(Int x, Int y) {
        x = root(x);
        y = root(y);
        if (x == y) return false;
        // merge technique（データ構造をマージするテク．小を大にくっつける）
        if (siz[x] < siz[y]) swap(x, y);
        siz[x] += siz[y];
        par[y] = x;
        return true;
    }

    bool issame(Int x, Int y) {  // 連結判定
        return root(x) == root(y);
    }

    Int size(Int x) {  // 素集合のサイズ
        return siz[root(x)];
    }
};

int main() {
    // input(sunippets: inpv, inpn, inps)
    Int n, m;
    cin >> n >> m;

    UnionFind uf(n);

    // calculation
    for (Int i = 0; i < m; i++) {
        Int x, y, z;
        cin >> x >> y >> z;
        uf.merge(x, y);
    }
    Int ans = 0;
    for (Int i = 0; i < n; i++) {
        if (uf.root(uf.par[i]) == i) ans++;
    }
    cout << ans << "\n";
    return 0;
}