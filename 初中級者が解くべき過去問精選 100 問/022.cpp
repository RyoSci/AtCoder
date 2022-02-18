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

double p;

double f(double x) { return x + p * pow(2.0, -2.0 / 3.0 * x); }

int main() {
    cin >> p;
    double x;
    x = 3.0 / 2.0 * log(p * 2.0 / 3.0 * log(2.0)) / log(2.0);
    if (x < 0.0) {
        //小数点以下の長さを指定
        cout << fixed << setprecision(15) << f(0) << endl;
    } else {
        cout << fixed << setprecision(15) << f(x) << endl;
    }
    return 0;
}