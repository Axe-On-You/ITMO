#include <deque>
#include <iostream>

using namespace std;

int a, b, c, d, e, f, g, h, j, k;
char z;
deque<int> q1, q2;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  if (!(cin >> a))
    return 0;

  b = 0;
  while (b < a) {
    cin >> z;
    if (z == 43) {
      cin >> c;
      q2.push_back(c);
    } else if (z == 42) {
      cin >> c;
      q2.push_front(c);
    } else if (z == 45) {
      cout << q1.front() << "\n";
      q1.pop_front();
    }

    while (q1.size() < q2.size()) {
      q1.push_back(q2.front());
      q2.pop_front();
    }
    while (q1.size() > q2.size() + 1) {
      q2.push_front(q1.back());
      q1.pop_back();
    }

    b = b + 1;
  }

  return 0;
}