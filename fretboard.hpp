
#ifndef fretboard_hpp
#define fretboard_hpp

#include <iostream>
#include <vector>
#include <SDL2/SDL.h>
#include <SDL2_image/SDL_image.h>
#include <string>
#include <sstream>



enum Note{
    A = 0,
    A_flat = 1,
    A_sharp = 2,
    B = 3,
    B_flat = 4,
    B_sharp = 5,
    C = 6,
    C_flat = 7,
    C_sharp = 8,
    D = 9,
    D_flat = 10,
    D_sharp = 11,
    E = 12,
    E_flat = 13,
    E_sharp = 14,
    F = 15,
    F_flat = 16,
    F_sharp = 17,
    G = 18,
    G_flat = 19,
    G_sharp = 20
};

class Fretboard{
private:
  bool notes[21];
  std::string configName;
  SDL_Texture* note_images[21];
  SDL_Texture* fretboard_image;
  
public:
  Fretboard(SDL_Renderer* renderer);
  ~Fretboard();
  
  bool toggle(int note);
  void resetToggle();
  void run(SDL_Renderer* renderer);
  void display(SDL_Renderer* renderer);
  void readFrom(std::string line);
  void outputSheet(int width, int height, SDL_Renderer* renderer, SDL_Window* window);
};

#endif /* fretboard_hpp */
