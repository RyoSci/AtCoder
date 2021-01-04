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

Int a, b, c;
string ans;
int main()
{
    cin >> a >> b >> c;
    if (a <= c & c <= b || b <= c & c <= a)
    {
        ans = "Yes";
    }
    else
    {
        ans = "No";
    }
    cout << ans << endl;
    return 0;
}