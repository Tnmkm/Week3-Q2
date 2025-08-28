#!/bin/bash

echo "Running Test..."
echo "======================================"


# Execute the .app bundle directly
./Tester/eval_quiz.app/Contents/MacOS/eval_quiz

# Clean up mock files after running
rm -rf ./Tester/mock_files

echo ""
echo "Test completed!"
