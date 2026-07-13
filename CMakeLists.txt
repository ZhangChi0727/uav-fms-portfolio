cmake_minimum_required(VERSION 3.20)
project(uav_fms_portfolio VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Compiler warnings
add_compile_options(-Wall -Wextra -Wpedantic)

# Release build optimizations
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    add_compile_options(-O3 -march=native)
endif()

# --- Dependencies ---

# Eigen3 (linear algebra — required for EKF)
find_package(Eigen3 3.4 REQUIRED NO_MODULE)

# pybind11 (Python bindings — optional, enabled by default)
option(BUILD_PYTHON_BINDINGS "Build pybind11 Python bindings" ON)
if(BUILD_PYTHON_BINDINGS)
    find_package(pybind11 QUIET)
    if(pybind11_FOUND)
        message(STATUS "pybind11 found — Python bindings will be built")
    else()
        message(WARNING "pybind11 not found — Python bindings will be skipped")
        set(BUILD_PYTHON_BINDINGS OFF)
    endif()
endif()

# Catch2 (C++ unit testing)
find_package(Catch2 3 QUIET)
if(NOT Catch2_FOUND)
    message(STATUS "Catch2 not found — fetching via FetchContent")
    include(FetchContent)
    FetchContent_Declare(
        Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG        v3.5.4
    )
    FetchContent_MakeAvailable(Catch2)
endif()

# --- EKF Library ---
add_library(ekf_lib
    02_estimation/cpp/src/ekf.cpp
)
target_include_directories(ekf_lib PUBLIC
    02_estimation/cpp/include
)
target_link_libraries(ekf_lib PUBLIC Eigen3::Eigen)

# --- C++ Unit Tests ---
add_executable(ekf_tests
    02_estimation/cpp/tests/test_ekf.cpp
)
target_link_libraries(ekf_tests PRIVATE ekf_lib Catch2::Catch2WithMain)

include(CTest)
include(Catch)
catch_discover_tests(ekf_tests)

# --- Python Bindings ---
if(BUILD_PYTHON_BINDINGS)
    pybind11_add_module(ekf_cpp
        02_estimation/cpp/bindings/ekf_bindings.cpp
    )
    target_link_libraries(ekf_cpp PRIVATE ekf_lib)
    message(STATUS "Python bindings target: ekf_cpp")
endif()
