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

bool f_dash(double m) {
    return 1.0 - p * 2.0 / 3.0 * log(2.0) * pow(2.0, -2.0 / 3.0 * m) >= 0.0;
}

int main() {
    cin >> p;
    double l = 0.0;
    double r = powl(10.0, 18);
    if (f_dash(l) >= 0) {
        //小数点以下の長さを指定
        cout << fixed << setprecision(15) << f(l) << endl;
    } else {
        double m;
        while (l + 0.00000000001 < r) {
            m = (l + r) / 2;
            if (f_dash(m))
                r = m;
            else
                l = m;
        }
        //小数点以下の長さを指定
        cout << fixed << setprecision(15) << f(l) << endl;
    }
    return 0;
}