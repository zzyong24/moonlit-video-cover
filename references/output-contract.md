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
  # only when requested by placement: cover-9x16-vNN.png
  cover-manifest.json
```

用户确认或按明确委托完成Agent验收后，复制采用版到 `deliverables/covers/`。不要覆盖历史确认版；新方向递增版本号。

## cover-manifest.json

```json
{
  "workId": "W-YYYYMMDD-NNN",
  "productionMode": "html_explainer",
  "title": "企业上 Agent，先拆这 5 层",
  "subtitle": "从一条询盘讲清业务边界",
  "sourceVideo": "/absolute/path/video.mp4",
  "sourceEvidence": ["/absolute/path/keyframe-or-diagram.png"],
  "identityAsset": "/absolute/path/fixed-identity-portrait.png",
  "action": {
    "id": "workspace-action-id",
    "name": "本期人物动作",
    "pose": "身体朝向、双手动作、视线落点与道具互动",
    "meaning": "动作如何表达本期命题"
  },
  "actionSelection": {
    "library": "maintenance/cover-action-library.json",
    "comparedCovers": ["/absolute/path/recently-used-cover.png"],
    "difference": "与已审看的往期动作区别；沿用时记录原因",
    "scope": "实际审看范围，不推断全历史"
  },
  "platformPlacement": ["douyin-feed-cover", "bilibili-video-cover"],
  "ratioEvidence": "creator upload UI preview, checked YYYY-MM-DD",
  "contentTypeDeclaration": "含AI生成内容",
  "outputs": {
    "3x4": "/absolute/path/cover-3x4-v01.png",
    "4x3": "/absolute/path/cover-4x3-v01.png",
    "16x9": "/absolute/path/cover-16x9-v01.png",
    "9x16": null
  },
  "status": "preview_ready"
}
```

## 画幅与发布交接

| 画幅 | 本地默认候选 | 常见用途 | 制作方式 |
|---|---:|---|---|
| 3:4 | 1080×1440 | 竖版信息流封面 | 竖向重排；标题、人像、内容板保持可读 |
| 4:3 | 1440×1080 | 横版视频封面 | 横向重排；标题与证据并置 |
| 16:9 | 1920×1080 | 横版空间或归档入口 | 按宽画幅重排；不能从 4:3 直接裁切 |
| 9:16 | 1080×1920 | 明确要求全屏竖封面的入口 | 单独排版并检查顶部/底部 UI 遮挡；不从 3:4 拉伸 |

本表描述工作区默认候选尺寸，不替代平台要求。交接前在该平台、该入口的当期上传界面核对比例、尺寸和裁切预览；规格不符时另排版并把依据写入 manifest。平台常见选择按已有本地发布流程参考：小红书 3:4；抖音和视频号按目标入口选 3:4 或横版；B 站以横版封面为主并按需另做 16:9。不要据此推断未查看的入口必定接受某比例。

交接前确认文件存在、像素尺寸正确、标题一致、本人身份可信、AI 内容声明真实。检查手部结构、持物互动和视线是否表达所选动作；生成、技术审看、平台裁切与用户认可分别记录。动作总览仅作姿态参考；是否逐张用户确认按工作区明确委托处理，无委托时确认，有委托时记录Agent验收，不能伪记用户逐图确认；采用后回填工作区动作库，不能把候选数量写成已采用数量。比例检查要看画面本身：目标画幅不能把另一比例的成图缩进画布，也不能留下非设计的黑边、空白边或 letterbox；背景色延伸到画布边缘属于正常设计。再用全尺寸图、缩略图和平台实际裁切预览核对标题、人物与内容证据是否完整可读。各项通过后再交接。封面内容或路径变化后必须重新生成发布包指纹。

逐平台交接须记录platform、placement/slot、ratio、width/height、assetPath、nativeEvidence（尚未出现时如实pending）以及acceptedBy（user或delegated-agent）。同画幅可复用通过该平台安全区检查的成图，但不同画幅必须分别排版。生产稿检查和上传后的真实槽位裁切分阶段完成。

## 生产阶段备齐全部目标规格

在生成前建立本期平台/入口矩阵，按制作合同准备各入口需要的成图，并以真实规格证据复核。当前已实测B站2026-10-12封面编辑器明确要求首页推荐4:3、个人空间16:9两幅，必须分别生成并关闭双比例同步改动，不能只上传4:3让平台自动裁出宽幅。小红书按本期计划选择3:4竖版或4:3横版入口，抖音需3:4与4:3，视频号双槽需两幅、明确共用3:4槽只需竖版。当前这组平台完整画幅集合为3:4、4:3、16:9；不是每个平台固定三幅，也不是生成7张不同画幅。按每个槽位独立验证画幅和安全区后，同规格且安全区适用的成图可复用。

制作阶段完成比例导出与原图/缩略图验收，再交给发布器直接替换。发布阶段禁止临时裁切、拉伸、补边或重排；发现入口规格变化回到生产阶段补图。native crop确认只接受保持已生成成图原比例和完整内容的操作。
