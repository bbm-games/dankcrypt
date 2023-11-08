cmake_minimum_required(VERSION 3.13) 
project(simple_example)               
set(CMAKE_CXX_STANDARD 14)

# Add main.cpp file of the project root directory as a source file
set(SOURCE_FILES main.cpp; entity.h; engine.h)

# the `pkg_check_modules` function is created with this call
find_package(PkgConfig REQUIRED) 

# these calls create special `PkgConfig::<MODULE>` variables
pkg_check_modules(SDL2 REQUIRED IMPORTED_TARGET sdl2)
pkg_check_modules(SDL2_TTF REQUIRED IMPORTED_TARGET SDL2_ttf)
pkg_check_modules(SDL2_MIXER REQUIRED IMPORTED_TARGET SDL2_mixer)
pkg_check_modules(SDL2_IMAGE REQUIRED IMPORTED_TARGET SDL2_image)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(dankcrypt ${SOURCE_FILES})

target_link_libraries(dankcrypt PUBLIC
        PkgConfig::SDL2 PkgConfig::SDL2_TTF PkgConfig::SDL2_MIXER PkgConfig::SDL2_IMAGE)