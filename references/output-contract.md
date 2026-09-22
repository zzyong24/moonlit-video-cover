# 输出与发布交接合同

## 目录

制作过程：

```text
production/video/<project>/covers/
  source-frames/
  prompts/
  cover-3x4-vNN.png
  cover-4x3-vNN.png
  cover-16x9-vNN.png
  cover-manifest.json
```

用户确认后复制确认版到 `deliverables/covers/`。不要覆盖历史确认版；新方向递增版本号。

## cover-manifest.json

```json
{
  "workId": "W-YYYYMMDD-NNN",
  "productionMode": "html_explainer",
  "title": "企业上 Agent，先拆这 5 层",
  "subtitle": "从一条询盘讲清业务边界",
  "sourceVideo": "/absolute/path/video.mp4",
  "sourceEvidence": ["/absolute/path/keyframe-or-diagram.png"],
  "identityAsset": "/absolute/path/astronaut-or-human-frame.png",
  "contentTypeDeclaration": "含AI生成内容",
  "outputs": {
    "3x4": "/absolute/path/cover-3x4-v01.png",
    "4x3": "/absolute/path/cover-4x3-v01.png",
    "16x9": "/absolute/path/cover-16x9-v01.png"
  },
  "status": "preview_ready"
}
```

## 发布交接

- 小红书：3:4。
- 抖音：3:4 与 4:3。
- B 站：4:3，16:9 作为伴随版。
- 视频号：3:4 与 4:3。

交接前确认文件存在、尺寸正确、标题一致、真人或月明宇航员身份正确、AI 内容声明真实。封面内容或路径变化后必须重新生成发布包指纹。
