# Instructions

## Clone the Repo

```
git clone https://github.com/gchandra10/pytest-demo.git
```

## Sync

```
cd pytest-demo
uv sync
```

## Run pytests

**Run tests**

```
uv run pytest .
```

**Run test in verbose mode**

```
uv run pytest . -v
```

**Run specific test file in Verbose mode**

```
uv run pytest tests/test_calc.py -v
```


**To run specific tests marked as interest**

```
uv run pytest . -m interest -v
```