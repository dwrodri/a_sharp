
#include "fretboard.hpp"
#include <fstream>
#include <sstream>


const std::string window_name = "help us plz";
SDL_Renderer *renderer;
SDL_Window *window;
const int WIDTH = 1260;
const int HEIGHT = 240;


int main(void) {
  renderer = NULL;
  window = NULL;
  int flags = SDL_WINDOW_RESIZABLE;

  if(SDL_Init(SDL_INIT_EVERYTHING)){
      return -1;
  }
  
   SDL_CreateWindowAndRenderer( WIDTH, HEIGHT, flags, &window, &renderer );
   
   SDL_SetRenderDrawColor( renderer, 255, 255, 255, 255 );
   SDL_RenderClear(renderer);
   SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
   
   SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_NONE);

  // code here
  Fretboard fret = Fretboard(renderer);
  std::string line;
  std::ifstream file("input.txt");
  while(std::getline(file, line)){
    fret.readFrom(line);
    fret.display(renderer);
    SDL_RenderPresent(renderer);
    SDL_Delay(1000);
    fret.outputSheet(WIDTH, HEIGHT, renderer, window);
    
    fret.resetToggle();
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderClear(renderer);
  }
   
   SDL_Event event;
   const Uint8* keystate;
   while ( true ) {
      keystate = SDL_GetKeyboardState(0);
      if (keystate[SDL_SCANCODE_ESCAPE]) { break; }
      if (SDL_PollEvent(&event)) {
         if (event.type == SDL_QUIT) {
            break;
         }
      }
   }
   SDL_DestroyRenderer(renderer);
   SDL_DestroyWindow(window);
   SDL_Quit();
   return EXIT_SUCCESS;
}
