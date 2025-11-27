# Skip Tracing Working Api MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-skip_tracing_working_api`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Skip Tracing Working Api API。

- **PyPI 包名**: `bach-skip_tracing_working_api`
- **版本**: 1.0.0
- **传输协议**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-skip_tracing_working_api
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-skip_tracing_working_api bach_skip_tracing_working_api

# 或指定版本
uvx --from bach-skip_tracing_working_api@latest bach_skip_tracing_working_api
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-skip_tracing_working_api

# 运行（命令名使用下划线）
bach_skip_tracing_working_api
```

## 配置

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |
| `PORT` | 不适用 | 否 |
| `HOST` | 不适用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "skip_tracing_working_api": {
      "command": "uvx",
      "args": ["--from", "bach-skip_tracing_working_api", "bach_skip_tracing_working_api"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\skip_tracing_working_api\server.py` 替换为实际的服务器文件路径。


## 可用工具

此服务器提供以下工具:


### `__trace_by_email`

search people by email

**端点**: `GET /search/byemail`


**参数**:

- `email` (string) *必需*: Enter any email address to search.

- `phone` (string): Example value: 1



---


### `_trace_by_address`

Search people by their address. Just like you search truepeople search.

**端点**: `GET /search/byaddress`


**参数**:

- `street` (string) *必需*: Example value: 3828 Double Oak Ln

- `citystatezip` (string) *必需*: Example value: Irving, TX 75061

- `page` (string): If Records are more than 10, use pagination.



---


### `__trace_by_name_and_address`

search people by name and address

**端点**: `GET /search/bynameaddress`


**参数**:

- `name` (string) *必需*: Example value: James Whitsitt

- `citystatezip` (string) *必需*: Example value: Dallas, TX 75228

- `page` (string): If Records are more than 10, use pagination.



---


### `_trace_by_name`

search people by name

**端点**: `GET /search/byname`


**参数**:

- `name` (string) *必需*: Example value: James E Whitsitt

- `page` (string): If Records are more than 10, use pagination.



---


### `__persondetailsbyid_emailphone`

Get person's details by putting the ID

**端点**: `GET /search/detailsbyID`


**参数**:

- `peo_id` (string) *必需*: Enter the person ID found from any search endpoints above: Ex. 1: p4r4020l80998ll84l64 or, Ex. 2: james-whitsitt_id_G6853526028387863316



---


### `__trace_by_phone`

Search people Using phone number

**端点**: `GET /search/byphone`


**参数**:

- `phoneno` (string) *必需*: Example value: (214)349-3972

- `page` (string): If Records are more than 10, use pagination.



---



## 技术栈

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 1.0.0
