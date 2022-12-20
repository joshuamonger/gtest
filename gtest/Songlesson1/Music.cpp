#include <iostream>
#include "Song.hpp"

int main() {
    
  Song electric_relaxation;
  electric_relaxation.add_title("Electric Relaxation");
  std::cout << electric_relaxation.get_title() << "\n";

  electric_relaxation.add_artist("A Tribe Called Quest");
  std::cout << electric_relaxation.get_artist() << "\n";

}
