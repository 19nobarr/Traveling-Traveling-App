#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

class stop {

public:
    stop() {
        stopName = "";
        x = 0;
        y = 0;
    }
    stop(std::string nameIn, int xIn, int yIn) {
        stopName = nameIn;
        x = xIn;
        y = yIn;
    }
    std::string getName() {
        return stopName;
    }
    int getX() {
        return x;
    }
    int getY() {
        return y;
    }

private:
    std::string stopName;
    int x;
    int y;
};

void tspDriver(std::vector<stop> pokeStops);