#!/bin/bash
# Change to the directory containing the Python script
cd "./test_suit"
# Define the output file for both stdout and stderr
output_file="mutation_output.log"

PYTHON_EXECUTABLE=python

# echo $PYTHON_EXECUTABLE

# Use tee to capture both stdout and stderr and save them to the file
{
    $PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_mutationAdequate -m 
    $PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_mutationAdequate -m --report-html mutation_report.html 
} 2>&1 | tee "$output_file"
