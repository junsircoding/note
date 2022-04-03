一些常用的 Hive SQL

加列
```sql
ALTER TABLE {table_name} ADD {col_name} {col_type};
```

改列类型
```sql
ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE datatype;
```

加联合唯一索引
```sql
ALTER TABLE {table_name} ADD CONSTRAINT {key_name} UNIQUE ({col_names,});
```

给列加注释
```sql
COMMENT ON COLUMN {table_name}.{col_name} IS '{col_desc}';
```

给列删注释
```sql
COMMENT ON COLUMN {table_name}.{col_name} IS NULL;
```

Hive 删表再建表

1. 根据血缘获取所有子表所在的 tdw 库
2. 拼接 sql 语句，删掉所有外表
    ```sql
    USE {tdw_db};
    DROP TABLE IF EXISTS {ext_tb_name};
    ```
3. 拼接sql语句，重建所有外表
    ```sql
    USE {tdw_db};
    CREATE EXTERNAL TABLE IF NOT EXISTS {ext_tb_name}
    ({col_name} {col_type} COMMENT '{col_desc}',...)
    WITH
    (ip='{ip}',
    port='{port}',
    db_name='{db_name}',
    user_name='{user_name}',
    pwd='{pwd}',
    table_name='public.{ext_tb_name}',
    charset='{charset}',
    db_type='{db_type}');
    ```

### Tips

如果 `create sql` 加了 `if not exist` 语句，那么即使有表，提交 SQL 也不会报错，且不会建表，依然维持原样。
外表后面的 with 语句记录了主表的链接信息，注意外表的库名和主表的库名不要混。
建外表语句中的表结构必须和主表一直，否则建表失败。
