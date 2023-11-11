#include <iostream>
#include <sstream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

#include <SDL2/SDL_ttf.h>
#include <SDL2/SDL_mixer.h>
#include <vector>
#include <fstream>
#include <map>

#include <cstdlib> // rand and srand
#include <ctime>   // For the time function
#include <cmath>   // abs
// #include "engine.h"
// #include "entity.h"

#define FPS_INTERVAL 1.0 // seconds.

static const char *MAINTHEME = "assets/theme.mp3";
int WINDOW_HEIGHT = 480;
int WINDOW_WIDTH = 640;

using namespace std; // technically a bad practice

// helper function for drawing text
SDL_Rect drawText(SDL_Renderer *mrenderer, string text, int text_size, int x, int y, Uint8 r, Uint8 g, Uint8 b)
{
  TTF_Font *arial = TTF_OpenFont("assets/font.ttf", text_size);
  if (arial == NULL)
  {
    printf("TTF_OpenFont: %s\n", TTF_GetError());
  }
  SDL_Color textColor = {r, g, b};
  SDL_Surface *surfaceMessage = TTF_RenderText_Solid(arial, text.c_str(), textColor);
  if (surfaceMessage == NULL)
  {
    printf("Unable to render text surface: %s\n", TTF_GetError());
  }
  SDL_Texture *message = SDL_CreateTextureFromSurface(mrenderer, surfaceMessage);
  SDL_FreeSurface(surfaceMessage);
  int text_width = surfaceMessage->w;
  int text_height = surfaceMessage->h;
  SDL_Rect textRect{x, y, text_width, text_height};

  SDL_RenderCopy(mrenderer, message, NULL, &textRect);
  TTF_CloseFont(arial);
  return textRect;
}

int main(int argc, char *argv[])
{

  // Get TTF initialized
  if (TTF_Init() < 0)
  {
    cout << "Error initializing SDL_ttf: " << TTF_GetError() << endl;
  }

  // get music setup
  int result = 0;
  int flags = MIX_INIT_MP3;

  if (SDL_Init(SDL_INIT_AUDIO) < 0)
  {
    printf("Failed to init SDL\n");
    exit(1);
  }

  if (flags != (result = Mix_Init(flags)))
  {
    printf("Could not initialize mixer (result: %d).\n", result);
    printf("Mix_Init: %s\n", Mix_GetError());
    exit(1);
  }

  Mix_OpenAudio(22050, AUDIO_S16SYS, 2, 640);
  Mix_Music *music = Mix_LoadMUS(MAINTHEME);
  Mix_VolumeMusic(MIX_MAX_VOLUME / 8);
  Mix_PlayMusic(music, 1);

  // FPS calculation variables
  Uint32 fps_lasttime = SDL_GetTicks(); // the last recorded time.
  Uint32 fps_current;                   // the current FPS.
  Uint32 fps_frames = 0;                // frames passed since the last recorded fps.

  SDL_Window *window = SDL_CreateWindow("dankcrypt",
                                        SDL_WINDOWPOS_UNDEFINED,
                                        SDL_WINDOWPOS_UNDEFINED,
                                        WINDOW_WIDTH,
                                        WINDOW_HEIGHT,
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
  // int success = SDL_QueueAudio(deviceId, wavBuffer, wavLength);
  // SDL_PauseAudioDevice(deviceId, 0);

  // engine window parameters
  // 640 x 480 (width and height)
  int width = 640;
  int height = 480;

  // splash screen loops
  SDL_Surface *splashimage = IMG_Load("assets/splash.png");
  SDL_Texture *splashtexture = SDL_CreateTextureFromSurface(renderer, splashimage);

  Uint32 initTime = SDL_GetTicks();
  Uint32 alpha = 0;

  while (SDL_GetTicks() - initTime < 5000)
  {

    // Get the next event
    SDL_Event event;
    if (SDL_PollEvent(&event))
    {
      if (event.type == SDL_KEYDOWN)
      {
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
    if (alpha <= 255)
    {
      SDL_SetTextureAlphaMod(splashtexture, alpha);
      alpha += 1;
      // printf("%d\n", alpha);
    }

    // CLEAR THE SCREEN WITH A WHITE COLOR:
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    SDL_RenderCopy(renderer, splashtexture, NULL, NULL);
    // draw something centrally
    drawText(renderer, "BBM Games", 30, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 2 - 30 / 2, 255, 215, 0);
    SDL_RenderPresent(renderer);
    // SDL_Delay(10);
  }

  // SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_ADD);
  int mouseX, mouseY; // stores position of mouse
  float clickx, clicky;

  while (true)
  {
    bool left_click = false;
    // Get the next event
    SDL_Event event;
    if (SDL_PollEvent(&event))
    {
      if (event.type == SDL_KEYDOWN)
      {
        switch (event.key.keysym.sym)
        {
        // move viewport according to arrow keys
        case SDLK_LEFT:
          break;
        case SDLK_RIGHT:
          break;
        case SDLK_UP:
          break;
        case SDLK_DOWN:
          break;

        // move player and viewport to center on player
        case SDLK_w:
          break;
        case SDLK_a:
          break;
        case SDLK_s:
          break;
        case SDLK_d:
          break;
        }
      }

      // kill velocity on player once key is lifted
      if (event.type == SDL_KEYUP)
      {
        switch (event.key.keysym.sym)
        {
        case SDLK_w:
          break;
        case SDLK_a:
          break;
        case SDLK_s:
          break;
        case SDLK_d:
          break;
        }
      }

      if (event.type == SDL_MOUSEBUTTONDOWN)
      {
        switch (event.button.button)
        {
        case SDL_BUTTON_LEFT:
        {
          printf("Left mouse button pressed at %d, %d. \n", mouseX, mouseY);
          left_click = true;
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

      if (event.type == SDL_MOUSEBUTTONUP)
      {
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
        // SDL_GetMouseState(&mouseX, &mouseY);
        // printf("MOVED MOUSE\n");
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

    // make default background black
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 225);

    // update and draw FPS
    fps_frames++;
    if (fps_lasttime < SDL_GetTicks() - FPS_INTERVAL * 1000)
    {
      fps_lasttime = SDL_GetTicks();
      fps_current = fps_frames;
      fps_frames = 0;
    }

    drawText(renderer, "FPS: " + to_string(fps_current), 20, 1, 1, 255, 0, 0);

    // * OPTIONAL CODE LINE HERE */
    // draw mouse position
    drawText(renderer, "Cursor at " + to_string(mouseX) + ", " + to_string(mouseY), 20, 1, 480 - 25, 255, 215, 0);

    /* CODE FOR DRAWING THE MENU!*/

    // menu background image code
    SDL_Surface *menuimage = IMG_Load("assets/menubg.png");
    SDL_Texture *menutexture = SDL_CreateTextureFromSurface(renderer, menuimage);
    SDL_RenderCopy(renderer, menutexture, NULL, NULL);

    // title
    drawText(renderer, "Dankcrypt", 40, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 50, 255, 215, 0);

    // menu options
    SDL_Rect rec1 = drawText(renderer, "Load Game", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 125, 255, 215, 0);
    SDL_Rect rec2 = drawText(renderer, "New Game", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 150, 255, 215, 0);
    SDL_Rect rec3 = drawText(renderer, "Settings", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 175, 255, 215, 0);
    SDL_Rect rec4 = drawText(renderer, "Quit", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 200, 255, 215, 0);

    // render text again in another color if the mouse goes over it
    if (mouseX > rec1.x && mouseX < (rec1.x + rec1.w) && mouseY > rec1.y && mouseY < (rec1.y + rec1.h))
    {
      SDL_Rect rec1 = drawText(renderer, "Load Game", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 125, 255, 0, 0);
    }

    if (mouseX > rec2.x && mouseX < (rec2.x + rec2.w) && mouseY > rec2.y && mouseY < (rec2.y + rec2.h))
    {
      SDL_Rect rec2 = drawText(renderer, "New Game", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 150, 255, 0, 0);
    }

    if (mouseX > rec3.x && mouseX < (rec3.x + rec3.w) && mouseY > rec3.y && mouseY < (rec3.y + rec3.h))
    {
      SDL_Rect rec3 = drawText(renderer, "Settings", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 175, 255, 0, 0);
    }
    if (mouseX > rec4.x && mouseX < (rec4.x + rec4.w) && mouseY > rec4.y && mouseY < (rec4.y + rec4.h))
    {
      SDL_Rect rec4 = drawText(renderer, "Quit", 20, WINDOW_WIDTH / 2 - 80, WINDOW_HEIGHT / 4 - 50 / 2 + 200, 255, 0, 0);
      if(left_click){
        // Tidy up
        SDL_CloseAudioDevice(deviceId);
        SDL_FreeWAV(wavBuffer);
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 0;
      }
            
      
    }

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
