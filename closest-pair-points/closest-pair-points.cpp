#include <iostream>
#include <cstdlib>
#include <cmath>


struct Point{
    
    int x;
    int y;
};


struct Pair{
    
    Point p1;
    Point p2;
    double dist;
};


void printPoints(Point* p, const int n);
int compareX (const void* a, const void* b);
int compareY (const void* a, const void* b);
double computeDist(Point p1, Point p2);
void findStripClosestPair(Point strip[], int n, double delta, Pair& closestPair);


int main(){
	
	Point p[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
	Pair pair = {{2, 3}, {12, 30}, 1.5};
	int n = sizeof(p) / sizeof(Point);
	
	qsort(p, n, sizeof(Point), compareY);
	
	printPoints(p, n);
	
	findStripClosestPair(p, n, 1.5, pair);
	
	std::cout << pair.p1.x << pair.p1.y << std::endl;
	std::cout << pair.p2.x << pair.p2.y << std::endl;
	std::cout << pair.dist << std::endl;
	
	return 0;
}


void printPoints(Point* p, const int n){
    
    for(int i = 0; i < n; i++)
        std::cout << "(" << p[i].x << "," << p[i].y << ") ";
    
    std::cout << std::endl;
}


// for internal use by qsort()
int compareX (const void* a, const void* b){
    
    // Need to cast void pointers to a pointer type before dereferencing
    Point *p1 = (Point*)(a);
    Point *p2 = (Point*)(b);        // Note that can't use static_cast<Point*>(a) because const
    
    // return (*p1).x - (*p2).x;
    return p1->x - p2->x;
}


// for internal use by qsort()
int compareY (const void* a, const void* b){
    
    Point *p1 = (Point*)(a);
    Point *p2 = (Point*)(b);
    
    return p1->y - p2->y;
}


// utility function for computing Euclidean distance between two points
double computeDist(Point p1, Point p2){
    
    return sqrt( pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2) );
}


// utility function for finding closest pair of points within a sorted (by Y) strip
void findStripClosestPair(Point strip[], int n, double delta, Pair& closestPair){
    
    for(int i = 0; i < n; i++){
        
        int j = i + 1;
        while(j < n && strip[j].y - strip[i].y < delta){
            
            double dist = computeDist(strip[i], strip[j]);
            if(dist < closestPair.dist){
                closestPair.p1 = strip[i];
                closestPair.p2 = strip[j];
                closestPair.dist = dist;
            }
            
            j++;
        }
    }
}


