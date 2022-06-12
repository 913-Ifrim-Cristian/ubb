#include "Interval.h"
#include <sstream>
#include <vector>

std::istream& operator>>(std::istream& in, Interval& i)
{
    std::string line;
    std::getline(in, line);

    if (line.empty())
        return in;

    std::stringstream ss{ line };
    std::string token;
    std::vector<std::string> res;
    while (std::getline(ss, token, ';')) {
        res.push_back(token);
    }
    if (res.size() != 5)
        return in;

    i.start = std::stoi(res[0]);
    i.end = std::stoi(res[1]);
    i.temperature = std::stoi(res[2]);
    i.precipitations = std::stoi(res[3]);
    i.description = res[4];

    return in;

}

std::string Interval::toString() const
{
    std::stringstream ss;
    ss << "Interval " << this->start << " -> " << this->end << ", temperature: " << this->temperature << ", precipitations possibility: " << this->precipitations << ", description: " << this->description << ".";
    return ss.str();
}
