# Log2Text

一个简单的工具，用于清理和压缩 Google AI Studio 导出的聊天记录，节省Token消耗。


在使用 Google AI Studio 时，我们也许需要在不同对话中分享上下文。但直接导出的 JSON 聊天记录包含大量元数据（timestamps、思考过程、格式标签等），占用了大量 Tokens。

Log2Text 能够提取纯对话内容，让你在补充上下文时更加高效。



##  安装

从 [Releases](https://github.com/aukmiriaP/Log2Text/releases) 页面下载 `Log2Text.exe`，双击运行即可。



## 使用方法

1. 从 Google AI Studio 导出你的聊天记录（下载为文件）
2. 打开 Log2Text 程序
3. 点击 **"Browse..."** 选择导出的文件
4. 点击 **"Start Cleaning"** 开始处理
5. 处理完成后，清理后的文件会自动保存在原文件目录中（文件名带 `_cleaned.txt` 后缀）


