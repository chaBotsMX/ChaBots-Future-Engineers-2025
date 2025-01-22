FROM ros:humble

# Instalar dependencias adicionales y herramientas para rplidar
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-demo-nodes-cpp \
    ros-humble-demo-nodes-py \
    ros-humble-rviz2 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear el workspace
WORKDIR /ros2_ws
RUN mkdir -p /ros2_ws/src

# Copiar el código del proyecto
COPY src/ /ros2_ws/src/

# Configurar el entorno
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
