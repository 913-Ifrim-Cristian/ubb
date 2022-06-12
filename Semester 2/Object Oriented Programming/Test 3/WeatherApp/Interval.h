#pragma once
#include <string>
#include <iostream>

class Interval
{
	int start;
	int end;
	int temperature;
	int precipitations;
	std::string description;

public:
	Interval() {}
	Interval(int start, int end, int temperature, const std::string& description);
	int getStart() const { return this->start; }
	int getEnd() const { return this->end; }
	int getTemperature() const { return this->temperature; }
	int getPrecipitations() const { return this->precipitations; }
	std::string getDescription() const { return this->description; }

	friend std::istream& operator>>(std::istream& in, Interval& i);
	std::string toString() const;
};

