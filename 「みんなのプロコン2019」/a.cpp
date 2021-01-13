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

Int n, k;
string ans;
int main()
{
    cin >> n >> k;
    if ((n + 1) / 2 >= k)
    {
        ans = "YES";
    }
    else
    {
        ans = "NO";
    }
    cout << ans << endl;
    return 0;
}