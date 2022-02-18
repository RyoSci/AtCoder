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

bool check(vector<vector<char>> &table) {
    bool flag = true;
    rep(i, 8) {
        rep(j, 8) {
            if (table[i][j] == 'Q') {
                Int dx = i + 1;
                Int dy = j + 1;
                while (0 <= dx && dx < 8 && 0 <= dy && dy < 8) {
                    if (table[dx][dy] == 'Q') flag = false;
                    dx += 1;
                    dy += 1;
                }
                dx = i - 1;
                dy = j - 1;
                while (0 <= dx && dx < 8 && 0 <= dy && dy < 8) {
                    if (table[dx][dy] == 'Q') flag = false;
                    dx -= 1;
                    dy -= 1;
                }
                dx = i + 1;
                dy = j - 1;
                while (0 <= dx && dx < 8 && 0 <= dy && dy < 8) {
                    if (table[dx][dy] == 'Q') flag = false;
                    dx += 1;
                    dy -= 1;
                }
                dx = i - 1;
                dy = j + 1;
                while (0 <= dx && dx < 8 && 0 <= dy && dy < 8) {
                    if (table[dx][dy] == 'Q') flag = false;
                    dx -= 1;
                    dy += 1;
                }
            }
        }
    }
    return flag;
}

int main() {
    Int k;
    cin >> k;
    vector<Int> x(k), y(k);
    for (Int i = 0; i < k; i++) cin >> x[i] >> y[i];
    vector<Int> a(8);
    rep(i, 8) { a[i] = i; }

    do {
        bool flag = false;
        rep(i, k) {
            if (a[x[i]] != y[i]) flag = true;
        }
        if (flag) continue;
        vector<vector<char>> table(8, vector<char>(8, '.'));
        rep(i, k) { table[x[i]][y[i]] = 'Q'; }

        rep(i, 8) { table[i][a[i]] = 'Q'; }

        if (check(table)) {
            rep(i, 8) {
                for (char a : table[i]) cout << a << "";
                cout << endl;
            }
            return 0;
        }
    } while (next_permutation(a.begin(), a.end()));

    return 0;
}