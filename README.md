# Log2Text

一个简单实用的工具，用于清理和压缩 Google AI Studio 导出的聊天记录，节省高达 **84%** 的 Token 消耗。

## 💡 背景

在使用 Google AI Studio 时，我们经常需要在不同对话中分享上下文。但直接导出的 JSON 聊天记录包含大量元数据（timestamps、思考过程、格式标签等），占用了大量 Tokens。

Log2Text 能够提取纯对话内容，让你在补充上下文时更加高效。

## ✨ 特性

- 🎯 **高效压缩**：移除所有元数据和思考过程，压缩率高达 84%
- 🧹 **智能清理**：自动合并连续消息，移除 Markdown 格式符号
- 🖥️ **图形界面**：简洁易用的 GUI，无需命令行操作
- 📦 **开箱即用**：提供独立 exe 文件，无需安装 Python

## 📥 安装

### 方式一：直接下载 exe（推荐）

直接从 [Releases](https://github.com/你的用户名/Log2Text/releases) 页面下载 `Log2Text.exe`，双击运行即可。

### 方式二：从源码运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/Log2Text.git
cd Log2Text

# 运行 GUI 程序
python clean_log_gui.py
```

## 🚀 使用方法

1. 从 Google AI Studio 导出你的聊天记录（下载为文件）
2. 打开 Log2Text 程序
3. 点击 **"Browse..."** 选择导出的文件
4. 点击 **"Start Cleaning"** 开始处理
5. 处理完成后，清理后的文件会自动保存在原文件旁边（文件名带 `_cleaned.txt` 后缀）

## 📊 效果对比

| 项目 | 原始文件 | 清理后 | 压缩率 |
|------|---------|--------|--------|
| 文件大小 | 146KB | 23KB | **84%** ↓ |
| 内容 | 包含元数据、思考过程、格式标签 | 仅保留对话内容 | - |

**清理前：**
```json
{
  "runSettings": {...},
  "chunkedPrompt": {
    "chunks": [{
      "role": "model",
      "isThought": true,
      "parts": [{"text": "**Analyzing...**", "thought": true}]
    }]
  }
}
```

**清理后：**
```
**USER**: 你好

**MODEL**: 你好！有什么可以帮你的吗？
```

## 🛠️ 技术栈

- Python 3.x
- tkinter (GUI)
- PyInstaller (打包)

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐
