


#include "stops.h"

int main() {

    std::cout << "start program\n";

    // run graphics driver

    // run python scraping script

    // extract nodes from the csv file

    std::vector<stop> pokeStops;

    std::fstream file("pokeStops.csv", std::ios::in);
    if(file.is_open()) {
        std::string temp; 
        while (getline(file, temp)) {
            size_t pos1 = temp.find_first_of(',');
            std::string nameIn = temp.substr(1, pos1-1);
            std::string coords = temp.substr(pos1+2);
            size_t pos2 = coords.find_first_of(',');
            std::string xInStr = coords.substr(0, pos2);
            std::string coords2 = coords.substr(pos2);
            size_t pos3 = coords2.find_first_of(';');
            std::string yInStr = coords2.substr(2,pos3-2);
            std::cout << xInStr << ". ." << yInStr << '\n';
            int xIn = (int)(std::stof(xInStr) * (100000));
            int yIn = (int)(std::stof(yInStr)*(100000));
            pokeStops.push_back(stop(nameIn, xIn, yIn));
        }
    }

    /*
    std::cout << "NAME ------- X -------- Y\n";
    for (int i=0; i < pokeStops.size(); i++) {
        std::cout << i+1 << ". " << pokeStops[i].getName() << ' ' << pokeStops[i].getX() << ' ' <<  pokeStops[i].getY() << '\n';
    }
    */

    // run tsp using the nodes
    tspDriver(pokeStops);

    // print the output throught the driver

    return 0;

}