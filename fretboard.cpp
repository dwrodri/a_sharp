
#include "fretboard.hpp"

Fretboard::Fretboard(SDL_Renderer* renderer){

  std::string path = "assets/fretboard_new.png";
  SDL_Surface* temp = NULL;
  temp = IMG_Load(path.c_str());
  if(!temp) {
    printf( "Unable to load image %s! SDL_image Error: %s\n", path.c_str(), IMG_GetError() );
    
  }
  fretboard_image = SDL_CreateTextureFromSurface(renderer, temp);
  SDL_FreeSurface(temp);
  temp = NULL;

  std::string filePath = "assets/allnotes_";
  char iterator = 'a';
  int j = 0;
  for(int i = 0; i < 21; i++){
    std::string fileName;
    notes[i] = 0;
    if(j == 2){
      fileName = filePath + iterator + "_sharp.png";
    }else if(j == 1){
      fileName = filePath + iterator + "_flat.png";
    }else{
      fileName = filePath + iterator + ".png";
    }
    
    temp = IMG_Load(fileName.c_str());
    note_images[i] = SDL_CreateTextureFromSurface(renderer, temp);
    SDL_FreeSurface(temp);
    temp = NULL;
    
    if(j < 2)
      j++;
    else{
      j = 0;
      iterator++;
    }
  }
  
};
Fretboard::~Fretboard(){

}

bool Fretboard::toggle(int note){
  return notes[note] = !notes[note];
}
void Fretboard::resetToggle(){
  for(int i = 0; i < 21; i++)
    notes[i] = 0;
}
void Fretboard::run(SDL_Renderer* renderer){
  
}
void Fretboard::display(SDL_Renderer* renderer){
  SDL_Rect loc;
  float scale = 2.5;
  loc.x = 0;
  loc.y = 0;
  loc.w = (int)(3089 / scale);
  loc.h = (int)(555 / scale);
  

  SDL_RenderCopy(renderer, fretboard_image, NULL, &loc);
  for(int i = 0; i < 21; i++){
    if(notes[i])
      SDL_RenderCopy(renderer, note_images[i], NULL, &loc);
  }
  
}

void Fretboard::outputSheet(int width, int height, SDL_Renderer* renderer, SDL_Window* window){
  SDL_Surface* screenCap = SDL_CreateRGBSurfaceWithFormat(0, width, height, 32, SDL_PIXELFORMAT_ARGB8888);
  if ( screenCap ) {
    SDL_RenderReadPixels(renderer, NULL,
      SDL_GetWindowPixelFormat(window),
      screenCap->pixels, screenCap->pitch);
  }
  std::string filename = "output/" + configName + ".bmp";
  SDL_SaveBMP(screenCap, filename.c_str());
}
void Fretboard::readFrom(std::string line){
  std::stringstream parser;
  parser << (line);
  std::string noteName;
  std::string scaleName;
  parser >> noteName >> scaleName;
  configName = noteName + " " + scaleName;
  std::string s;
  while(parser >> s){
  
    if(s.compare("A") == 0)
      toggle(0);
    else if(s.compare("A_flat") == 0)
      toggle(1);
    else if(s.compare("A_sharp") == 0)
      toggle(2);
    else if(s.compare("B") == 0)
      toggle(3);
    else if(s.compare("B_flat") == 0)
      toggle(4);
    else if(s.compare("B_sharp") == 0)
      toggle(5);
    else if(s.compare("C") == 0)
      toggle(6);
    else if(s.compare("C_flat") == 0)
      toggle(7);
    else if(s.compare("C_sharp") == 0)
      toggle(8);
    else if(s.compare("D") == 0)
      toggle(9);
    else if(s.compare("D_flat") == 0)
      toggle(10);
    else if(s.compare("D_sharp") == 0)
      toggle(11);
    else if(s.compare("E") == 0)
      toggle(12);
    else if(s.compare("E_flat") == 0)
      toggle(13);
    else if(s.compare("E_sharp") == 0)
      toggle(14);
    else if(s.compare("F") == 0)
      toggle(15);
    else if(s.compare("F_flat") == 0)
      toggle(16);
    else if(s.compare("F_sharp") == 0)
      toggle(17);
    else if(s.compare("G") == 0)
      toggle(18);
    else if(s.compare("G_flat") == 0)
      toggle(19);
    else
      toggle(20);
    
    s.erase();
  }
}
