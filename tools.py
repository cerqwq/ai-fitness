"""
AI Fitness - AI健身工具
支持训练计划、动作指导、进度追踪
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIFitnessTools:
    """
    AI健身工具
    支持：训练、指导、追踪
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_workout(self, goal: str, level: str, duration: int, equipment: List[str]) -> Dict:
        """生成训练计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        equipment_text = ", ".join(equipment)

        prompt = f"""请生成训练计划：

目标：{goal}
水平：{level}
时长：{duration}分钟
设备：{equipment_text}

请返回JSON格式：
{{
    "warm_up": [{{"exercise": "动作", "duration": "时长"}}],
    "main_workout": [{{"exercise": "动作", "sets": 组数, "reps": "次数", "rest": "休息"}}],
    "cool_down": [{{"exercise": "动作", "duration": "时长"}}],
    "estimated_calories": "预估消耗"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"workout": content}

    def explain_exercise(self, exercise: str) -> Dict:
        """解释动作"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请详细解释{exercise}动作：

请返回JSON格式：
{{
    "name": "动作名",
    "target_muscles": ["目标肌群"],
    "equipment": "所需设备",
    "steps": ["步骤1", "步骤2"],
    "common_mistakes": ["常见错误"],
    "variations": ["变体"],
    "tips": ["技巧"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"exercise": content}

    def create_progress_tracker(self, exercises: List[str]) -> Dict:
        """创建进度追踪"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        exercises_text = ", ".join(exercises)

        prompt = f"""请为以下动作创建进度追踪模板：

动作：{exercises_text}

请返回JSON格式：
{{
    "exercises": [
        {{"name": "动作", "tracking_metrics": ["指标"], "initial_benchmark": "初始基准", "goals": ["目标"]}}
    ],
    "frequency": "记录频率",
    "milestones": ["里程碑"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"tracker": content}

    def suggest_recovery(self, muscle_soreness: List[str]) -> Dict:
        """建议恢复方案"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        soreness_text = ", ".join(muscle_soreness)

        prompt = f"""请为以下肌肉酸痛提供恢复方案：

酸痛部位：{soreness_text}

请返回JSON格式：
{{
    "stretching": ["拉伸动作"],
    "foam_rolling": ["泡沫轴动作"],
    "nutrition": ["营养建议"],
    "rest": "休息建议",
    "timeline": "恢复时间线"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"recovery": content}

    def calculate_macros(self, weight: float, goal: str, activity_level: str) -> Dict:
        """计算宏量营养素"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请计算宏量营养素需求：

体重：{weight}kg
目标：{goal}
活动水平：{activity_level}

请返回JSON格式：
{{
    "daily_calories": "每日卡路里",
    "protein": "蛋白质(克)",
    "carbs": "碳水化合物(克)",
    "fat": "脂肪(克)",
    "meal_timing": "进餐建议"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"macros": content}


def create_tools(**kwargs) -> AIFitnessTools:
    """创建健身工具"""
    return AIFitnessTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Fitness Tools")
    print()

    # 测试
    workout = tools.generate_workout("增肌", "intermediate", 60, ["哑铃", "杠铃"])
    print(json.dumps(workout, ensure_ascii=False, indent=2))
