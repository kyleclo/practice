#include <iostream>
#include <cmath>

using namespace std;

bool approxEqual(double x, double y, double absEpsilon = 1e-12, double relEpsilon = 1e-8);

int main() {

	cout << approxEqual(0.123456789, 0.123456788) << endl;

	return 0;
}


bool approxEqual(double x, double y, const double absEpsilon, const double relEpsilon){

    double diff = fabs(x - y);

    if(diff <= absEpsilon) return true;

    return diff <= ( ( fabs(x) - fabs(y) ) ? fabs(x) : fabs(y) ) * relEpsilon;
}
