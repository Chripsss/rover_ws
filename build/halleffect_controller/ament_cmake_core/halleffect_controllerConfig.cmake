# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_halleffect_controller_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED halleffect_controller_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(halleffect_controller_FOUND FALSE)
  elseif(NOT halleffect_controller_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(halleffect_controller_FOUND FALSE)
  endif()
  return()
endif()
set(_halleffect_controller_CONFIG_INCLUDED TRUE)

# output package information
if(NOT halleffect_controller_FIND_QUIETLY)
  message(STATUS "Found halleffect_controller: 0.0.0 (${halleffect_controller_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'halleffect_controller' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT halleffect_controller_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(halleffect_controller_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${halleffect_controller_DIR}/${_extra}")
endforeach()
