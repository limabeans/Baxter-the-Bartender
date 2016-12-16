# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cup_grabber: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cup_grabber_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv" NAME_WE)
add_custom_target(_cup_grabber_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cup_grabber" "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv" ""
)

get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv" NAME_WE)
add_custom_target(_cup_grabber_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cup_grabber" "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cup_grabber
)
_generate_srv_cpp(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cup_grabber
)

### Generating Module File
_generate_module_cpp(cup_grabber
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cup_grabber
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cup_grabber_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cup_grabber_generate_messages cup_grabber_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_cpp _cup_grabber_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_cpp _cup_grabber_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cup_grabber_gencpp)
add_dependencies(cup_grabber_gencpp cup_grabber_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cup_grabber_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cup_grabber
)
_generate_srv_lisp(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cup_grabber
)

### Generating Module File
_generate_module_lisp(cup_grabber
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cup_grabber
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cup_grabber_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cup_grabber_generate_messages cup_grabber_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_lisp _cup_grabber_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_lisp _cup_grabber_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cup_grabber_genlisp)
add_dependencies(cup_grabber_genlisp cup_grabber_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cup_grabber_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber
)
_generate_srv_py(cup_grabber
  "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber
)

### Generating Module File
_generate_module_py(cup_grabber
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cup_grabber_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cup_grabber_generate_messages cup_grabber_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/MultiARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_py _cup_grabber_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-abq/Desktop/baxter-waiter/src/cup_grabber/srv/ARPose.srv" NAME_WE)
add_dependencies(cup_grabber_generate_messages_py _cup_grabber_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cup_grabber_genpy)
add_dependencies(cup_grabber_genpy cup_grabber_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cup_grabber_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cup_grabber)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cup_grabber
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(cup_grabber_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cup_grabber)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cup_grabber
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(cup_grabber_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cup_grabber
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(cup_grabber_generate_messages_py std_msgs_generate_messages_py)
