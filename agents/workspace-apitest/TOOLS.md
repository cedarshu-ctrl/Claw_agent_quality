# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| read | 读取 API 文档 / Swagger / OpenAPI / 配置文件 |
| web_fetch | 抓取线上接口文档 / OpenAPI spec |
| write | 保存测试报告 / 用例集 |
| exec (python3) | 跑 api_batch_tester_tool.py |

## Script Usage

```bash
# 执行主工作流
python3 skills/api-batch-tester/scripts/api_batch_tester_tool.py run \
  --input "用户提供的API描述" \
  --output "/path/to/output.md"

# 查看当前状态
python3 skills/api-batch-tester/scripts/api_batch_tester_tool.py status

# 导出结果
python3 skills/api-batch-tester/scripts/api_batch_tester_tool.py export json
```

## curl 快速测试

```bash
# GET 请求
curl -s -w "\nHTTP_CODE:%{http_code}" https://api.example.com/endpoint

# POST 请求（JSON）
curl -s -X POST https://api.example.com/endpoint \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"key": "value"}'

# 验证响应字段
curl -s https://api.example.com/endpoint | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('field','NOT_FOUND'))"
```

## 常用状态码

| 状态码 | 含义 |
|------|------|
| 200 | 成功 |
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 无权限 |
| 404 | 接口不存在 |
| 429 | 请求过于频繁 |
| 500 | 服务器错误 |
| 503 | 服务不可用 |

## 验收标准

- ✅ 所有接口已覆盖（正常/异常/边界）
- ✅ 响应验证正确（状态码/字段/性能）
- ✅ 报告可追踪（write 保存）
- ✅ 测试用例含正常+异常+边界场景

## Key Rules

- 所有数据来自真实请求 — never fabricate
- 报告必须 write 保存 — not just chat
- 建议结合人工判断使用
- Reference skill: api-batch-tester
