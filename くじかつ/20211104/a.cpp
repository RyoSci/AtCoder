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
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)



int main()
{
    int x;
    cin >> x;
    if (x<40)
    {
        /* code */
        cout << 40-x << "\n";
    }
    else if (x<70)
    {
        /* code */
        cout << 70-x << "\n";
    }
    
    else if (x<90)
    {
        /* code */
        cout << 90-x << "\n";
    }
    else
    {
        /* code */
        cout << "expert" << "\n";
    }
    
    
    return 0;
}