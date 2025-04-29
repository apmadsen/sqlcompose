select * from $INCLUDE(included-query1.sql)
union all
select * from $INCLUDE(nested\included-query3.sql)