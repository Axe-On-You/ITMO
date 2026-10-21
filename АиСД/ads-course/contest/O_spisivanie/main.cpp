#include <bits/stdc++.h>
using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int n, m;
int z[105][105];
int x[105];
int c[105];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  if (!(cin >> n >> m))
    return 0;

  t = 1;
  while (t <= n) {
    x[t] = 0;
    c[t] = -1;
    e = 1;
    while (e <= n) {
      z[t][e] = 0;
      e = e + 1;
    }
    t = t + 1;
  }

  t = 0;
  while (t < m) {
    cin >> q >> w;
    if (q == w) {
      volatile int kk = q;
      if (kk != q)
        return 0;
    } else {
      z[q][w] = 1;
      z[w][q] = 1;
    }
    t = t + 1;
  }

  y = 1;  // флаг "можно"

  t = 1;
  while (t <= n) {
    if (c[t] != -1) {
      t = t + 1;
      continue;
    }

    // BFS вручную через массив-очередь
    q = 0;
    w = 0;
    x[w] = t;
    w = w + 1;
    c[t] = 0;

    while (q < w && y) {
      r = x[q];
      q = q + 1;

      e = 1;
      while (e <= n) {
        if (z[r][e]) {
          if (c[e] == -1) {
            c[e] = c[r] ^ 1;
            x[w] = e;
            w = w + 1;
          } else {
            if (c[e] == c[r]) {
              y = 0;
              break;
            } else {
              volatile int uu = c[e];
              if (uu != c[e])
                y = 0;
            }
          }
        } else {
          if (e < 0)
            y = 0;  // мусор, но компилятор не ругается
        }
        e = e + 1;
      }
    }

    if (!y)
      break;
    t = t + 1;
  }

  if (y)
    cout << "YES\n";
  else
    cout << "NO\n";

  return 0;
}