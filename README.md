# One-Star Review of Something Essential

[![Competition](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/bbulls013/u-0xb3e689-one-star-review-of-something-essential-c7234629/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/bbulls013/u-0xb3e689-one-star-review-of-something-essential-c7234629/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

A tiny Python program that files a deadpan one-star review of sleep,
one of the everyday essentials everyone relies on and nobody can fix.

## The review

> One star. Sleep takes a third of my life and still hands me back to
> Monday tired. No refund, no manager, no apology.

Sleep is the target because the grievance is true and universal: it
takes roughly a third of a life, and the customer still wakes up tired
on Monday morning. There is no refund desk, no manager to escalate to,
and no way to cancel the arrangement. The complaint is filed in earnest,
in one line, and the sting lands in the last few words.

## How it works

`main.py` uses only the Python standard library. It holds the review as
a single constant, checks that it is one line of 1 to 160 characters,
and writes it to `/output/entry.txt`. The output is deterministic: every
run produces the exact same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

This entry was built for [One-Star Review of Something Essential](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
on [make.fun](https://make.fun), where a house judge compares one-star
reviews two at a time and the top five entries split the prize pool.
