# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.3

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/xilinx/Vitis/2021.2/tps/lnx64/cmake-3.3.2/bin/cmake

# The command to remove a file.
RM = /home/xilinx/Vitis/2021.2/tps/lnx64/cmake-3.3.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src

# Include any dependencies generated for this target.
include CMakeFiles/example_utils.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/example_utils.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/example_utils.dir/flags.make

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o: CMakeFiles/example_utils.dir/flags.make
CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o: ../sw_src/event_timer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o -c /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/event_timer.cpp

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/event_timer.cpp > CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.i

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/event_timer.cpp -o CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.s

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.requires:

.PHONY : CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.requires

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.provides: CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.requires
	$(MAKE) -f CMakeFiles/example_utils.dir/build.make CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.provides.build
.PHONY : CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.provides

CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.provides.build: CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o


CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o: CMakeFiles/example_utils.dir/flags.make
CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o: ../sw_src/xilinx_ocl_helper.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o -c /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/xilinx_ocl_helper.cpp

CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/xilinx_ocl_helper.cpp > CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.i

CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/sw_src/xilinx_ocl_helper.cpp -o CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.s

CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.requires:

.PHONY : CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.requires

CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.provides: CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.requires
	$(MAKE) -f CMakeFiles/example_utils.dir/build.make CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.provides.build
.PHONY : CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.provides

CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.provides.build: CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o


# Object files for target example_utils
example_utils_OBJECTS = \
"CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o" \
"CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o"

# External object files for target example_utils
example_utils_EXTERNAL_OBJECTS =

libexample_utils.a: CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o
libexample_utils.a: CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o
libexample_utils.a: CMakeFiles/example_utils.dir/build.make
libexample_utils.a: CMakeFiles/example_utils.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libexample_utils.a"
	$(CMAKE_COMMAND) -P CMakeFiles/example_utils.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example_utils.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/example_utils.dir/build: libexample_utils.a

.PHONY : CMakeFiles/example_utils.dir/build

CMakeFiles/example_utils.dir/requires: CMakeFiles/example_utils.dir/sw_src/event_timer.cpp.o.requires
CMakeFiles/example_utils.dir/requires: CMakeFiles/example_utils.dir/sw_src/xilinx_ocl_helper.cpp.o.requires

.PHONY : CMakeFiles/example_utils.dir/requires

CMakeFiles/example_utils.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/example_utils.dir/cmake_clean.cmake
.PHONY : CMakeFiles/example_utils.dir/clean

CMakeFiles/example_utils.dir/depend:
	cd /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src /home/kaxiotis/Vitis-Tutorials-Data-Transfer/Hardware_Acceleration/Introduction/design_source/hw_src/CMakeFiles/example_utils.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/example_utils.dir/depend

