#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class AtbotsPublisher : public rclcpp::Node
{
public:
    AtbotsPublisher() : Node("atbots_publisher")
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("atbots_topic", 10);

        timer_ = this->create_wall_timer(
            1s,
            std::bind(&AtbotsPublisher::publish_message, this));
    }

private:
    void publish_message()
    {
        auto message = std_msgs::msg::String();
        message.data = "Hi AT Bots";

        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());

        publisher_->publish(message);
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<AtbotsPublisher>());

    rclcpp::shutdown();
    return 0;
}
