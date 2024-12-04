#include <iostream>

using namespace std;

class HumanBeing{
    public:
        void display(){
            std::cout << "I am a Human Being";
        }

};

int main()
{
    HumanBeing anil;
    anil.display();

    return 0;
}