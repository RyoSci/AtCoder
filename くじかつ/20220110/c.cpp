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
#include <atcoder/modint>
using namespace atcoder;
using lli = long long;
using mint = modint1000000007;

Int gcd(Int a, Int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

bool is_prime(Int x) {
    if (x == 1) {
        /* code */
        return false;
    }

    for (Int i = 2; i * i <= x; i++) {
        if (x % i == 0) {
            /* code */
            return false;
        }
    }
    return true;
}
vector<vector<Int>> g(10000 + 10);

void dfs(Int pair, Int root, bool &ans, vector<bool> &seen,
         vector<bool> &finished) {
    seen[pair] = true;

    for (auto chi : g[pair]) {
        if (chi == root) {
            /* code */
            ans = false;
            continue;
        }
        // 完全終了した頂点はスルー
        if (finished[chi]) continue;
        // サイクルを検出
        if (seen[chi] && !finished[chi]) {
            ans = false;
            return;
        }
        dfs(chi, pair, ans, seen, finished);
    }
    finished[pair] = true;
}

vector<Int> quick_sort(vector<Int> a) {
    if (a.size() == 0) {
        /* code */
        return a;
    }

    vector<Int> l;
    vector<Int> r;
    Int n = a.size();
    Int x = n / 2;
    rep(i, n) {
        if (i == x) {
            continue;
        } else if (a[i] < a[x]) {
            /* code */
            l.push_back(a[i]);
        } else if (a[i] > a[x]) {
            r.push_back(a[i]);
        } else {
            if (rand() % 2) {
                /* code */
                l.push_back(a[i]);
            } else {
                /* code */
                r.push_back(a[i]);
            }
        }
    }

    l = quick_sort(l);
    r = quick_sort(r);

    vector<Int> res;
    rep_e(x, l) { res.push_back(x); }
    res.push_back(a[x]);
    rep_e(x, r) { res.push_back(x); }

    return res;
}

Int div_cal(Int x) {
    set<Int> res;
    for (Int i = 1; i * i <= x; i++) {
        if (x % i == 0) {
            /* code */
            res.insert(i);
            res.insert(x / i);
        }
    }
    return res.size();
}

void heaphy(vector<Int> &a) {
    Int n = a.size();
    // Int x = n / 2 - 1;
    rep_r(x, n / 2 - 1, -1)

    {
        Int k = x;
        while (true) {
            if (2 * k + 1 >= n) {
                break;
            }

            Int max_index = k;
            if (a[k] >= a[2 * k + 1]) {
                max_index = k;
            } else {
                max_index = 2 * k + 1;
            }

            if (2 * k + 2 < n) {
                if (a[max_index] >= a[2 * k + 2]) {
                    max_index = max_index;
                } else {
                    max_index = 2 * k + 2;
                }
            }
            if (max_index == k) {
                break;
            }

            Int tmp = a[k];
            a[k] = a[max_index];
            a[max_index] = tmp;
            k = max_index;
        }
    }

    return;
}

void heepppop(vector<Int> &a, Int n, Int i) {
    // Int n = a.size();
    // Int x = n / 2 - 1;
    Int k = i;
    while (true) {
        if (2 * k + 1 >= n) {
            break;
        }

        Int max_index = k;
        if (a[k] >= a[2 * k + 1]) {
            max_index = k;
        } else {
            max_index = 2 * k + 1;
        }

        if (2 * k + 2 < n) {
            if (a[max_index] >= a[2 * k + 2]) {
                max_index = max_index;
            } else {
                max_index = 2 * k + 2;
            }
        }
        if (max_index == k) {
            break;
        }

        Int tmp = a[k];
        a[k] = a[max_index];
        a[max_index] = tmp;
        k = max_index;
    }

    return;
}

Int f(vector<Int> &a, Int x, Int n, vector<vector<Int>> &memo) {
    if (memo[n][x] != -1) return memo[n][x];
    Int res = 0;
    if (n == 0) {
        if (x == 0) res = 1;
    } else {
        if (f(a, x, n - 1, memo) == 1) res = 1;
        if (x - a[n - 1] >= 0 && f(a, x - a[n - 1], n - 1, memo) == 1) res = 1;
    }
    return memo[n][x] = res;
}

map<Int, Int> div_element(Int n, map<Int, Int> &ans) {
    for (Int i = 2; i * i <= n; i++) {
        while (true) {
            if (n % i == 0) {
                n /= i;
                ans[i]++;
            } else
                break;
        }
    }
    if (n != 1) ans[n]++;
    return ans;
}

Int find(vector<Int> &p, Int x) {
    if (p[x] < 0) return x;
    return p[x] = find(p, p[x]);
}

void unite(vector<Int> &p, Int x, Int y) {
    Int px = find(p, x);
    Int py = find(p, y);
    if (px == py) return;
    p[px] += p[py];
    p[py] = px;
    return;
}
// Union-Find
struct UnionFind {
    vector<Int> par, rank, siz;

    // 構造体の初期化
    UnionFind(Int n) : par(n, -1), rank(n, 0), siz(n, 1) {}

    // 根を求める
    Int root(Int x) {
        if (par[x] == -1)
            return x;  // x が根の場合は x を返す
        else
            return par[x] = root(par[x]);  // 経路圧縮
    }

    // x と y が同じグループに属するか (= 根が一致するか)
    bool issame(Int x, Int y) { return root(x) == root(y); }

    // x を含むグループと y を含むグループを併合する
    bool unite(Int x, Int y, vector<Int> &w) {
        Int rx = root(x), ry = root(y);  // x 側と y 側の根を取得する
        if (rx == ry) return false;  // すでに同じグループのときは何もしない
        // union by rank
        if (rank[rx] < rank[ry])
            swap(rx, ry);  // ry 側の rank が小さくなるようにする
        par[ry] = rx;      // ry を rx の子とする
        if (rank[rx] == rank[ry]) rank[rx]++;  // rx 側の rank を調整する
        siz[rx] += siz[ry];                    // rx 側の siz を調整する
        w[rx] += w[ry];
        return true;
    }

    // x を含む根付き木のサイズを求める
    Int size(Int x) { return siz[root(x)]; }
};

Int binary_search(vector<Int> &a, Int target) {
    Int l = 0, r = a.size();
    Int m;
    while (l != r) {
        m = (l + r) / 2;
        if (a[m] >= target)
            r = m;
        else
            l = m + 1;
    }
    return l;
}

Int f(Int n, Int m) {
    Int res = 0;
    rep_s(i, 1, n + 1) { res += min(m / i, n); }
    return res;
}

Int binary_search_disition(Int n, Int x) {
    Int l = 0, r = 1e18;
    while (l + 1 < r) {
        Int m = (l + r) / 2;
        if (f(n, m) >= x)
            r = m;
        else
            l = m;
    }
    return r;
}

int main() {
    Int n, m;
    cin >> n >> m;
    vector<vector<Int>> g(n);
    vector<Int> par(n, -1);
    rep(i, m) {
        Int ai, bi;
        cin >> ai >> bi;
        ai--;
        bi--;
        unite(par, ai, bi);
    }
    set<Int> res;
    rep(i, n) { res.insert(find(par, i)); }
    cout << res.size() - 1 << "\n";
    return 0;
}