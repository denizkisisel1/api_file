#include <iostream>
#include <fstream>

int main() {
    // Write data to a file
    std::ofstream file("data.txt");
    file << "Input data from C++" << std::endl;
    file.close();

    // Wait for Python to complete its work

    // Read Python's result from the file
    std::ifstream resultFile("result.txt");
    std::string result;
    std::getline(resultFile, result);
    resultFile.close();

    // Display the result
    std::cout << "Result from Python: " << result << std::endl;

    return 0;
}
