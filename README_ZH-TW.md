# Skip Tracing Working Api MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-skip_tracing_working_api`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個 MCP 伺服器，用於存取 Skip Tracing Working Api API。

- **PyPI 套件名**: `bach-skip_tracing_working_api`
- **版本**: 1.0.0
- **傳輸協定**: stdio


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

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |
| `PORT` | 不適用 | 否 |
| `HOST` | 不適用 | 否 |



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

**注意**: 請將 `E:\path\to\skip_tracing_working_api\server.py` 替換為實際的伺服器檔案路徑。


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

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 1.0.0
