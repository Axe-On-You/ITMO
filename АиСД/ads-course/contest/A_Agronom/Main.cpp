#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  if (!(cin >> n)) {
    return 0;
  }
  vector<int> a(n + 1);
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
  }
  int max_len = 0;
  int best_l = 1;
  int best_r = 1;

  int l = 1;

  for (int r = 1; r <= n; r++) {
    if (a[r] == a[r - 1] && a[r] == a[r - 2]) {
      l = r - 1;
    }
    int current_len = r - l + 1;
    if (current_len > max_len) {
      max_len = current_len;
      best_l = l;
      best_r = r;
    }
  }
  cout << best_l << " " << best_r << endl;

  return 0;
}