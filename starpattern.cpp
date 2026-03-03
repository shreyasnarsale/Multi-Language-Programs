#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    // 1. Square Pattern
    cout << "\n1. Square Pattern\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 2. Left Half Pyramid
    cout << "\n2. Left Half Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 3. Inverted Left Half Pyramid
    cout << "\n3. Inverted Left Half Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 4. Right Half Pyramid
    cout << "\n4. Right Half Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << "  ";
        }
        for(int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 5. Inverted Right Half Pyramid
    cout << "\n5. Inverted Right Half Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < i; j++) {
            cout << "  ";
        }
        for(int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 6. Full Pyramid
    cout << "\n6. Full Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for(int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // 7. Inverted Full Pyramid
    cout << "\n7. Inverted Full Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < i; j++) {
            cout << " ";
        }
        for(int j = 0; j < 2 * (n - i) - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // 8. Diamond Pattern
    cout << "\n8. Diamond Pattern\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for(int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    for(int i = n - 2; i >= 0; i--) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for(int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // 9. Hollow Square
    cout << "\n9. Hollow Square\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(i == 0 || i == n-1 || j == 0 || j == n-1)
                cout << "* ";
            else
                cout << "  ";
        }
        cout << endl;
    }

    // 10. Hollow Pyramid
    cout << "\n10. Hollow Pyramid\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for(int j = 0; j < 2 * i + 1; j++) {
            if(j == 0 || j == 2 * i || i == n - 1)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }

    return 0;
}

