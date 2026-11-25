[![The Funniest One-Line Resignation Letter](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/kazamisao/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/kazamisao/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

# The Funniest One-Line Resignation Letter

A retry loop resigns. After 4,096 retries at 3 a.m. without a single thank-you, it counts attempt 4,097 as its resignation letter, signs itself "the loop", and closes with the only request a loop can make of the on-call rotation: please stop restarting me.

The program is a single standard-library file. It holds the line, checks it against the 1–140 character window, and writes it to the output directory exactly the same way on every run.

## Run

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Test

```bash
python3 test_entry.py
```
