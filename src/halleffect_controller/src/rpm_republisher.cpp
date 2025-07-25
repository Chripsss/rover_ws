#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/float64.hpp>
#include <geometry_msgs/msg/twist_stamped.hpp>

class rpm_republisher: public rclcpp::Node
{
public:
    rpm_republisher() : Node("rpm_to_twiststamped"), rpm_left_(0.0), rpm_right_(0.0)
    {
        rpm_left_sub_ = this->create_subscription<std_msgs::msg::Float64>(
            "/motor_rpm_left", 10,
            [this](const std_msgs::msg::Float64::SharedPtr msg) {
                rpm_left_ = msg->data;
                publish_twist();
            }
        );

        rpm_right_sub_ = this->create_subscription<std_msgs::msg::Float64>(
            "/motor_rpm_right", 10,
            [this](const std_msgs::msg::Float64::SharedPtr msg) {
                rpm_right_ = msg->data;
                publish_twist();
            }
        );

        twist_pub_ = this->create_publisher<geometry_msgs::msg::TwistStamped>("/halleffect_controller/cmd_vel", 10);
    }
private:
    void publish_twist() {
        double rps_left = rpm_left_ / 60.0;
        double rps_right = rpm_right_ / 60.0;
        double diameter = 0.21;
        double wheel_separation = 0.5; // example value
        double circumference = M_PI * diameter;

        double v_left = rps_left * circumference;
        double v_right = rps_right * circumference;

        double linear_velocity = (v_left + v_right) / 2.0;
        double angular_velocity = (v_right - v_left) / wheel_separation;

        auto twist_msg = geometry_msgs::msg::TwistStamped();
        twist_msg.header.stamp = this->now();
        twist_msg.twist.linear.x = linear_velocity;
        twist_msg.twist.angular.z = angular_velocity;
        twist_pub_->publish(twist_msg);
    }

    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr rpm_left_sub_;
    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr rpm_right_sub_;
    rclcpp::Publisher<geometry_msgs::msg::TwistStamped>::SharedPtr twist_pub_;
    double rpm_left_;
    double rpm_right_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<rpm_republisher>());
    rclcpp::shutdown();
    return 0;
}