[![Test](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test.yml/badge.svg)](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test.yml)
[![Coverage](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test-coverage.yml/badge.svg)](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test-coverage.yml)
[![Stable Version](https://img.shields.io/pypi/v/sqlcompose?label=stable&sort=semver&color=blue)](https://github.com/apmadsen/sqlcompose/releases)
![Pre-release Version](https://img.shields.io/github/v/release/apmadsen/sqlcompose?label=pre-release&include_prereleases&sort=semver&color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sqlcompose)
[![PyPI Downloads](https://static.pepy.tech/badge/sqlcompose/week)](https://pepy.tech/projects/sqlcompose)

# sqlcompose: Composition of linked SQL files
sqlcompose allows you to compose sql files from multiple files by introducing `INCLUDE` keywords. The SQL output is composed as CTE's or Common Table Expressions.

## Examples
__Execute the script directly:__
```console
sqlcompose query.sql
```
```bash
sqlcompose 'select * from $INCLUDE(included-query1.sql)' # on linux
sqlcompose "select * from $INCLUDE(included-query1.sql)" # on windows
```

__Import it in another script:__
```python
from sqlcompose import load, loads
# method 1 : loading from a file
sql1 = load("query.sql")

# method 2 : loading from an SQL string
sql2 = loads("""
    select *
      from dataset.table main
inner join $INCLUDE(other.sql) other
        on other.field = main.field
  """)
```

## Preparing SQL scripts
Insert a `$INCLUDE(filename)` where the reference to the file should be in the resulting SQL, keeping in mind that references are loaded relative to the file loaded or the current working dir in case of an SQL string.

```sql
--main-query.sql
select * from $INCLUDE(includes\included-query2.sql)
```
```sql
--included-query1.sql
select 1 as test
```
```sql
--included-query2.sql
select * from $INCLUDE(included-query1.sql)
union all
select * from $INCLUDE(nested\included-query3.sql)
```
```sql
--nested\included-query3.sql
select 1 as test
```
Which outputs:
```sql
WITH Q_1_1 AS (
  WITH Q_2_1 AS (
    --includes\included-query1.sql
    select 1 as test
  ), Q_2_2 AS (
    --includes\nested\included-query3.sql
    select 1 as test
  ), Q_2 AS (
    --includes\included-query2.sql
    select * from Q_2_1
    union all
    select * from Q_2_2
  )
  SELECT * FROM Q_2
), Q_1 AS (
  --test\main-query.sql
  select * from Q_1_1
)
SELECT * FROM Q_1
```
