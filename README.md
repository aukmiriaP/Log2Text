# Log2Text

一个简单实用的工具，用于清理和压缩 Google AI Studio 导出的聊天记录，节省Token消耗。


在使用 Google AI Studio 时，我们也许需要在不同对话中分享上下文。但直接导出的 JSON 聊天记录包含大量元数据（timestamps、思考过程、格式标签等），占用了大量 Tokens。

Log2Text 能够提取纯对话内容，让你在补充上下文时更加高效。



##  安装

### 方式一：直接下载 exe

直接从 [Releases](https://github.com/你的用户名/Log2Text/releases) 页面下载 `Log2Text.exe`，双击运行即可。

### 方式二：从源码运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/Log2Text.git
cd Log2Text

# 运行 GUI 程序
python clean_log_gui.py
```

## 使用方法

1. 从 Google AI Studio 导出你的聊天记录（下载为文件）
2. 打开 Log2Text 程序
3. 点击 **"Browse..."** 选择导出的文件
4. 点击 **"Start Cleaning"** 开始处理
5. 处理完成后，清理后的文件会自动保存在原文件旁边（文件名带 `_cleaned.txt` 后缀）


