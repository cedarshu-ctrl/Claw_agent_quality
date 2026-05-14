# TOOLS.md - Local Notes

## Tool Chain

| Tool | Purpose |
|------|---------|
| read | 读取代码文件、解析项目结构 |
| write | 保存注释代码 / Markdown API 文档 |

## Script Usage

```bash
python3 skills/code-doc-generator/scripts/code_doc_generator_tool.py run \
  --input "用户需求" \
  --output /path/to/output.md
```

## Docstring 参考

### Python (Google Style)
```python
def fetch_data(url, params=None):
    """Fetches data from the given URL.

    Args:
        url (str): The URL to fetch from.
        params (dict, optional): Query parameters.

    Returns:
        dict: The JSON response.

    Raises:
        ValueError: If URL is invalid.
    """
```

### JSDoc
```javascript
/**
 * Fetches data from the given URL.
 * @param {string} url - URL to fetch.
 * @param {Object} params - Query params.
 * @returns {Promise<Object>} JSON response.
 */
async function fetchData(url, params) {}
```

## Markdown API Doc Template

```markdown
# API Documentation

## fetchData(url, params)

**Description:** ...

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| url | string | ... |

**Returns:** Promise<Object>

**Example:**
```
fetchData('...');
```
```

## Coverage Target

- 所有导出函数/类必须有注释
- 公共 API 100% 覆盖
- README 包含项目概述和使用说明
