FROM arm32v7/ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y remove x264 libx264-dev
RUN apt-get -y install build-essential cmake pkg-config yasm git gfortran libpng-dev
RUN apt-get -y install libtiff5-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
RUN apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
RUN apt-get -y install libxine2-dev libv4l-dev
RUN apt-get -y install libgstreamer1.0-dev libgstreamer-opencv1.0-0 libgstreamer-plugins-base1.0-dev libgtk2.0-dev libtbb-dev qt5-default libatlas-base-dev
RUN apt-get -y install libmp3lame-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libopencore-amrnb-dev libopencore-amrwb-dev
RUN apt-get -y install libavresample-dev x264 v4l-utils libprotobuf-dev protobuf-compiler libgoogle-glog-dev libgflags-dev
RUN apt-get -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
RUN apt-get -y install python3-dev python3-pip python3-testresources python3-setuptools
RUN pip3 install --upgrade pip
RUN pip3 install numpy requests
RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git
RUN cd opencv && mkdir build && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
 -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules -D ENABLE-NEON=ON -D ENABLE_VFPV3=ON -D BUILD_TESTS=OFF -D OPENCV_ENABLE_NONFREE=ON \
 -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=OFF -D BUILD_EXAMPLES=OFF .. && make -j4 && make install && ldconfig
