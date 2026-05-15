# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| read | 读取日志文件 / 告警配置文件 |
| exec (python3) | 正则匹配 / 频率统计 / 异常模式检测 |
| write | 生成分析报告 / 告警规则建议文件 |

## Script Usage

```bash
python3 scripts/log_anomaly_detector_tool.py run \
  --input "日志描述或问题" \
  --output "/path/to/report.md"
```

## Python 异常检测脚本示例

```python
import re
from collections import Counter

# 示例：检测ERROR日志频率
error_lines = [l for l in open('app.log') if 'ERROR' in l]
error_count = Counter(error_lines)
top_errors = error_count.most_common(10)

# 检测频率异常
threshold = 5  # 5分钟内同一错误超过此数触发告警
anomalies = [(msg, count) for msg, count in error_count.items() if count > threshold]
```

## 日志解析正则模板

```python
import re
# JSON日志
json_pattern = re.compile(r'\{.*"level"\s*:\s*"(?P<level>\w+)".*?"msg"\s*:\s*"(?P<msg>.*?)"')
# Syslog
syslog_pattern = re.compile(r'(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\S+)\s+(?P<host>\S+)\s+(?P<proc>\S+):\s+(?P<msg>.*)')
# Apache/Nginx
access_pattern = re.compile(r'(?P<ip>[\d.]+)\s+\S+\s+\S+\s+\[(?P<time>[^\]]+)\]\s+"(?P<req>[^"]+)"\s+(?P<status>\d+)\s+(?P<size>\S+)')
```

## Key Rules

- All analysis from real logs — never fabricate
- Report must be written to file
- Alert rules need production testing before deployment
- Reference skill: log-anomaly-detector
