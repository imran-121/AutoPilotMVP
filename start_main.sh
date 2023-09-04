#!/bin/bash

#This is a Bash script to run main.py and is very first file to be triggred.#
# Please run this file to trigger test automation framework

install_python_libraries() {
    echo -e "             ________________________________________________________________\n"
    echo "              Installing required python packages from config/requiremets.txt"
    echo -e "             ________________________________________________________________\n"
    python -m pip install --upgrade pip
    python -m pip install -r .\\config\\requirements.txt
    echo -e "\nPackage installtion is complete\n\n"
}


run_main_py_file(){
    echo -e "             ________________________________________________________________\n"
    echo -e "                          Triggering (main.py) file"
    echo -e "             ________________________________________________________________\n"
    python_script="main.py"

    if [ -f "$python_script" ]; then
        # Run the Python script
        python "$python_script"
    else
        echo "Python script not found: $python_script"
    fi

    echo -e "Script (main.py) is completed"
}

install_python_libraries
run_main_py_file

echo -e "\nWaiting on key press to shutdown the console. Please hit any key ..."
read -n 1 -s -r key

