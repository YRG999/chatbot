#!/bin/bash
export CMAKE_ARGS="-DLLAMA_METAL=on"
export FORCE_CMAKE=1
pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir
#make script executable
#chmod +x install_llamacpp.sh
#run script
# ./install_llamacpp.sh
