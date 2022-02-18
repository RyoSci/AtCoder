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

set<Int> res;
void f(Int x) {
    for (Int i = 1; i * i <= x; i++) {
        if (x % i == 0) {
            res.insert(i);
            res.insert(x / i);
        }
    }
}

Int cal(Int a, Int b) {
    return pow(a, 4) + pow(a, 3) * b + pow(a, 2) * pow(b, 2) + a * pow(b, 3) +
           pow(b, 4);
}

int main() {
    Int x;
    cin >> x;
    f(x);
    for (Int a = -1000; a < 1000; a++) {
        rep_e(i, res) {
            Int b = a - i;
            if (cal(a, b) == x / i) {
                cout << a << " " << b << "\n";
                return 0;
            }
        }
    }
    return 0;
}