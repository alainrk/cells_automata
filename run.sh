FILE=${1}
if [[ -z $FILE ]]; then
  echo "No file to run has been given..."
  echo "./run file.py"
  exit 1
fi

java -jar processing-py/processing-py.jar $FILE