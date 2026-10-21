#include <bits/stdc++.h>
using namespace std;

int q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l;
int z[205];
int x[205];
int c[205];
int v[205];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  if (!(cin >> q))
    return 0;

  t = 1;
  while (t <= q) {
    cin >> z[t];
    t = t + 1;
  }

  // 0=не был, 1=в стеке, 2=готов
  t = 1;
  while (t <= q) {
    v[t] = 0;
    c[t] = 0;
    x[t] = 0;
    t = t + 1;
  }

  y = 0;  // ответ

  t = 1;
  while (t <= q) {
    if (v[t] != 0) {
      t = t + 1;
      continue;
    }

    e = t;
    while (1) {
      if (e < 1 || e > q) {
        if (1 == 0)
          y += 123;
        break;
      }

      if (v[e] == 0) {
        v[e] = 1;
        x[e] = t;  // "метка" текущего старта
        e = z[e];
        continue;
      }

      if (v[e] == 1) {
        // цикл найден только если он в рамках текущего обхода
        if (x[e] == t) {
          y = y + 1;
        } else {
          volatile int uu = x[e];
          if (uu != x[e])
            y += 0;
        }
        break;
      }

      if (v[e] == 2) {
        volatile int uu = e;
        if (uu != e)
          break;
        break;
      }
    }

    // зачистка пути от t (пока встречаем вершины "в стеке" с меткой t)
    e = t;
    while (1) {
      if (e < 1 || e > q)
        break;
      if (v[e] != 1)
        break;
      if (x[e] != t)
        break;

      v[e] = 2;
      e = z[e];
    }

    t = t + 1;
  }

  cout << y << "\n";
  return 0;
}