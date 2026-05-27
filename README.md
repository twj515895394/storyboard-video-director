# storyboard-video-director

> 中文版在前，English version follows.

## 中文版

### AI 故事版与视频分镜导演 Skill

`storyboard-video-director` 是一个面向 **AI 视频制作、影视前期、故事版设计、gpt-image2 图片故事版 Prompt、Seedance / 通用视频 Prompt** 的标准 Skill 包。

它不是几段固定提示词，而是一套可复用的影视前期工作流：

```text
简短主题
→ 创意方向发散
→ grill-me 式追问
→ 故事扩展
→ Sequence / Beat 拆解
→ Shot Map
→ gpt-image2 故事版图片 Prompt
→ Seedance / 通用视频 Prompt
→ 可选 Multi-Clip 拆分
→ 案例入库 / 模板沉淀
```

本仓库按标准 Skill 包思路组织：**仓库根目录就是 Skill 目录**，`SKILL.md` 是入口，`references/`、`assets/`、`schemas/` 和 `scripts/` 用于渐进式加载规则、模板、示例和自动化脚本。

---

### 适合什么场景

- 根据一句主题生成影视故事版方案；
- 为 `gpt-image2` 生成单张故事版总览图 Prompt；
- 为 Seedance 2.0、Kling、Veo、Runway、Sora 等视频模型生成视频 Prompt；
- 把故事版图片 Prompt 和视频 Prompt 统一到同一份 Shot Map；
- 规划 10s / 15s / 30s 多镜头视频；
- 拆分复杂视频为多个可生成 clip；
- 将优秀 Prompt / 分镜案例入库，沉淀成可复用模板；
- 维护个人 AI 视频制作 Prompt 资产库。

---

### 核心能力

#### 1. 自适应模式路由

Skill 会根据用户自然语言自动进入不同模式：

| 用户意图 | Skill 模式 | 输出 |
|---|---|---|
| 设计分镜 | Storyboard Design | 创意摘要、Beat、Shot Map |
| 生成图片故事版 | Storyboard Image Prompt | 中文/英文 gpt-image2 Prompt |
| 生成视频提示词 | Video Prompt | 中文/英文视频 Prompt |
| 从主题到完整方案 | Complete Package | 方案 + 图片 Prompt + 视频 Prompt |
| 收集好案例 | Case Ingestion | 案例卡 + 模板建议 |
| 整理案例库 | Template Maintenance | 模板归类与更新建议 |

#### 2. 一份 Shot Map，多种输出

图片故事版和视频 Prompt 不各写各的，而是同源于一份结构化 Shot Map：

```text
Project Brief
→ Story / Visual Brief
→ Sequence / Beat Layer
→ Shot Map
→ Storyboard Image Prompt Extension
→ Video Prompt Extension
```

#### 3. gpt-image2 故事版图片 Prompt

默认规则：

- 16:9 宽幅影视故事版；
- 中文短标注；
- 动态分镜数量，最多 16 格；
- 可包含顶部 Reference Strip；
- 可包含底部 Technical Reference Bar；
- 强角色 / 主体一致性；
- 避免长段文字和拥挤排版。

#### 4. 视频 Prompt 生成

视频 Prompt 不固定死套 Seedance 格式，而是使用自适应维度系统：

```text
Format：时长 / 镜头数 / 节奏
Subjects：角色 / 主体 / 参考图绑定
Scene：场景 / 空间路线
Action Logic：动作因果
Shot Sequence：镜头序列
Camera Language：景别 / 机位 / 运动
Audio Design：音效 / 对白 / BGM
Mood：情绪
Color Logic：色彩逻辑
Style：视觉风格
Constraints：禁止项
```

#### 5. 动作因果与连续性

适合机械、动作、追逐、产品演示等场景，强调：

```text
可见准备
→ 工具 / 接触 / 操作
→ 可见反应
→ 结果 / payoff
```

同时跟踪角色位置、运动方向、道具状态、受损状态和镜头衔接。

#### 6. 自适应声音设计

Audio Design 是默认检查维度，但不会强行加入对白、旁白或 BGM：

- 动作 / 机械类：重点写 SFX；
- 情绪 / 广告 / 氛围类：可写 BGM、环境声、静默；
- vlog / 口播 / 剧情类：可写对白或旁白；
- 无声视觉片：可明确 `minimal sound / ambient only`。

#### 7. 字幕默认关闭

V1 默认不主动生成字幕、屏幕文字、贴纸 caption。只有用户明确要求时才加入。

---

### 安装方式

> 不同宿主对 Skill 的加载目录可能不同。本仓库保持标准 Skill 包结构：只要宿主支持从一个包含 `SKILL.md` 的目录加载 Skill，就可以使用。

#### 方式 A：作为 Git 仓库使用，推荐用于开发和维护

```bash
git clone git@github.com:twj515895394/storyboard-video-director.git
cd storyboard-video-director
python scripts/validate_skill.py .
```

适合：

- 你要继续维护这个 Skill；
- 你要提交案例、模板、脚本；
- 你要使用 GitHub Actions 自动校验。

#### 方式 B：复制到你的 Agent / Claude Code / 兼容宿主的 Skills 目录

```bash
cp -R storyboard-video-director <YOUR_SKILLS_DIR>/storyboard-video-director
```

要求：

```text
<YOUR_SKILLS_DIR>/storyboard-video-director/SKILL.md
<YOUR_SKILLS_DIR>/storyboard-video-director/references/
<YOUR_SKILLS_DIR>/storyboard-video-director/assets/
<YOUR_SKILLS_DIR>/storyboard-video-director/scripts/
```

注意：`<YOUR_SKILLS_DIR>` 由你的实际宿主决定。不同平台可能叫 workspace skills、global skills、custom skills 或 project skills。

#### 方式 C：打包成 zip 后导入

如果你的宿主支持上传或导入 Skill 压缩包，可以使用：

```bash
python scripts/package_skill.py . --out storyboard-video-director.zip
```

然后在宿主里导入 `storyboard-video-director.zip`。

#### 方式 D：作为项目级 Skill 引用

如果你的 AI Agent 支持项目级 Skill，可以直接把仓库作为项目依赖保留：

```text
project-root/
└── skills/
    └── storyboard-video-director/
        ├── SKILL.md
        ├── references/
        ├── assets/
        └── scripts/
```

---

### 安装后验证

```bash
python scripts/validate_skill.py .
```

期望输出：

```text
OK: storyboard-video-director skill package looks valid.
```

生成样例 Prompt：

```bash
python scripts/compile_prompt.py assets/examples/sample-shot-map.json --mode complete --lang both
```

打包 Skill：

```bash
python scripts/package_skill.py . --out storyboard-video-director.zip
```

---

### 快速使用示例

#### 示例 1：完整 AI 视频前期方案

```text
我想做一个 15 秒 AI 短片：一个小机器人在废弃工厂里发现自己被替换了。帮我从主题到视频 Prompt 完整设计。
```

#### 示例 2：只生成 gpt-image2 故事版图片 Prompt

```text
帮我把这个主题做成一张 16:9 影视故事版图片 Prompt，用于 gpt-image2，默认中文标注。
```

#### 示例 3：只生成视频 Prompt

```text
帮我生成 Seedance 风格的视频提示词，15 秒，动作节奏快，不需要对白，重点写机械音效和动作因果。
```

#### 示例 4：案例入库

```text
把这个优秀视频 Prompt 案例入库，拆解它的结构，并判断是否适合沉淀成模板。
```

---

### 目录结构

```text
storyboard-video-director/
├── SKILL.md
├── README.md
├── .github/workflows/validate.yml
├── references/
│   ├── 00-router.md
│   ├── 01-grill-me-workflow.md
│   ├── 02-brief-shot-map-schema.md
│   ├── 03-storyboard-image-prompt-builder.md
│   ├── 04-video-prompt-builder.md
│   ├── 05-action-causality-continuity.md
│   ├── 06-audio-design-layer.md
│   ├── 07-multi-clip-controller.md
│   ├── 08-case-ingestion-template-library.md
│   └── 09-quality-checklist.md
├── assets/
│   ├── templates/
│   ├── prompt-snippets/
│   ├── examples/
│   └── case-cards/
├── schemas/
├── scripts/
└── docs/
```

---

### 自动化脚本

| 脚本 | 作用 |
|---|---|
| `scripts/validate_skill.py` | 校验 Skill 包结构、frontmatter、核心引用和 schema |
| `scripts/compile_prompt.py` | 从 Shot Map JSON 编译图片 / 视频 Prompt 草案 |
| `scripts/scaffold_case.py` | 从原始案例生成案例卡骨架 |
| `scripts/package_skill.py` | 校验并打包 Skill zip |

---

### 案例库说明

案例库不是必需。没有任何案例时，Skill 会使用内置 SOP 正常工作。

当你看到好案例时，可以触发：

```text
把这个案例入库，拆解它的结构，判断是否适合沉淀成模板。
```

或使用脚本生成案例卡骨架：

```bash
python scripts/scaffold_case.py \
  --raw assets/examples/seedance-sabotage-example.md \
  --name "sabotage action" \
  --family "action-mechanical" \
  --mode video
```

---

### GitHub Actions

仓库已内置 CI：

```text
.github/workflows/validate.yml
```

每次 push / pull request 会执行：

```bash
python scripts/validate_skill.py .
python scripts/compile_prompt.py assets/examples/sample-shot-map.json --mode complete --lang both
python scripts/package_skill.py . --out /tmp/storyboard-video-director.zip
```

---

### 后续路线

- 增加 Seedance / Kling / Veo / Runway / Sora 的模型偏好参考；
- 增加更多真实案例卡；
- 增加从案例卡自动更新模板家族的脚本；
- 增加更严格的 JSON Schema 校验；
- 增加更多 gpt-image2 故事版风格模板；
- 增加更多高质量视频 Prompt 示例。

---

## English Version

### AI Storyboard and Video Shot Director Skill

`storyboard-video-director` is a standard Skill package for **AI video pre-production, cinematic storyboard design, gpt-image2 storyboard image prompts, and Seedance-style or generic video generation prompts**.

It is not a collection of fixed prompts. It is a reusable pre-production workflow:

```text
Short theme
→ Creative direction packages
→ grill-me clarification
→ Story expansion
→ Sequence / Beat design
→ Shot Map
→ gpt-image2 storyboard image prompt
→ Seedance / generic video prompt
→ Optional Multi-Clip splitting
→ Case ingestion / template refinement
```

This repository follows a standard Skill package layout: the repository root is the Skill folder, `SKILL.md` is the entry file, and `references/`, `assets/`, `schemas/`, and `scripts/` provide progressively loaded instructions, templates, examples, and automation scripts.

---

### Use Cases

- Turn a short theme into a cinematic storyboard plan.
- Generate a single storyboard sheet prompt for `gpt-image2`.
- Generate video prompts for Seedance 2.0, Kling, Veo, Runway, Sora, or generic AI video models.
- Keep storyboard image prompts and video prompts aligned through one shared Shot Map.
- Plan 10s / 15s / 30s multi-shot videos.
- Split complex video ideas into multiple generatable clips.
- Ingest strong prompt/storyboard examples into reusable case cards.
- Build a personal AI video prompt asset library.

---

### Core Capabilities

#### 1. Adaptive Mode Routing

| User Intent | Skill Mode | Output |
|---|---|---|
| Design a storyboard | Storyboard Design | Creative summary, Beat, Shot Map |
| Generate storyboard image prompt | Storyboard Image Prompt | Chinese/English gpt-image2 prompt |
| Generate video prompt | Video Prompt | Chinese/English video prompt |
| Build complete pre-production package | Complete Package | Plan + image prompt + video prompt |
| Save a good example | Case Ingestion | Case card + template suggestion |
| Organize cases/templates | Template Maintenance | Template classification and update plan |

#### 2. One Shot Map, Multiple Outputs

Storyboard image prompts and video prompts must derive from the same structured source:

```text
Project Brief
→ Story / Visual Brief
→ Sequence / Beat Layer
→ Shot Map
→ Storyboard Image Prompt Extension
→ Video Prompt Extension
```

#### 3. gpt-image2 Storyboard Image Prompts

Default behavior:

- 16:9 wide cinematic storyboard sheet.
- Short Chinese labels by default.
- Dynamic panel count, maximum 16 panels.
- Optional Reference Strip.
- Optional Technical Reference Bar.
- Strong subject/character consistency.
- Avoid dense text and crowded layouts.

#### 4. Video Prompt Generation

Video prompts are not locked to a rigid Seedance format. They use adaptive prompt dimensions:

```text
Format: duration / shot count / rhythm
Subjects: characters / subjects / reference asset binding
Scene: location / route / spatial logic
Action Logic: visible cause and effect
Shot Sequence: ordered shot list
Camera Language: shot size / angle / movement
Audio Design: SFX / dialogue / BGM when needed
Mood: emotional arc
Color Logic: palette and lighting logic
Style: visual language
Constraints: negative and continuity constraints
```

#### 5. Action Causality and Continuity

For mechanical, action, chase, combat, and product-demo scenes, the Skill emphasizes:

```text
visible setup
→ tool / contact / operation
→ visible reaction
→ payoff
```

It also tracks character position, movement direction, prop state, damage state, geography, and camera continuity.

#### 6. Adaptive Audio Design

Audio is inspected by default, but dialogue, voiceover, and BGM are not forced.

- Action/mechanical scenes: focus on SFX.
- Emotional/ad/mood films: use BGM, ambience, or silence when helpful.
- Vlog/dialogue scenes: use dialogue or voiceover when useful.
- Silent visual films: specify `minimal sound / ambient only`.

#### 7. Subtitles Disabled by Default

V1 does not automatically add subtitles, screen text, or caption stickers. These are included only when explicitly requested.

---

### Installation

> Installation paths vary by host. This repository is a standard Skill folder: any compatible host that can load a directory containing `SKILL.md` should be able to use it.

#### Option A: Use as a Git repository, recommended for development

```bash
git clone git@github.com:twj515895394/storyboard-video-director.git
cd storyboard-video-director
python scripts/validate_skill.py .
```

Best for:

- maintaining the Skill;
- adding cases/templates/scripts;
- using GitHub Actions validation.

#### Option B: Copy into your Agent / Claude Code / compatible host Skills directory

```bash
cp -R storyboard-video-director <YOUR_SKILLS_DIR>/storyboard-video-director
```

Expected layout:

```text
<YOUR_SKILLS_DIR>/storyboard-video-director/SKILL.md
<YOUR_SKILLS_DIR>/storyboard-video-director/references/
<YOUR_SKILLS_DIR>/storyboard-video-director/assets/
<YOUR_SKILLS_DIR>/storyboard-video-director/scripts/
```

`<YOUR_SKILLS_DIR>` depends on your actual host. It may be called workspace skills, global skills, custom skills, or project skills.

#### Option C: Package as a zip for import

If your host supports importing a Skill archive:

```bash
python scripts/package_skill.py . --out storyboard-video-director.zip
```

Then import `storyboard-video-director.zip` in your host.

#### Option D: Use as a project-level Skill

For agents that support project-level Skills:

```text
project-root/
└── skills/
    └── storyboard-video-director/
        ├── SKILL.md
        ├── references/
        ├── assets/
        └── scripts/
```

---

### Verify Installation

```bash
python scripts/validate_skill.py .
```

Expected output:

```text
OK: storyboard-video-director skill package looks valid.
```

Compile a sample prompt:

```bash
python scripts/compile_prompt.py assets/examples/sample-shot-map.json --mode complete --lang both
```

Package the Skill:

```bash
python scripts/package_skill.py . --out storyboard-video-director.zip
```

---

### Quick Usage Examples

#### Example 1: Complete AI video pre-production package

```text
I want to make a 15-second AI short film: a small robot discovers it has been replaced inside an abandoned factory. Design the full pre-production package from theme to video prompt.
```

#### Example 2: gpt-image2 storyboard image prompt only

```text
Turn this theme into a 16:9 cinematic storyboard image prompt for gpt-image2, with Chinese labels by default.
```

#### Example 3: Video prompt only

```text
Generate a Seedance-style 15-second video prompt. Keep the action fast, no dialogue, focus on mechanical SFX and clear action causality.
```

#### Example 4: Case ingestion

```text
Ingest this strong video prompt example, deconstruct its structure, and decide whether it should become a reusable template.
```

---

### Repository Structure

```text
storyboard-video-director/
├── SKILL.md
├── README.md
├── .github/workflows/validate.yml
├── references/
├── assets/
├── schemas/
├── scripts/
└── docs/
```

---

### Automation Scripts

| Script | Purpose |
|---|---|
| `scripts/validate_skill.py` | Validate Skill structure, frontmatter, references, and schemas |
| `scripts/compile_prompt.py` | Compile draft image/video prompts from a Shot Map JSON |
| `scripts/scaffold_case.py` | Generate a case-card scaffold from a raw example |
| `scripts/package_skill.py` | Validate and package the Skill as a zip |

---

### Case Library

The case library is optional. The Skill works with built-in SOP rules even when no custom case cards exist.

To scaffold a case card:

```bash
python scripts/scaffold_case.py \
  --raw assets/examples/seedance-sabotage-example.md \
  --name "sabotage action" \
  --family "action-mechanical" \
  --mode video
```

---

### GitHub Actions

The repository includes CI validation:

```text
.github/workflows/validate.yml
```

On push / pull request it runs:

```bash
python scripts/validate_skill.py .
python scripts/compile_prompt.py assets/examples/sample-shot-map.json --mode complete --lang both
python scripts/package_skill.py . --out /tmp/storyboard-video-director.zip
```

---

### Roadmap

- Add model preference references for Seedance, Kling, Veo, Runway, and Sora.
- Add more real-world case cards.
- Add a script for updating template families from case cards.
- Add stricter JSON Schema validation.
- Add more gpt-image2 storyboard style templates.
- Add more high-quality AI video prompt examples.
