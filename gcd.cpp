#include <cassert>
#include <iostream>
#include <cstdint>
#include <utility>

template <class Int>
Int gcd(Int a, Int b) {
    assert(a > 0 && b > 0);
    while (b > 0) {
        a %= b;
        std::swap(a, b);
    }
    return a;
}

int main()
{
    std::int64_t a, b;
    std::cin >> a >> b;
    std::cout << gcd(a,b) << std::endl;
    return 0;
}
