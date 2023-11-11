import sys
from sdl2 import *
import sdl2.ext
from sdl2.sdlmixer import *
from sdl2.sdlttf import *
from sdl2.sdlimage import *


def run():
    WINDOW_SIZE = (800, 600)
    RESOURCES = sdl2.ext.Resources(__file__, "dankcrypt/assets")

    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Dankcrypt",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              800, 600, SDL_WINDOW_SHOWN)

    windowsurface = sdl2.SDL_GetWindowSurface(window)

    # Initialize FLAC and MP3 support separately
    for flag in [MIX_INIT_FLAC, MIX_INIT_MP3]:
        Mix_Init(flag)
        err = Mix_GetError() # check for any errors loading library
        if len(err):
            print(err)

    # Initialize a 44.1 kHz 16-bit stereo mixer with a 1024-byte buffer size
    ret = Mix_OpenAudio(44100, sdl2.AUDIO_S16SYS, 2, 1024)
    if ret < 0:
        err = Mix_GetError().decode("utf8")
        raise RuntimeError("Error initializing the mixer: {0}".format(err))
    
    maintheme = Mix_LoadMUS(RESOURCES.get_path('theme.mp3').encode('utf8'))
    print(type(maintheme))
    Mix_PlayMusic(maintheme, loops=99)

    TTF_Init()
    #TTF_OpenFont(RESOURCES.get_path("font/LibreBaskerville-Regular.ttf"), ptsize)

    # Display the splashscreen

    # Initialize JPEG and PNG support separately
    for flag in [IMG_INIT_JPG, IMG_INIT_PNG]:
        IMG_Init(flag)
        err = IMG_GetError() # check for any errors loading library
        if len(err):
            print(err)

    """
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(RESOURCES.get_path("splash.png"))
    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)
    """

    
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC, SDL_RENDERER_ACCELERATED)
    SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND)

    splashimage = IMG_Load(RESOURCES.get_path("splash.png").encode('utf8'))
    splashtexture = SDL_CreateTextureFromSurface(renderer, splashimage)

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
    SDL_RenderClear(renderer)

    SDL_RenderCopy(renderer, splashtexture, None, None)
    SDL_RenderPresent(renderer)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        
        

    Mix_FreeMusic(maintheme)
    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())