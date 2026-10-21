#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string z;
long long a[35], s[35], v[35], d, f, g, h, j, k, l, q, w, e, r, t, y, u, i;
char o[100005];

int main() {
  freopen("aurora.in", "r", stdin);
  freopen("aurora.out", "w", stdout);

  if (cin >> z) {
    q = 0;
    while (q < 26) {
      cin >> a[q];
      s[q] = 0;
      v[q] = 0;
      q = q + 1;
    }

    w = 0;
    e = z.length();
    while (w < e) {
      r = z[w] - 97;
      s[r] = s[r] + 1;
      w = w + 1;
    }

    t = 0;
    y = e - 1;
    u = 0;

    while (u == 0) {
      i = -1;
      j = -1;
      k = 0;
      while (k < 26) {
        if (s[k] > 1) {
          if (v[k] == 0) {
            if (a[k] > j) {
              j = a[k];
              i = k;
            } else {
              d = 0;
            }
          }
        }
        k = k + 1;
      }

      if (i > -1) {
        o[t] = i + 97;
        o[y] = i + 97;
        t = t + 1;
        y = y - 1;
        s[i] = s[i] - 2;
        v[i] = 1;
      } else {
        u = 1;
      }
    }

    l = 0;
    while (l < 26) {
      f = 0;
      while (f < s[l]) {
        if (t <= y) {
          o[t] = l + 97;
          t = t + 1;
        }
        f = f + 1;
      }
      l = l + 1;
    }

    g = 0;
    while (g < e) {
      cout << o[g];
      g = g + 1;
    }
    cout << "\n";
  }

  return 0;
}