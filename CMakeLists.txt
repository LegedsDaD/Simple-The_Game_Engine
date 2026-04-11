cmake_minimum_required(VERSION 3.20)

project(Simple VERSION 1.1.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include(FetchContent)

# pybind11
FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.13.6.tar.gz
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)
FetchContent_MakeAvailable(pybind11)

# GLFW (windowing + input)
set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)
# Manylinux images sometimes have partial Wayland detection but miss `wayland-scanner`,
# which breaks configuration. Force X11-only for maximum wheel compatibility.
set(GLFW_BUILD_WAYLAND OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_X11 ON CACHE BOOL "" FORCE)
FetchContent_Declare(
  glfw
  URL https://github.com/glfw/glfw/archive/refs/tags/3.4.tar.gz
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)
FetchContent_MakeAvailable(glfw)

# manylinux2014 (CentOS 7) headers are sensitive to feature macros.
# We need:
# - clock_gettime/CLOCK_MONOTONIC (timer) and
# - O_CLOEXEC (joystick hotplug)
# when building GLFW from source.
if (UNIX AND NOT APPLE)
  if (TARGET glfw)
    target_compile_definitions(glfw PRIVATE _POSIX_C_SOURCE=200809L _GNU_SOURCE=1)
  endif()
endif()

pybind11_add_module(
  _simple_core
  cpp_core/bindings/bindings.cpp
  cpp_core/platform/gl_loader.cpp
  cpp_core/window/window.cpp
  cpp_core/input/input.cpp
  cpp_core/renderer/renderer.cpp
  cpp_core/renderer/shader.cpp
  cpp_core/renderer/texture.cpp
  cpp_core/scene/entity.cpp
  cpp_core/scene/scene.cpp
  cpp_core/engine/engine.cpp
  cpp_core/branding/branding.cpp
)

if (APPLE)
  target_sources(_simple_core PRIVATE cpp_core/platform/window_hints_macos.cpp)
else()
  target_sources(_simple_core PRIVATE cpp_core/platform/window_hints_common.cpp)
endif()

target_include_directories(_simple_core PRIVATE cpp_core)
target_link_libraries(_simple_core PRIVATE glfw)

if (UNIX AND NOT APPLE)
  # glibc on older distros may still require librt for clock_gettime at link time.
  find_library(RT_LIBRARY rt)
  if (RT_LIBRARY)
    target_link_libraries(_simple_core PRIVATE ${RT_LIBRARY})
  endif()
endif()

if (WIN32)
  target_link_libraries(_simple_core PRIVATE opengl32)
elseif(APPLE)
  find_library(COCOA_LIBRARY Cocoa REQUIRED)
  find_library(IOKIT_LIBRARY IOKit REQUIRED)
  find_library(COREVIDEO_LIBRARY CoreVideo REQUIRED)
  find_library(OPENGL_LIBRARY OpenGL REQUIRED)
  target_link_libraries(_simple_core PRIVATE ${COCOA_LIBRARY} ${IOKIT_LIBRARY} ${COREVIDEO_LIBRARY} ${OPENGL_LIBRARY})
else()
  find_package(OpenGL REQUIRED)
  target_link_libraries(_simple_core PRIVATE OpenGL::GL)
endif()

target_compile_definitions(_simple_core PRIVATE GLFW_INCLUDE_NONE=1)

if (MSVC)
  target_compile_options(_simple_core PRIVATE /W4 /permissive-)
else()
  target_compile_options(_simple_core PRIVATE -Wall -Wextra -Wpedantic)
endif()

# Wheel layout:
# - Install Python package from python_api/ as site-packages/simple/
# - Install extension into that same package.
install(
  DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python_api/
  DESTINATION simple
  PATTERN "__pycache__" EXCLUDE
  PATTERN "*.pyc" EXCLUDE
  PATTERN "*.pyo" EXCLUDE
)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/assets/ DESTINATION simple/assets)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/templates/ DESTINATION simple/templates)
install(
  TARGETS _simple_core
  LIBRARY DESTINATION simple
  RUNTIME DESTINATION simple
  ARCHIVE DESTINATION simple
)
