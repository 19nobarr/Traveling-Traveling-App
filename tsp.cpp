#include "stops.h"

void primsAlgorithm();
void twoOpt();
void branchAndBound();

void tspDriver(std::vector<stop> &pokeStops) {

	std::cout << "training... \n";

	primsAlgorithm();
	twoOpt();
	branchAndBound();

	return;
}

double calculateEuclidean(Coordinate& a, Coordinate& b) {
	return sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2) * 1.0);
}

void primsAlgorithm() {

	double weight = 0.0;

	primsTable[0].edgeParent = 0;
	primsTable[0].edgeWeight = 0.0;
	int lowestIndex = 0;

	for (size_t i = 0; i < pokeCoords.size(); i++) {

		double lowestEdge = std::numeric_limits<double>::infinity();


		for (int j = 0; j < (int)pokeCoords.size(); j++) {
			if (primsTable[j].edgeFound == false) {
				double dV = primsTable[j].edgeWeight;
				if (dV < lowestEdge) {
					lowestEdge = dV;
					lowestIndex = j;
				}
			}
		}

		primsTable[lowestIndex].edgeFound = true;

		for (int k = 0; k < (int)pokeCoords.size(); k++) {
			if (primsTable[k].edgeFound == false && isCompatible(k, lowestIndex)) {
				double dW = calculateEuclidean(pokeCoords[k], pokeCoords[lowestIndex]);
				if (dW < primsTable[k].edgeWeight) {
					primsTable[k].edgeParent = lowestIndex;
					primsTable[k].edgeWeight = dW;
				}
			}
		}

		weight += primsTable[lowestIndex].edgeWeight;

		Coordinate temp;
		if (lowestIndex < primsTable[lowestIndex].edgeParent) {
			temp.x = lowestIndex;
			temp.y = primsTable[lowestIndex].edgeParent;
		}
		else {
			temp.x = primsTable[lowestIndex].edgeParent;
			temp.y = lowestIndex;
		}
		minSpanTree.push(temp);
	}
	std::cout << weight << '\n';


	std::cout << "finished prim's\n";
	return;
}

void twoOpt() {

	std::cout << "finished two opt\n";
	return;
}

void branchAndBound() {


	std::cout << "finished branch and bound\n";
	return; 
}