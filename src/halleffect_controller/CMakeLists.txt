cmake_minimum_required(VERSION 3.8)
project(halleffect_controller)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)



include_directories(include)

include_directories( ${EIGEN3_INCLUDE_DIR} )

add_executable(simple_controller src/simple_controller.cpp)
ament_target_dependencies(simple_controller
  rclcpp
  std_msgs
  geometry_msgs
  ${Eigen_LIBRARIES}
  sensor_msgs
  nav_msgs
  tf2
  tf2_ros
)

add_executable(noisy_controller src/noisy_controller.cpp)
ament_target_dependencies(noisy_controller
  rclcpp
  geometry_msgs
  ${Eigen_LIBRARIES}
  sensor_msgs
  nav_msgs
  tf2
  tf2_ros
)

add_executable(joystick_republisher src/joystick_republisher.cpp)
ament_target_dependencies(joystick_republisher
 rclcpp 
 geometry_msgs
 )

install(
  DIRECTORY include 
  DESTINATION include
)


install (TARGETS 
  simple_controller
  noisy_controller
  joystick_republisher
  DESTINATION lib/${PROJECT_NAME}

)


install(
  DIRECTORY config launch 
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()


endif()

ament_package()
