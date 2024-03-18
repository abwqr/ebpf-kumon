FROM ubuntu

# Copy files from the host system into the Docker build context

#COPY /lib/modules/6.5.0-15-generic/build /tmp

RUN apt-get update && \
    apt-get install -y \
        bison \
        build-essential \
        cmake \
        flex \
        git \
        libedit-dev \
        libllvm11 \
        llvm-11-dev \
        libclang-11-dev \
        zlib1g-dev \
        libelf-dev \
        libfl-dev \
        python3-distutils \
        python3-setuptools \
        zip 
RUN apt-get install linux-headers-$(uname -r) -y
        
ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y expect        

RUN git clone https://github.com/iovisor/bcc.git

WORKDIR /bcc/build
RUN cmake .. && \
    make && \
    make install

RUN cmake -DPYTHON_CMD=python3 .. && \
    cd src/python/ && \
    make && \
    make install && \
    cd ..

# Copy files from the Docker build context into the image
#COPY /tmp/build /bcc/build

COPY parsers /bcc/parsers

WORKDIR /bcc
RUN chmod +x parsers/pipeline.sh
CMD ["bash", "./parsers/pipeline.sh"]

