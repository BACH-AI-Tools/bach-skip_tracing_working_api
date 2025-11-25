"""
Skip Tracing Working Api MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "skip_tracing_working_api/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Skip Tracing Working Api\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: oneapiproject/skip-tracing-working-api\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://skip-tracing-working-api.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/search/byemail\": {\n      \"get\": {\n        \"summary\": \"📧 / trace by email\",\n        \"description\": \"search people by email\",\n        \"operationId\": \"📧_/_trace_by_email\",\n        \"parameters\": [\n          {\n            \"name\": \"email\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter any email address to search.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"phone\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 1\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/byaddress\": {\n      \"get\": {\n        \"summary\": \"🏠/ trace by address\",\n        \"description\": \"Search people by their address. Just like you search truepeople search.\",\n        \"operationId\": \"🏠/_trace_by_address\",\n        \"parameters\": [\n          {\n            \"name\": \"street\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: 3828 Double Oak Ln\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"citystatezip\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: Irving, TX 75061\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If Records are more than 10, use pagination.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/bynameaddress\": {\n      \"get\": {\n        \"summary\": \"🏡 / trace by name and address\",\n        \"description\": \"search people by name and address\",\n        \"operationId\": \"🏡_/_trace_by_name_and_address\",\n        \"parameters\": [\n          {\n            \"name\": \"name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: James Whitsitt\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"citystatezip\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: Dallas, TX 75228\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If Records are more than 10, use pagination.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/byname\": {\n      \"get\": {\n        \"summary\": \"🙎🏻‍♂️/ trace by name\",\n        \"description\": \"search people by name\",\n        \"operationId\": \"🙎🏻‍♂️/_trace_by_name\",\n        \"parameters\": [\n          {\n            \"name\": \"name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: James E Whitsitt\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If Records are more than 10, use pagination.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/detailsbyID\": {\n      \"get\": {\n        \"summary\": \"❇️ / personDetailsByID (email,phone)\",\n        \"description\": \"Get person's details by putting the ID\",\n        \"operationId\": \"❇️_/_persondetailsbyid_(email,phone)\",\n        \"parameters\": [\n          {\n            \"name\": \"peo_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter the person ID found from any search endpoints above: Ex. 1: p4r4020l80998ll84l64 or, Ex. 2: james-whitsitt_id_G6853526028387863316\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/byphone\": {\n      \"get\": {\n        \"summary\": \"📞 / trace by phone\",\n        \"description\": \"Search people Using phone number\",\n        \"operationId\": \"📞_/_trace_by_phone\",\n        \"parameters\": [\n          {\n            \"name\": \"phoneno\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: (214)349-3972\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If Records are more than 10, use pagination.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "skip-tracing-working-api.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://skip-tracing-working-api.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="skip_tracing_working_api",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "skip-tracing-working-api.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Skip Tracing Working Api MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()