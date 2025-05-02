select * from $INCLUDE(included-query1.sql)
union all
select * from $INCLUDE(included-query2.sql)
union all
select * from $INCLUDE(included-query1.sql)