#pragma once
#include "Interval.h"
#include <vector>

class Controller
{
	std::vector<Interval> repo;

public:
	Controller();
	std::vector<Interval> getIntervals(int precipitations = -1);
	int totalHours(const std::string& desc, int start);
};

