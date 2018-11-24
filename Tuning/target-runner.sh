error() {
    echo "`TZ=UTC date`: $0: error: $@"
    exit 1
}

EXE=/anaconda3/bin/python
FILE=/Users/lucas.adriano/Projetos/PIN3/MaxCliqueVertexWeightedProblem/irace.py
FIXED_PARAMS=""

CONFIG_ID=$1
INSTANCE_ID=$2
SEED=$3
INSTANCE=$4
shift 4 || error "Not enough parameters"
CONFIG_PARAMS=$*

STDOUT=c${CONFIG_ID}-${INSTANCE_ID}-${SEED}.stdout
STDERR=c${CONFIG_ID}-${INSTANCE_ID}-${SEED}.stderr

if [ ! -x "${EXE}" ]; then
    error "${EXE}: not found or not executable (pwd: $(pwd))"
fi

$EXE $FILE ${FIXED_PARAMS} -i $INSTANCE --seed ${SEED} ${CONFIG_PARAMS} 1> ${STDOUT} 2> ${STDERR}

if [ -s "${STDOUT}" ]; then
    COST=$(tail -n 1 ${STDOUT} | grep -e '^[[:space:]]*[+-]\?[0-9]' | cut -f1)
    echo "$COST"
    rm -f "${STDOUT}" "${STDERR}"
    exit 0
else
    error "${STDOUT}: No such file or directory"
fi
