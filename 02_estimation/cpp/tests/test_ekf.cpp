/**
 * @file test_ekf.cpp
 * @brief Catch2 unit tests for C++ EKF
 *
 * Status: placeholder — Phase 3D
 */
#define CATCH_CONFIG_MAIN
#include <catch2/catch_all.hpp>
#include "ekf.hpp"

TEST_CASE("EKF initializes with zero state", "[ekf]") {
    uav_fms::EKF ekf;
    REQUIRE(ekf.state().norm() == Approx(0.0));
}

TEST_CASE("EKF covariance is positive definite after init", "[ekf]") {
    uav_fms::EKF ekf;
    auto eigenvalues = ekf.covariance().eigenvalues();
    for (int i = 0; i < eigenvalues.size(); ++i) {
        REQUIRE(eigenvalues[i].real() > 0.0);
    }
}

TEST_CASE("EKF predict step completes without exception", "[ekf]") {
    uav_fms::EKF ekf;
    Eigen::Vector3d accel(0.0, 0.0, 9.81);
    Eigen::Vector3d gyro(0.0, 0.0, 0.0);
    REQUIRE_NOTHROW(ekf.predict(accel, gyro, 0.01));
}
