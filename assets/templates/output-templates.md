# Output Templates

## Complete Package

```markdown
# 创意摘要

# 项目参数

| 字段 | 内容 |
|---|---|
| 输出模式 | complete_package |
| 视频时长 |  |
| 视频比例 | 9:16 / 16:9 / 1:1 / 4:5 / custom |
| 视频方向 | 竖屏 / 横屏 / 方形 / 自定义 |
| 目标平台 | 抖音 / 小红书 / YouTube / PPT / 通用 |
| 时间轴策略 | 默认加入 |

# 故事版设计方案

# Sequence / Beat 拆解

# Shot Map

| Shot | Beat | Time | Frame | Camera | Action/Causality | Audio | Notes |
|---|---|---|---|---|---|---|---|

# 视频时间轴 / Timeline Beat Map

| Time | Visual / Action Beat | Camera / Motion | Scene / Route State | Audio Cue |
|---|---|---|---|---|

# gpt-image2 故事版图片 Prompt

## 中文版

## English Version

# 视频生成 Prompt

## 中文版

## English Version

# 质量自检与生成建议
```

## Storyboard Image Prompt Only

```markdown
# 图片故事版设计摘要

# 分镜表

# gpt-image2 Prompt 中文版

# gpt-image2 Prompt English Version
```

## Video Prompt Only

```markdown
# 视频方案说明

# 项目参数

| 字段 | 内容 |
|---|---|
| 视频时长 |  |
| 视频比例 | 9:16 / 16:9 / 1:1 / 4:5 / custom |
| 视频方向 | 竖屏 / 横屏 / 方形 / 自定义 |
| 目标平台 |  |
| 镜头策略 | one_take / multi_shot / montage / loop / clip_series |
| 节奏类型 | slow_burn / medium_flow / fast_kinetic / staccato / crescendo |
| 是否需要时间轴 | 是，直接视频 Prompt 默认必选 |

# 时间轴设计 / Timeline Beat Map

| Time | Visual / Action Beat | Camera / Motion | Scene / Route State | Audio Cue |
|---|---|---|---|---|

# 中文视频 Prompt

# English Video Prompt

# 可执行性检查
```

## Storyboard Image To Video Prompt

```markdown
# 故事板解析摘要

# 时间轴确认

在基于故事板图片生成视频 Prompt 时，先询问：

> 要不要在视频 Prompt 里加入明确时间轴？A 加入，按每个分镜/动作拆成时间段（推荐） B 不加入，只保留连续视频描述 C 你指定时间分配。

# 视频项目参数

| 字段 | 内容 |
|---|---|
| 视频时长 |  |
| 视频比例 | 继承故事板 / 9:16 / 16:9 / 1:1 / custom |
| 视频方向 | 竖屏 / 横屏 / 方形 / 自定义 |
| 目标平台 |  |
| 时间轴策略 | 用户确认后执行 |

# 视频 Prompt

## 中文版

## English Version
```

## Multi-Clip Package

```markdown
# Global Brief

# Global Video Parameters

| 字段 | 内容 |
|---|---|
| 总时长 |  |
| 视频比例 | 9:16 / 16:9 / 1:1 / 4:5 / custom |
| 视频方向 | 竖屏 / 横屏 / 方形 / 自定义 |
| 目标平台 |  |
| 时间轴策略 | 每个 clip 必须有独立时间轴 |

# Clip Map

| Clip | Duration | Function | Start State | End State | Timeline Required |
|---|---|---|---|---|---|

# Per-Clip Prompts

## Clip 1

### Timeline Beat Map

| Time | Visual / Action Beat | Camera / Motion | Scene / Route State | Audio Cue |
|---|---|---|---|---|

### Prompt

## Clip 2

### Timeline Beat Map

| Time | Visual / Action Beat | Camera / Motion | Scene / Route State | Audio Cue |
|---|---|---|---|---|

### Prompt

# Stitching Notes
```
