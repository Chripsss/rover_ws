#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist_stamped.hpp>

class TwistStampedRepublisher : public rclcpp::Node
{
public:
    TwistStampedRepublisher()
    : Node("twist_stamped_republisher")
    {
        this->declare_parameter<std::string>("input_topic", "/cmd_vel");
        this->declare_parameter<std::string>("output_topic", "/halleffect_controller/cmd_vel");

        std::string input_topic = this->get_parameter("input_topic").as_string();
        std::string output_topic = this->get_parameter("output_topic").as_string();

        publisher_ = this->create_publisher<geometry_msgs::msg::TwistStamped>(output_topic, 10);
        subscription_ = this->create_subscription<geometry_msgs::msg::TwistStamped>(
            input_topic, 10,
            [this](geometry_msgs::msg::TwistStamped::UniquePtr msg) {
                publisher_->publish(std::move(msg));
            });
    }

private:
    rclcpp::Publisher<geometry_msgs::msg::TwistStamped>::SharedPtr publisher_;
    rclcpp::Subscription<geometry_msgs::msg::TwistStamped>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TwistStampedRepublisher>());
    rclcpp::shutdown();
    return 0;
}