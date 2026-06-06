# 💪 AI Fitness

AI健身工具，支持训练计划、动作指导、进度追踪。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏋️ 训练计划生成
- 📖 动作详细解释
- 📈 进度追踪模板
- 🧘 恢复方案建议
- 📊 宏量营养素计算

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_fitness import create_tools

tools = create_tools()

# 训练计划
workout = tools.generate_workout("增肌", "intermediate", 60, ["哑铃", "杠铃"])

# 动作解释
exercise = tools.explain_exercise("深蹲")

# 进度追踪
tracker = tools.create_progress_tracker(["深蹲", "卧推", "硬拉"])

# 恢复方案
recovery = tools.suggest_recovery(["大腿", "胸部"])

# 宏量营养素
macros = tools.calculate_macros(75, "减脂", "中等")
```

## 📁 项目结构

```
ai-fitness/
├── tools.py       # 健身工具核心
└── README.md
```

## 📄 许可证

MIT License
