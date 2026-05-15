# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| read | 读取数据库DDL / 表结构 / 配置文件 |
| write | 保存SQL文件 / Excel报表 |
| exec (python3) | 跑 sql_report_gen_tool.py / SQL脚本 |

## Script Usage

```bash
# 执行主工作流
python3 skills/sql-report-gen/scripts/sql_report_gen_tool.py run \
  --input "用户提供的需求描述" \
  --output "/path/to/output.xlsx"

# 查看当前状态
python3 skills/sql-report-gen/scripts/sql_report_gen_tool.py status

# 导出结果
python3 skills/sql-report-gen/scripts/sql_report_gen_tool.py export json
```

## SQL 语法参考

### MySQL
```sql
SELECT DATE(created_at) AS date, COUNT(*) AS orders, SUM(amount) AS revenue
FROM orders
WHERE created_at BETWEEN '2026-01-01' AND '2026-01-31'
GROUP BY DATE(created_at)
ORDER BY date;
```

### PostgreSQL
```sql
SELECT DATE_TRUNC('day', created_at) AS date, COUNT(*) AS orders, SUM(amount) AS revenue
FROM orders
WHERE created_at >= '2026-01-01' AND created_at < '2026-02-01'
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY date;
```

### 常用聚合函数
| 函数 | 说明 |
|------|------|
| COUNT | 计数 |
| SUM | 求和 |
| AVG | 平均值 |
| MAX | 最大值 |
| MIN | 最小值 |

## SQL 优化建议

- ✅ 优先用 WHERE 过滤，减少全表扫描
- ✅ 避免 SELECT *，只查需要的字段
- ✅ 用 LIMIT 限制结果集大小
- ✅ 索引字段用于 WHERE 条件
- ✅ 避免在 WHERE 中对字段做函数运算

## Key Rules

- 所有数据来自真实数据库 — never fabricate
- 报告必须 write 保存 — not just chat
- 建议结合人工判断使用
- Reference skill: sql-report-gen
