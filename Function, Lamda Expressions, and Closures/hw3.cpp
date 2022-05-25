#include <stdlib.h> // for rand()
#include <iostream> // for cout and endl
#include <iomanip>  // for setw()
#include "TBuffer.hpp"
using namespace std;
class TablePrint {
    int column;
public:
    // initialize the column count in the constructor
    TablePrint() : column(0) {}
    // output newline when the table is done (we go out of scope)
    ~TablePrint() {
        cout << endl;
    }
    // overloaded () operator lets object be used like function
    void operator()(int x) {
        // count the column to output a newline when needed
        if (++column > 10) {
            cout << endl;
            column = 1;
        }
        cout << setw(5) << x;
    }
};
#define BUFSZ 25
int main() {
    TBuffer<int, BUFSZ> ibuf;
    // fill the buffer with (pseudo) random integers
    for (int i = 0; i < BUFSZ; ++i)
        ibuf.add(rand() % 100);
    // print the numbers in a table using a fuctor
    ibuf.map(TablePrint());
    // print the number all in a row using a lambda
    ibuf.map([] (int value) { cout << value << " "; });
    // sort the number low to high using a lamda for the compare
    ibuf.sort([] (int value1, int value2) { return value1 > value2; });
    // compute the sum and average using a closure here
    double sum = 0;
    ibuf.map([&] (int value) { sum += value; });
    cout << "\nThe average is " << sum / BUFSZ << endl;
    // print a table like the one above, only this time using a closure
    int column = 0;
    ibuf.map([&] (int value)
    {
        if (++column > 10) {
            cout << endl;
            column = 1;
        }
        cout << setw(5) << value;
    });
    cout << endl;
    return 0;
}
