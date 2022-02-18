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
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)

int main()
{
    string a, b;
    cin >> a >> b;
    int x = stoi(a + b);
    rep(i, 1000)
    {
        if (pow(i, 2) == x)
        {
            cout << "Yes"
                 << "\n";
            return 0;
        }
    }
    cout << "No"
         << "\n";

    return 0;
}