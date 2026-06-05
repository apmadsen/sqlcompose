[![Test](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test.yml/badge.svg)](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test.yml)
[![Coverage](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test-coverage.yml/badge.svg)](https://github.com/apmadsen/sqlcompose/actions/workflows/python-test-coverage.yml)
[![Stable Version](https://img.shields.io/pypi/v/sqlcompose?label=stable&sort=semver&color=blue)](https://github.com/apmadsen/sqlcompose/releases)
![Pre-release Version](https://img.shields.io/github/v/release/apmadsen/sqlcompose?label=pre-release&include_prereleases&sort=semver&color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sqlcompose)
[![PyPI Downloads](https://static.pepy.tech/badge/sqlcompose/week)](https://pepy.tech/projects/sqlcompose)

# SQLCompose

Composable SQL for Python — designed to make large queries easier to structure, reuse, and maintain.

## 🚀 Why this exists

As SQL queries grow, they tend to become difficult to manage:

- Large queries turn into monolithic files
- Logic gets duplicated across transformations
- Small changes become risky and time-consuming
- Reusability is limited

👉 Over time, SQL becomes harder to understand, evolve, and maintain.

This project introduces a simple idea:

**Treat SQL as composable building blocks instead of monolithic scripts.**


## ✨ Features

- 🧩 Split SQL into reusable components
- 🔗 Compose queries from smaller building blocks
- ♻️ Reduce duplication across pipelines
- 🧠 Improve readability and structure
- ⚡ Lightweight and framework-agnostic


## 📦 Use cases

This library is especially useful when working with:

- Data pipelines
- ETL/ELT workflows
- Analytics transformations
- Data warehouse queries
- Systems with repeated SQL logic

👉 Particularly valuable in environments where SQL is a core part of the architecture.


## 🏗 Core idea

Traditional SQL workflows rely on large, self-contained query files.

SQLCompose takes a different approach:

- Break queries into smaller, focused pieces
- Reuse common logic across multiple queries
- Assemble final queries through composition

👉 This enables a more modular and maintainable way of working with SQL.


## 🔄 Reusability & maintainability

By introducing composition:

- Shared logic can be defined once and reused
- Changes can be made in one place instead of many
- Query structure becomes easier to reason about

👉 This reduces both duplication and long-term maintenance cost.


## 🧠 Design philosophy

This project is built around a few key principles:

### 1. Modularity over monoliths
Large SQL files should be broken into smaller, understandable units.

### 2. Reusability by design
Common logic should be shareable across queries and pipelines.

### 3. Simplicity over abstraction
The goal is not to hide SQL, but to organize it better.

### 4. Fit into existing workflows
The library works alongside existing tools and data platforms.


## 🔗 What this enables

With composable SQL, you can:

- Build more maintainable data pipelines
- Reduce duplication across transformations
- Standardize common query patterns
- Improve collaboration across teams

👉 Particularly useful in growing data platforms.


## ⚖️ Trade-offs

| Focus ✅ | Not a goal ❌ |
|---------|--------------|
| SQL composability | Full query engine abstraction |
| Maintainability | Replacing SQL with another DSL |
| Simplicity | Complex orchestration frameworks |

👉 The goal is not to replace SQL —
but to make it **easier to structure at scale**.


## 🧠 Context

This library fits into a broader focus on:

- Data engineering workflows
- Clean architecture principles
- Composable systems
- Reducing duplication in large codebases


## 🎯 When to use

Use this library if you:

- Work with large or growing SQL codebases
- Reuse logic across multiple queries
- Maintain data pipelines or transformations
- Want cleaner, more modular SQL


## 🚫 When not to use

This library may not be necessary if:

- Your SQL queries are small and simple
- Reusability is not a concern
- Query complexity is low


## 🔗 Related projects

Part of a broader focus on:

- Runtime abstractions
- Developer tooling
- Structured Python systems

👉 https://github.com/apmadsen


## 🤝 Contributing

Feedback, ideas, and contributions are welcome!

## ⚙️ Examples

### 1. Execute the script with the filename as an argument and output to the console:
```bash
sqlcompose query.sql
```

### 2. Pipe data into application and output to a file
```bash
cat query.sql | sqlcompose > output.sql
```

### 3. Execute the script with SQL string as argument
```bash
sqlcompose 'select * from $INCLUDE(included-query1.sql)'
```
> NOTE: Different consoles have different limitations, so you may have to switch from single to double quotes to allow for using the dollar sign.

### 4. Import it in another python application or package
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
