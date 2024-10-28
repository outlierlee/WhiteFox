#!/bin/bash
set -e

nl_path=${1:-"Requirements-new/llvm/req"}
generate_dir=${2:-"Prompts-generated-new"}

template_dir="template-llvm"
mode="nl"
cd ..
python prompt_gen.py --optpath=llvm-exec/example.json --nlpath=${nl_path} --mode=${mode}2test --template=${template_dir}/starcoder-mixnl2test-oneshot.txt --outdir=${generate_dir}/llvm
