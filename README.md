![视频封面：把这一期讲什么，压缩成一眼可读](assets/readme/hero.png)

# 月明·视频封面

根据视频内容和出镜形态，制作带有本期主题、角色与叙事元素的三画幅封面。

## 你会得到什么

- 3:4 竖版、4:3 横版、16:9 横版封面
- 已进入图片的标题及与视频对应的视觉主题
- 各画幅的提示词、审看记录与确认版路径

## 试着这样说

```text
用 moonlit-video-cover。给这期视频做三画幅封面，沿用我提供的风格参考。真人视频保留本人身份，标题和画面围绕这一期的核心判断。
```

## 安装与首次使用

将本仓库的完整目录交给支持本地 Skill 的 Agent 安装，保留 `SKILL.md` 与随附资源。已有同名版本时先检查差异；使用版本锁的工作区沿用自身升级机制。

让 Agent 安装：

```text
请安装这个 Skill：https://github.com/zzyong24/moonlit-video-cover
```

也可通过 Skills CLI 安装：

```bash
npx skills add zzyong24/moonlit-video-cover
```

## 配置与依赖

需要视频或可核对的脚本、核心命题、制作模式及身份／风格参考。默认使用 image_gen 生成 PNG/JPEG。真人、数字人和纯 AI 视频分别采用对应角色。

## 数据与使用边界

参考图和提示词交给图像生成服务。无成片时可以做方向稿，不能标为可发布封面；三画幅需分别重构，确认后的文件才交给 moonlit-video-publisher。

## 配套 Skill

[video-publisher](https://github.com/zzyong24/moonlit-video-publisher)

## 详细说明

执行流程与资源导航见 [SKILL.md](SKILL.md)。安装检查不代表真实业务验收；需要外部服务、账号登录或付费生成的步骤，应在使用者自己的环境中验证。

---

月明水清深 · `moonlit-video-cover`

首图为 AI 生成的品牌概念插画，不是工具截图或执行结果。
