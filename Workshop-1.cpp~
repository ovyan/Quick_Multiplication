#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <deque>
#include <fstream>

class Multiplicator {
private:
    std::deque<int> bigNum;
    std::vector<std::pair<double, double>> times;
public:
    Multiplicator() {
        bigNum = {0};
    }
    Multiplicator(const std::deque<int>& a) {
        bigNum = a;
    }
    Multiplicator(const std::string s) {
        bigNum.clear();
        for (int i = 0; i < s.size(); i++) {
            bigNum.push_back(s[i] - '0');
        }
    }
    void generator(const int k) {
        bigNum.clear();
        int t = (rand() % 9) + 1;
        bigNum.push_back(t);
        for (int i = 1; i < k; i++) {
            t = rand() % 10;
            bigNum.push_back(t);
        }
    }
    std::deque<int> getNum() const {
        return bigNum;
    }
    int getDigit(int i) const {
        return bigNum[i];
    }
    int size() const {
        return bigNum.size();
    }
    void appendZero() {
        bigNum.push_back(0);
    }
    std::pair<std::deque<int>, std::deque<int>> getParts(int m) const{
        std::deque<int> low;
        std::deque<int> high(size() - m);
        for (int i = 0; i < high.size(); i++) {
            high[i] = getDigit(i);
        }
        bool metNonZero = false;
        for (int i = 0; i < m; i++) {
            if (getDigit(i + high.size()) > 0) {
                metNonZero = true;
            }
            if (metNonZero) {
                low.push_back(getDigit(i + high.size()));
            }
        }

        return std::make_pair(low, high);
    }
    Multiplicator operator+=(const Multiplicator &other) {
        int i = bigNum.size() - 1, sub = 0, j;
        for (j = other.size() - 1; i >= 0 && j >= 0; j--) {
            bigNum[i] += other.bigNum[j] + sub;
            sub = bigNum[i] / 10;
            bigNum[i] %= 10;
            i--;
        }
        if (i < 0 && j < 0) {
            if (sub == 1) {
                bigNum.push_front(1);
            }
        } else if (i < 0) {
            for (; j >= 0; j--) {
                bigNum.push_front(sub + other.bigNum[j]);
                sub = bigNum[0] / 10;
                bigNum[0] %= 10;
            }
            if (sub == 1) {
                bigNum.push_front(1);
            }
        } else {
            for (; i >= 0; i--) {
                bigNum[i] += sub;
                sub = bigNum[i] / 10;
                bigNum[i] %= 10;
                if (sub == 0) {
                    break;
                }
            }
            if (sub == 1) {
                bigNum.push_front(1);
            }
        }

        return *this;
    }
    Multiplicator operator+(const Multiplicator& b) const{
        Multiplicator cur(bigNum);
        cur += b;

        return cur;
    }
    Multiplicator operator-=(const Multiplicator& other) {
        int i = size() - 1, sub = 0;
        for (int j = other.size() - 1; j >= 0; j--) {
            if (bigNum[i] - other.bigNum[j] - sub < 0) {
                bigNum[i] += 10 - (other.bigNum[j] + sub);
                sub = 1;
            } else {
                bigNum[i] -= other.bigNum[j] + sub;
                sub = 0;
            }
            --i;
        }
        for (; i >= 0 && sub == 1; i--) {
            if (bigNum[i] - sub < 0) {
                bigNum[i] = 9;
                sub = 1;
            } else {
                bigNum[i] -= 1;
                sub = 0;
            }
        }
        if (bigNum[0] == 0) {
            bigNum.pop_front();
        }
        if (bigNum.size() == 0) {
            bigNum.push_back(0);
        }

        return *this;
    }
    Multiplicator operator-(const Multiplicator& b) {
        Multiplicator cur(bigNum);
        cur -= b;
        
        return cur;
    }
    static void shiftLeft(Multiplicator& a, int k) {
        for (int i = 0; i < k; i++) {
            a.appendZero();
        }
    }
    static Multiplicator multiplyByDigit(const Multiplicator& a, int b) {
        int n = a.size();
        int carry = 0;
        std::deque<int> ans;
        for (int i = n - 1; i >= 0; i--) {
            int prd = a.getDigit(i) * b + carry;
            ans.push_front(prd % 10);
            carry = prd / 10;
        }
        if (carry) {
            ans.push_front(carry);
        }
        
        return Multiplicator(ans);
    }
    static Multiplicator schoolMultiplication(const Multiplicator& m1, const Multiplicator& m2) {
        Multiplicator ans("0");
        for (int i = m2.size() - 1; i >= 0; i--) {
            Multiplicator curr = multiplyByDigit(m1, m2.getDigit(i));
            Multiplicator::shiftLeft(curr, m2.size() - i - 1);
            ans += curr;
        }
        
        return Multiplicator(ans);
    }
    static Multiplicator divideAndConquer(const Multiplicator& m1, const Multiplicator& m2) {
        if (m1.size() <= 60 || m2.size() <= 60) {
            return Multiplicator::schoolMultiplication(m1, m2);
        }
        int m = std::min(m1.size(), m2.size());
        m = floor(m / 2);
        std::pair<std::deque<int>, std::deque<int>> a = m1.getParts(m);
        std::pair<std::deque<int>, std::deque<int>> b = m2.getParts(m);
        Multiplicator l1(a.first);
        Multiplicator h1(a.second);
        Multiplicator l1h1 = l1 + h1;
        
        Multiplicator l2(b.first);
        Multiplicator h2(b.second);
        Multiplicator l2h2 = l2 + h2;
        
        Multiplicator z0 = divideAndConquer(l1, l2);
        Multiplicator z1 = divideAndConquer(l1h1, l2h2);
        Multiplicator z2 = divideAndConquer(h1, h2);
        
        Multiplicator ans = z1 - z2 - z0;
        Multiplicator::shiftLeft(ans, m);
        Multiplicator::shiftLeft(z2, 2 * m);
        
        return ans + z2 + z0;
    }
    void calculate() {
        Multiplicator m1("0");
        Multiplicator m2("0");
        for (int i = 1; i <= 400; i++) {
            if (i % 10 == 0) {
                std::cout << "Test number: " << i << '\n';
            }
            m1.generator(i);
            m2.generator(i);
            double ans1 = 0, ans2 = 0;
            for (int j = 0; j < 3; j++) {
                clock_t start1 = clock();
                schoolMultiplication(m1, m2);
                clock_t end1 = clock();
                ans1 += (double)(end1 - start1) / CLOCKS_PER_SEC;
                clock_t start2 = clock();
                divideAndConquer(m1, m2);
                clock_t end2 = clock();
                ans2 += (double)(end2 - start2) / CLOCKS_PER_SEC;
            }
            ans1 /= 0.3;
            ans2 /= 0.3;
            times.push_back(std::make_pair(ans1, ans2));
        }
    }
    void printer() {
        std::ofstream fout("out.csv");
        for (int i = 0; i < times.size(); i++) {
            fout << i + 1 << ',' << times[i].first << ',' << times[i].second << '\n';
        }
        fout.close();
        std::cout << "CSV file has been generated\n";
    }
    void doEverything() {
        this->calculate();
        this->printer();
    }
};

std::ostream& operator << (std::ostream& out, const Multiplicator& m) {
    for (int i = 0; i < m.size(); i++) {
        out << m.getDigit(i);
    }
    
    return out;
}

int main() {
    srand(time(NULL));
    Multiplicator m1("0");
    m1.doEverything();
    system("python3 plot.py"); //running python script to show plot, the same in the notebook.
    return 0;
}
