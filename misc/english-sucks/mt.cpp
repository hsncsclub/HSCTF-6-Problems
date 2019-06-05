#include <fstream>
#include <iostream>
#include <random>

int main() {
    std::mt19937 random{std::random_device()()};
    std::ios::sync_with_stdio(false);

    std::cout << "English sucks!\n"
	         "I just noticed the other day that the letters\n"
                 "B, C, D, G, P, T, V, and Z all rhyme with E\n"
                 "(Z = zee in USA)\n"
                 "My hearing is bad, and sometimes I have trouble\n"
                 "identifying some of the letters.\n"
                 "Can you help me understand what letter is being said?\n"
                 "Here, I'll give you some sample answers:\n";

    for (auto i = 216; i--;) {
        auto v1 = random();
        auto v2 = random();
        auto v3 = random();

        std::cout << "BCDGPTVZ"[v2 >> 0x1F & 0x1 | v3 >> 0x0 & 0x3]
                  << "BCDGPTVZ"[v1 >> 0x09 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x05 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x08 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x15 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x06 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x1D & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x1B & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x04 & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x0D & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x0A & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x1A & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x16 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x17 & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x1C & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x14 & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x01 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x11 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x00 & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x13 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x18 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x0B & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x19 & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x10 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x03 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x12 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x0F & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x02 & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x0C & 0x7]
                  << "BCDGPTVZ"[v2 >> 0x07 & 0x7]
                  << "BCDGPTVZ"[v3 >> 0x0E & 0x7]
                  << "BCDGPTVZ"[v1 >> 0x1E & 0x3 | v2 >> 0x00 & 0x1]
		  << '\n';
    }

    std::cout << "Okay, now tell me what letters are being said." << std::endl;

    decltype(' ') s;
    
    auto v1 = random();
    auto v2 = random();
    auto v3 = random();

    // lol macros are for losers

    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x1E & 0x3 | v2 >> 0x00 & 0x1]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x09 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x05 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x08 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x15 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x06 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x1D & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x1B & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x04 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x0D & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x0A & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x16 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x1A & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x17 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x1C & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x14 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x01 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x00 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x11 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x13 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x18 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x0B & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x19 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x10 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x03 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x12 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x0F & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v1 >> 0x0C & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x07 & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v3 >> 0x0E & 0x7]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }
    
    std::cin >> s;
    
    if (s != "BCDGPTVZ"[v2 >> 0x1F & 0x1 | v3 >> 0x0 & 0x3]) {
        std::cout << "I'm sorry, thats wrong." << std::endl;
        return 0;
    }

    std::cout << "You Win!\n" << std::ifstream("flag.txt").rdbuf() << std::endl;
    
    return 0;
}
