#ifndef SIMPLE_CONTROLLER_HPP
#define SIMPLE_CONTROLLER_HPP

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist_stamped.hpp>
#include <std_msgs/msg/float64_multi_array.hpp>
#include <sensor_msgs/msg/joint_state.hpp>
#include <Eigen/Core>


class SimpleController : public rclcpp::Node
{
public:
    SimpleController(const std::string & name);


private:
    void velCallback(const geometry_msgs::msg::TwistStamped & msg);

    void jointCallback(const sensor_msgs::msg::JointState & msg);


    //create a subscriber for the velocity command This subscriber will subscribe to the topic "/cmd_vel" and call the velCallback function
    rclcpp::Subscription<geometry_msgs::msg::TwistStamped>::SharedPtr vel_sub_;
    //create a publisher for the velocity command This publisher will publish to the topic "/wheel_cmd"
    rclcpp::Publisher<std_msgs::msg::Float64MultiArray>::SharedPtr wheel_cmd_pub_;
    //create a subscriber for the joint state This subscriber will subscribe to the topic "/joint_states" and call the jointCallback function
    rclcpp::Subscription<sensor_msgs::msg::JointState>::SharedPtr joint_sub_;

    double wheel_radius_;
    double wheel_separation_;
    Eigen::Matrix2d speed_conversion_;


    double left_wheel_prev_pos_;
    double right_wheel_prev_pos_;

    rclcpp::Time prev_time_;


};

#endif
