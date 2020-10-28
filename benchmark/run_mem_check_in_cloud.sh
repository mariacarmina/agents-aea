#!/bin/bash

CURR_BRANCH=`git rev-parse --abbrev-ref HEAD`
prepare_cmd="git clone https://github.com/fetchai/agents-aea.git -b $CURR_BRANCH && cd agents-aea/ && pip install -e .[all] && pipenv install -d --deploy --skip-lock --system"
run_check_cmd="bash ./benchmark/checks/run_benchmark_messages_mem.sh"
cmd="($prepare_cmd) &> /dev/null && $run_check_cmd"
kubectl run benchmark-checks --image=gcr.io/fetch-ai-sandbox/aea-benchmark:0.0.0 --overrides='{"spec": {"dnsPolicy": "Default", "hostNetwork": true}}' --restart=Never -it --rm -- bash -c "$cmd"
