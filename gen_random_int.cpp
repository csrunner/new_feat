#include <random>
#include <iostream>
#include <ctime>

//该函数接受三个参数分别指定随机数范围和种子，返回double
int random_unint(unsigned int min, unsigned int max, unsigned int seed = 0)
{
    static std::default_random_engine e(seed);
    static std::uniform_real_distribution<double> u(min, max);
    return u(e);
}

int main(void)
{
    for (int i = 0; i < 15; ++i) {
        std::cout << random_unint(0, 15, time(NULL)) << " ";
    }
    std::cout << std::endl;
    return 0;
}
