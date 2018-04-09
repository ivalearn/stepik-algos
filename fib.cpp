#include <cassert>
#include <iostream>
#include <vector>

class Fibonacci final {
  public:
    static unsigned long long get(int n) {
        assert(n >= 0);
        if (n <= 1)
            return n;
        unsigned long long a,b,t;
        a=0;
        b=1;
        for (int i = 0; i < n; i++) {
            t=b;
            b=a+b;
            a=t;
        }
        return a;
    }
};


int main()
{
    int n;
    std::cin >> n;
    std::cout << Fibonacci::get(n) << std::endl;
    return 0;
}
