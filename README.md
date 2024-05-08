# DVC issue 10419 proof of concept
How to reproduce:
1. Modify `dvc_simple/deep/dep.py`, change string value to `'queue'`.
2. Queue experiment while being inside poetry virtual env:

```bash
poetry install
poetry shell

# inside poetry shell
git status
# make sure only dep.py is changed

dvc exp run -n 'absolute-imports' --queue
# do not run experiment yet
```
3. Revert change from `dep.py`: open file and change string value to `'main'`.
4. While staying inside poetry virtual environment, run queue worker:

```bash
dvc queue start
```
5. Open logs and watch `'main'` being printed while your experiment had string value equal to `'queue'`.

