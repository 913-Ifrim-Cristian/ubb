#include "Controller.h"
#include <fstream>
#include <algorithm>

Controller::Controller()
{
	std::ifstream f("repo.txt");
	Interval d;
	while (f >> d) {
		repo.push_back(d);
		if (f.eof())
			break;
	}
}

std::vector<Interval> Controller::getIntervals(int precipitations)
{
	std::vector<Interval> res{};

	for (auto it : this->repo) {
		if (precipitations == -1 || it.getPrecipitations() < precipitations)
			res.push_back(it);
	}

	std::sort(res.begin(), res.end(), [](Interval a, Interval b) {
		return a.getStart() < b.getStart();
		});

	return res;
}

int Controller::totalHours(const std::string& desc, int start)
{
	int sum = 0;
	for (auto it : this->repo) {
		if (it.getStart() > start && it.getDescription().find(desc) != std::string::npos)
			sum += -it.getStart() + it.getEnd();
		else if (it.getStart() <= start && start < it.getEnd() && it.getDescription().find(desc) != std::string::npos)
			sum += it.getEnd() - start;
	}
	return sum;
}
