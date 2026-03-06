#!/usr/bin/env python3
"""
第5章 智算中心架构插图
图3: 阿里云飞天智算平台架构图
300dpi, 印刷级质量
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'WenQuanYi Micro Hei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(1, 1, figsize=(12, 11), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 阿里云配色
colors = {
    'primary': '#FF6A00',       # 阿里橙
    'secondary': '#00C1DE',     # 阿里蓝
    'accent': '#1677FF',        # 深蓝
    'green': '#52C41A',
    'purple': '#722ED1',
    'red': '#F5222D',
    'bg': '#FFF7E6',
}

# 标题
ax.text(50, 98, 'Alibaba Cloud Feitian AI Computing Platform', 
        fontsize=18, fontweight='bold', ha='center', va='top', color=colors['primary'])
ax.text(50, 94, '阿里云飞天智算平台架构', 
        fontsize=14, ha='center', va='top', color='#666666')

# ===== 应用层 (最上层) =====
app_box = FancyBboxPatch((3, 82), 94, 10, boxstyle="round,pad=0.02,rounding_size=1",
                         facecolor='#FFF2E8', edgecolor=colors['primary'], linewidth=2)
ax.add_patch(app_box)
ax.text(50, 89, 'AI Applications / 人工智能应用层', fontsize=12, fontweight='bold', 
        ha='center', va='center', color=colors['primary'])

apps = ['LLM Training\n大模型训练', 'AIGC\n生成式AI', 'Scientific\nComputing\n科学计算', 
        'Autonomous\nDriving\n自动驾驶', 'Drug\nDiscovery\n药物研发', 'Financial\nModeling\n金融建模']
for i, app in enumerate(apps):
    x = 12 + i * 15
    box = FancyBboxPatch((x-6, 83), 12, 6, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor='white', edgecolor=colors['primary'], linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, 86, app, fontsize=7, ha='center', va='center', color=colors['primary'])

# ===== 平台层 =====
platform_box = FancyBboxPatch((3, 62), 94, 18, boxstyle="round,pad=0.02,rounding_size=1",
                              facecolor='#E6F7FF', edgecolor=colors['secondary'], linewidth=2)
ax.add_patch(platform_box)
ax.text(50, 77, 'PAI Platform / 人工智能平台', fontsize=12, fontweight='bold', 
        ha='center', va='center', color=colors['secondary'])

# 平台子模块
platform_modules = [
    ('PAI-DSW\n交互式建模', 12, 70),
    ('PAI-DLC\n深度学习训练', 30, 70),
    ('PAI-EAS\n模型推理服务', 48, 70),
    ('PAI-Blade\n推理加速', 66, 70),
    ('PAI-Designer\n可视化建模', 84, 70),
    ('PAI-LLM\n大模型训练', 21, 64),
    ('PAI-QuickStart\n快速开始', 43, 64),
    ('PAI-FeatureStore\n特征平台', 65, 64),
    ('PAI-Rec\n推荐引擎', 84, 64),
]
for name, x, y in platform_modules:
    box = FancyBboxPatch((x-8, y-2.5), 16, 5, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor='white', edgecolor=colors['secondary'], linewidth=1)
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=7, ha='center', va='center', color=colors['secondary'])

# ===== 灵骏智算层 =====
lingjun_box = FancyBboxPatch((3, 38), 94, 22, boxstyle="round,pad=0.02,rounding_size=1",
                             facecolor='#F6FFED', edgecolor=colors['green'], linewidth=2)
ax.add_patch(lingjun_box)
ax.text(50, 57, 'Lingjun AI Computing / 灵骏智算集群', fontsize=12, fontweight='bold', 
        ha='center', va='center', color=colors['green'])

# 灵骏集群硬件
clusters = [
    ('GPU Cluster\nGPU集群\n(A100/H100)', 18, 50, colors['accent']),
    ('NPU Cluster\nNPU集群\n(含光800)', 40, 50, colors['purple']),
    ('CPU Cluster\nCPU集群\n(倚天710)', 62, 50, '#13C2C2'),
    ('Heterogeneous\n异构计算池', 84, 50, colors['red']),
]

for title, x, y, c in clusters:
    box = FancyBboxPatch((x-9, y-6), 18, 12, boxstyle="round,pad=0.01,rounding_size=0.5",
                         facecolor=c, edgecolor='white', linewidth=2, alpha=0.85)
    ax.add_patch(box)
    ax.text(x, y+2, title, fontsize=8, fontweight='bold', ha='center', va='center', color='white')

# 网络
ax.text(50, 41, 'High-Speed Interconnect: RDMA (100G/200G) | VPC | InfiniBand', 
        fontsize=8, ha='center', va='center', color=colors['green'], style='italic')

# ===== 基础设施层 =====
infra_box = FancyBboxPatch((3, 15), 94, 21, boxstyle="round,pad=0.02,rounding_size=1",
                           facecolor='#F9F0FF', edgecolor=colors['purple'], linewidth=2)
ax.add_patch(infra_box)
ax.text(50, 33, 'Infrastructure / 基础设施层', fontsize=12, fontweight='bold', 
        ha='center', va='center', color=colors['purple'])

# 基础设施模块
infra_items = [
    ('Compute\n计算', 'ECS\nBare Metal\nGPU/NPU', 15, 26),
    ('Storage\n存储', 'OSS\nNAS\nCPFS', 35, 26),
    ('Network\n网络', 'VPC\nSLB\nCDN', 55, 26),
    ('Security\n安全', 'WAF\nKMS\nRAM', 75, 26),
    ('Container\n容器', 'ACK\nASK\nK8s', 90, 26),
]

for title, content, x, y in infra_items:
    box = FancyBboxPatch((x-8, y-6), 16, 12, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor='white', edgecolor=colors['purple'], linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, y+2.5, title, fontsize=8, fontweight='bold', ha='center', va='center', color=colors['purple'])
    ax.text(x, y-2.5, content, fontsize=6, ha='center', va='center', color='#531dab')

# 底部存储规格
storage_tiers = [
    ('CPFS\n高性能并行存储', 15, 18),
    ('OSS\n对象存储', 38, 18),
    ('NAS\n文件存储', 61, 18),
    ('EBS\n块存储', 84, 18),
]
for name, x, y in storage_tiers:
    box = FancyBboxPatch((x-9, y-2), 18, 4, boxstyle="round,pad=0.01,rounding_size=0.2",
                         facecolor='#E6FFFB', edgecolor='#13C2C2', linewidth=1)
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=7, ha='center', va='center', color='#006D75')

# ===== 数据中心层 =====
dc_box = FancyBboxPatch((3, 3), 94, 10, boxstyle="round,pad=0.02,rounding_size=1",
                        facecolor='#FFF1F0', edgecolor=colors['red'], linewidth=2)
ax.add_patch(dc_box)
ax.text(50, 10, 'Data Centers / 数据中心基础设施', fontsize=11, fontweight='bold', 
        ha='center', va='center', color=colors['red'])

dc_items = ['张北数据中心', '乌兰察布数据中心', '河源数据中心', '南通数据中心', '成都数据中心']
for i, dc in enumerate(dc_items):
    x = 12 + i * 18
    box = FancyBboxPatch((x-7, 4), 14, 4, boxstyle="round,pad=0.01,rounding_size=0.2",
                         facecolor='white', edgecolor=colors['red'], linewidth=1)
    ax.add_patch(box)
    ax.text(x, 6, dc, fontsize=7, ha='center', va='center', color=colors['red'])

# 连接线装饰
ax.annotate('', xy=(50, 82), xytext=(50, 80), arrowprops=dict(arrowstyle='<->', color='#999', lw=1.5))
ax.annotate('', xy=(50, 62), xytext=(50, 60), arrowprops=dict(arrowstyle='<->', color='#999', lw=1.5))
ax.annotate('', xy=(50, 38), xytext=(50, 36), arrowprops=dict(arrowstyle='<->', color='#999', lw=1.5))
ax.annotate('', xy=(50, 15), xytext=(50, 13), arrowprops=dict(arrowstyle='<->', color='#999', lw=1.5))

# 图例
legend_elements = [
    mpatches.Patch(facecolor=colors['primary'], label='Application Layer'),
    mpatches.Patch(facecolor=colors['secondary'], label='PAI Platform'),
    mpatches.Patch(facecolor=colors['green'], label='Lingjun AI Computing'),
    mpatches.Patch(facecolor=colors['purple'], label='Infrastructure'),
    mpatches.Patch(facecolor=colors['red'], label='Data Center'),
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.01, 0.75), 
          fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('/workspace/projects/books/智算基石/images/ch05-aliyun-feitian.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Generated: ch05-aliyun-feitian.png")
