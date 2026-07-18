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