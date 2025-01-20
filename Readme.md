setup: 
conda create --name ReCatcher python=3.9
conda activate ReCatcher
pip install -e . 
pip install -r requirements.txt


1- install PMD: https://pmd.github.io/pmd/pmd_userdocs_cpd
2- Add pmd to path, for example in linux we do export PATH=$PATH:{installation path}/pmd-dist-7.8.0-bin/pmd-bin-7.8.0/bin


Edit pylint to add the custom checker: put the file custom_checkers/custom_checker.py inside envs/ReCatcher/lib/python3.9/site-packages/pylint/checkers

before running general logic and performance tests on bigcodebench, please install all dependencies found here: bigcodebench_requirements.txt

