#include <iostream>
#include <sstream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <cstdlib>   // rand and srand
//#include "engine.h"
//#include "entity.h"

#define FPS_INTERVAL 1.0 //seconds.

using namespace std; // technically a bad practice


int main( int argc, char *argv[] ) {

  // FPS calculation variables
  Uint32 fps_lasttime = SDL_GetTicks(); // the last recorded time.
  Uint32 fps_current; // the current FPS.
  Uint32 fps_frames = 0; // frames passed since the last recorded fps.

  SDL_Window *window = SDL_CreateWindow("dankcrypt",
    SDL_WINDOWPOS_UNDEFINED,
    SDL_WINDOWPOS_UNDEFINED,
    640,
    480,
    SDL_WINDOW_OPENGL);
  if (window == nullptr)
  {
    SDL_Log("Could not create a window: %s", SDL_GetError());
    return -1;
  }

  SDL_Surface *icon = IMG_Load("assets/icon.png");
  SDL_SetWindowIcon(window, icon);


  SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC || SDL_RENDERER_ACCELERATED);
  if (renderer == nullptr)
  {
    SDL_Log("Could not create a renderer: %s", SDL_GetError());
    return -1;
  }

  SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);
  
  SDL_Init(SDL_INIT_AUDIO);
  
  // load WAV file
  SDL_AudioSpec wavSpec;
  Uint32 wavLength;
  Uint8 *wavBuffer;

  SDL_LoadWAV("assets/music.wav", &wavSpec, &wavBuffer, &wavLength);

  // open audio device
  SDL_AudioDeviceID deviceId = SDL_OpenAudioDevice(NULL, 0, &wavSpec, NULL, 0);

  // play audio
  //int success = SDL_QueueAudio(deviceId, wavBuffer, wavLength);
  //SDL_PauseAudioDevice(deviceId, 0);

  // engine window parameters
  // 640 x 480 (width and height) 
  int width = 640;
  int height = 480;

  // splash screen loops

  SDL_Surface * splashimage = IMG_Load("assets/splash.png");
  SDL_Texture * splashtexture = SDL_CreateTextureFromSurface(renderer, splashimage);

  Uint32 initTime = SDL_GetTicks();

  Uint32 alpha = 0;

  while (SDL_GetTicks() - initTime < 5000)
  { 
    // Get the next event
    SDL_Event event;
    if (SDL_PollEvent(&event))
    {
      if (event.type == SDL_KEYDOWN){
        break;
      }
      if (event.type == SDL_QUIT)
      {
        // Break out of the loop on quit
        break;
      }
    }

    SDL_SetTextureAlphaMod(splashtexture, alpha);
    // fade in effect
    if (alpha <= 255){
      SDL_SetTextureAlphaMod(splashtexture, alpha);
      alpha += 1;
      //printf("%d\n", alpha);
    }

    // CLEAR THE SCREEN WITH A WHITE COLOR:
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    SDL_RenderCopy(renderer, splashtexture, NULL, NULL);
    SDL_RenderPresent(renderer);
    //SDL_Delay(10);
    
  }

  //SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_ADD);

  int mouseX, mouseY; // stores position of mouse
  float clickx, clicky;


  while (true)
  {
    // Get the next event
    SDL_Event event;
    if (SDL_PollEvent(&event))
    {
      if (event.type == SDL_KEYDOWN){
        switch (event.key.keysym.sym)
        {
          // move viewport according to arrow keys
          case SDLK_LEFT:  break;
          case SDLK_RIGHT:  break;
          case SDLK_UP:    break;
          case SDLK_DOWN:   break;

          // move player and viewport to center on player
          case SDLK_w:   break; 
          case SDLK_a:   break;
          case SDLK_s:   break; 
          case SDLK_d:   break; 

        }
      }

      // kill velocity on player once key is lifted
      if (event.type == SDL_KEYUP){
        switch (event.key.keysym.sym)
        {
          case SDLK_w:   break;
          case SDLK_a:   break;
          case SDLK_s:   break;
          case SDLK_d:  break;
        }
      }

      if (event.type == SDL_MOUSEBUTTONDOWN){
        switch (event.button.button)
        {
          case SDL_BUTTON_LEFT:
            {
              printf("Left mouse button pressed at %d, %d. \n", mouseX, mouseY);

              break;
            }
            

          case SDL_BUTTON_RIGHT:
            printf("Right mouse button pressed.\n");
            break;

          default:
            printf("Some other mouse button pressed.\n");
            break;
        }
      }

      if (event.type == SDL_MOUSEBUTTONUP){
        switch (event.button.button)
        {
          case SDL_BUTTON_LEFT:
            break;

          default:
            break;
        }
      }

      if (event.type == SDL_MOUSEMOTION)
      {
        //SDL_GetMouseState(&mouseX, &mouseY);
        //printf("MOVED MOUSE\n");
        mouseX = event.motion.x;
        mouseY = event.motion.y;
      }
      
      if (event.type == SDL_QUIT)
      {
        // Break out of the loop on quit
        break;
      }
    }

    
    // CLEAR THE SCREEN
    SDL_RenderClear(renderer);

  
    // make default background white
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 225);

    
    // update and draw FPS
    fps_frames++;
    if (fps_lasttime < SDL_GetTicks() - FPS_INTERVAL*1000)
    {
      fps_lasttime = SDL_GetTicks();
      fps_current = fps_frames;
      fps_frames = 0;
    }

    //newengine -> drawText(to_string(fps_current),20,1,1,255,0,0);

    // Show the renderer contents
    SDL_RenderPresent(renderer);

  }

  // Tidy up

  SDL_CloseAudioDevice(deviceId);
  SDL_FreeWAV(wavBuffer);
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();

  return 0;
}

