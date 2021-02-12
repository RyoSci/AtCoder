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

string s, t;
int res;
int main()
{
    cin >> s;
    t = "CODEFESTIVAL2016";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != t[i])
        {
            res += 1;
        }
    }
    cout << res << endl;
    return 0;
}