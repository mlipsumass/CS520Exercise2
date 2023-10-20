#!/bin/sh
# Change to the directory containing the Python script
cd "./test_suit"
coverage run -m pytest test_triangle.py
coverage report -m --include="test_triangle.py"
coverage html -d initial_statement_html


#!/bin/bash
# Change to the directory containing the Python script

coverage run --branch test_triangle.py
coverage report -m --include="test_triangle.py"
coverage html -d initial_decision_html

##python.exe command works for windows system. Use only python if you are working on a UNIX system.


# Check the operating system
PYTHON_EXECUTABLE="python"

# Define the output file for both stdout and stderr
output_file="initial_mutation_output.log"
# Use tee to capture both stdout and stderr and save them to the file
{
    $PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_triangle -m  
    $PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_triangle -m --report-html initial_mutation_report.html
} 2>&1 | tee "$output_file"