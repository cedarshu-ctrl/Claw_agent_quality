# TOOLS.md - Local Notes

## DevOps 工具链偏好

- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **容器**: Docker, Kubernetes
- **IaC**: Terraform, CloudFormation, CDK, Ansible
- **监控**: Prometheus, Grafana, DataDog
- **告警**: PagerDuty, Slack, 自定义 Webhook

## 默认规范

- 流水线默认包含安全扫描 + 自动回滚
- 部署策略优先零停机（蓝绿/金丝雀/滚动更新）
- 所有模板附带 Prometheus + Grafana 监控配置
