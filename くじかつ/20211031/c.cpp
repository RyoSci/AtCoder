#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>
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

int main()
{
    int n;
    cin >> n;
    vector<double> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    sort(a.begin(), a.end());
    // 浮動小数出力に対応する (小数点以下 2 桁まで出す)
    cout << fixed << setprecision(2);
    if (n % 2 == 0)
    {
        /* code */
        cout << (a[n / 2 - 1] + a[n / 2]) / 2.0 << "\n";
    }
    else
    {
        cout << a[(n - 1) / 2] << "\n";
    }

    return 0;
}