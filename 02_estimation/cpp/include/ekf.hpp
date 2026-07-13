/**
 * @file ekf.hpp
 * @brief Extended Kalman Filter — C++17 implementation
 *
 * Header-only interface. See ekf.cpp for implementation.
 * Requires Eigen3.
 *
 * Status: placeholder — Phase 3D
 */
#pragma once
#include <Eigen/Dense>

namespace uav_fms {

class EKF {
public:
    static constexpr int STATE_DIM   = 16;
    static constexpr int GPS_MEAS_DIM = 6;
    static constexpr int VO_MEAS_DIM  = 6;

    using StateVec   = Eigen::Matrix<double, STATE_DIM, 1>;
    using StateMat   = Eigen::Matrix<double, STATE_DIM, STATE_DIM>;
    using GpsMeasVec = Eigen::Matrix<double, GPS_MEAS_DIM, 1>;

    EKF();

    void predict(const Eigen::Vector3d& accel,
                 const Eigen::Vector3d& gyro,
                 double dt);

    void update_gps(const GpsMeasVec& z_gps);

    [[nodiscard]] const StateVec& state() const { return x_; }
    [[nodiscard]] const StateMat& covariance() const { return P_; }

private:
    StateVec x_;
    StateMat P_;
    StateMat Q_;
    Eigen::Matrix<double, GPS_MEAS_DIM, GPS_MEAS_DIM> R_gps_;

    StateMat compute_jacobian_F(const Eigen::Vector3d& accel,
                                const Eigen::Vector3d& gyro,
                                double dt) const;
};

} // namespace uav_fms
