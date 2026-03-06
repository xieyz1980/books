#!/usr/bin/env python3
"""
第5章 智算中心架构插图
图4: 智算中心机柜布局图
300dpi, 印刷级质量
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'WenQuanYi Micro Hei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
fig, ax = plt.subplots(1, 1, figsize=(13, 9), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 配色
colors = {
    'gpu': '#1E40AF',           # GPU机柜 - 深蓝
    'cpu': '#059669',           # CPU机柜 - 绿
    'storage': '#B45309',       # 存储机柜 - 琥珀
    'network': '#7C3AED',       # 网络机柜 - 紫
    'power': '#DC2626',         # 配电 - 红
    'cooling': '#0891B2',       # 冷却 - 青
    'mgmt': '#4B5563',          # 管理 - 灰
    'red': '#DC2626',
}

# 标题
ax.text(50, 97, 'Intelligent Computing Center - Rack Layout', 
        fontsize=18, fontweight='bold', ha='center', va='top', color='#1F2937')
ax.text(50, 93, '智算中心机柜布局平面图 (示例: 1000个机柜规模)', 
        fontsize=12, ha='center', va='top', color='#6B7280')

# 数据中心边界
outer_border = FancyBboxPatch((3, 3), 94, 87, boxstyle="round,pad=0.02,rounding_size=1",
                              facecolor='#F9FAFB', edgecolor='#374151', linewidth=2)
ax.add_patch(outer_border)

# 机房区域标记
room_labels = [
    ('机房A\nGPU Computing', 10, 88, 35, 3),
    ('机房B\nGPU Computing', 47, 88, 35, 3),
    ('机房C\nStorage & Network', 10, 55, 35, 3),
    ('机房D\nInfrastructure', 47, 55, 35, 3),
]
for label, x, y, w, h in room_labels:
    room = FancyBboxPatch((x, y-h), w, h, boxstyle="round,pad=0.01,rounding_size=0.3",
                          facecolor='#E5E7EB', edgecolor='#9CA3AF', linewidth=1)
    ax.add_patch(room)
    ax.text(x+w/2, y-h/2, label, fontsize=8, ha='center', va='center', color='#4B5563')

# ===== 机房A: GPU计算机柜 =====
# 绘制机柜网格 (10列 x 6行)
gpu_cabinets = []
for row in range(6):
    for col in range(10):
        x = 11 + col * 3.2
        y = 82 - row * 4
        gpu_cabinets.append((x, y))
        
        # GPU机柜
        rack = Rectangle((x, y-3), 2.5, 3, facecolor=colors['gpu'], 
                         edgecolor='white', linewidth=0.5)
        ax.add_patch(rack)
        
        # 机柜编号
        rack_id = f'G{row*10+col+1:02d}'
        ax.text(x+1.25, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
                color='white', fontweight='bold')

# 机房A标签
ax.text(28, 85, 'GPU Computing Room A (60 Racks)', fontsize=9, fontweight='bold', 
        ha='center', color=colors['gpu'])

# ===== 机房B: GPU计算机柜 =====
for row in range(6):
    for col in range(10):
        x = 48 + col * 3.2
        y = 82 - row * 4
        
        rack = Rectangle((x, y-3), 2.5, 3, facecolor=colors['gpu'], 
                         edgecolor='white', linewidth=0.5)
        ax.add_patch(rack)
        
        rack_id = f'G{60+row*10+col+1:02d}'
        ax.text(x+1.25, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
                color='white', fontweight='bold')

ax.text(65, 85, 'GPU Computing Room B (60 Racks)', fontsize=9, fontweight='bold', 
        ha='center', color=colors['gpu'])

# ===== 机房C: 存储和网络机柜 =====
# 存储机柜
for row in range(4):
    for col in range(6):
        x = 11 + col * 4.5
        y = 50 - row * 4
        
        rack = Rectangle((x, y-3), 3.5, 3, facecolor=colors['storage'], 
                         edgecolor='white', linewidth=0.5)
        ax.add_patch(rack)
        
        rack_id = f'S{row*6+col+1:02d}'
        ax.text(x+1.75, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
                color='white', fontweight='bold')

# 网络机柜
for row in range(4):
    for col in range(3):
        x = 38 + col * 3
        y = 50 - row * 4
        
        rack = Rectangle((x, y-3), 2.5, 3, facecolor=colors['network'], 
                         edgecolor='white', linewidth=0.5)
        ax.add_patch(rack)
        
        rack_id = f'N{row*3+col+1:02d}'
        ax.text(x+1.25, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
                color='white', fontweight='bold')

ax.text(28, 53, 'Storage (24) + Network (12)', fontsize=9, fontweight='bold', 
        ha='center', color=colors['storage'])

# ===== 机房D: 基础设施机柜 =====
# CPU机柜
for row in range(3):
    for col in range(5):
        x = 48 + col * 4
        y = 50 - row * 4
        
        rack = Rectangle((x, y-3), 3.5, 3, facecolor=colors['cpu'], 
                         edgecolor='white', linewidth=0.5)
        ax.add_patch(rack)
        
        rack_id = f'C{row*5+col+1:02d}'
        ax.text(x+1.75, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
                color='white', fontweight='bold')

# 管理机柜
for col in range(3):
    x = 70 + col * 3
    y = 50
    
    rack = Rectangle((x, y-3), 2.5, 3, facecolor=colors['mgmt'], 
                     edgecolor='white', linewidth=0.5)
    ax.add_patch(rack)
    
    rack_id = f'M{col+1:02d}'
    ax.text(x+1.25, y-1.5, rack_id, fontsize=4, ha='center', va='center', 
            color='white', fontweight='bold')

ax.text(65, 53, 'CPU (15) + Mgmt (3) + Power/Cooling', fontsize=9, fontweight='bold', 
        ha='center', color=colors['cpu'])

# ===== 配电和冷却区域 =====
power_box = FancyBboxPatch((48, 28), 34, 15, boxstyle="round,pad=0.02,rounding_size=0.5",
                           facecolor='#FEE2E2', edgecolor=colors['power'], linewidth=2)
ax.add_patch(power_box)
ax.text(65, 40, 'Power Distribution', fontsize=10, fontweight='bold', 
        ha='center', color=colors['power'])
ax.text(65, 36, 'UPS Systems | HV/MV Transformers', fontsize=8, ha='center', color='#991B1B')
ax.text(65, 32, '2N Redundancy | 150MW Total Capacity', fontsize=8, ha='center', color='#991B1B')

# 冷却区域
cooling_box = FancyBboxPatch((8, 28), 38, 15, boxstyle="round,pad=0.02,rounding_size=0.5",
                             facecolor='#CFFAFE', edgecolor=colors['cooling'], linewidth=2)
ax.add_patch(cooling_box)
ax.text(27, 40, 'Cooling Infrastructure', fontsize=10, fontweight='bold', 
        ha='center', color=colors['cooling'])
ax.text(27, 36, 'Chillers | Cooling Towers | CRAH Units', fontsize=8, ha='center', color='#0E7490')
ax.text(27, 32, 'Liquid Cooling Ready | PUE < 1.2', fontsize=8, ha='center', color='#0E7490')

# ===== 入口和通道 =====
# 主通道
main_aisle = Rectangle((5, 15), 90, 6, facecolor='#E5E7EB', edgecolor='#9CA3AF', linewidth=1)
ax.add_patch(main_aisle)
ax.text(50, 18, 'Main Corridor / 主通道 (3m width)', fontsize=9, ha='center', va='center', color='#4B5563')

# 入口
entrance = Rectangle((42, 6), 16, 6, facecolor='#10B981', edgecolor='#059669', linewidth=2)
ax.add_patch(entrance)
ax.text(50, 9, 'MAIN ENTRANCE / 主入口', fontsize=10, fontweight='bold', 
        ha='center', va='center', color='white')

# 消防通道
ax.text(8, 22, 'Emergency Exit', fontsize=7, ha='center', color=colors['red'])
ax.text(92, 22, 'Emergency Exit', fontsize=7, ha='center', color=colors['red'])

# ===== 图例 =====
legend_items = [
    (colors['gpu'], 'GPU Rack (DGX/HGX) - 120 units'),
    (colors['storage'], 'Storage Rack - 24 units'),
    (colors['network'], 'Network Rack - 12 units'),
    (colors['cpu'], 'CPU Rack - 15 units'),
    (colors['mgmt'], 'Management Rack - 3 units'),
    (colors['power'], 'Power Distribution'),
    (colors['cooling'], 'Cooling Infrastructure'),
]

legend_y = 12
for i, (color, label) in enumerate(legend_items):
    x = 8 + (i % 4) * 24
    y = legend_y if i < 4 else legend_y - 5
    rect = Rectangle((x, y-1.5), 3, 2, facecolor=color, edgecolor='white', linewidth=1)
    ax.add_patch(rect)
    ax.text(x+4, y-0.5, label, fontsize=7, va='center', color='#374151')

# 规格说明
specs_text = [
    'Layout Specifications:',
    '• Total Floor Area: ~3,000 m² | Rack Count: ~174 | Power Density: 15-30kW per GPU rack',
    '• Cooling: Room + Row + Rack-level liquid cooling | Fire Suppression: FM-200 / Novec 1230',
    '• Standards: Tier III+ / Uptime Institute | GB 50174-2017 A级',
]
for i, text in enumerate(specs_text):
    ax.text(50, -3-i*2, text, fontsize=8, ha='center', color='#6B7280', 
            fontweight='bold' if i == 0 else 'normal')

plt.tight_layout()
plt.savefig('/workspace/projects/books/智算基石/images/ch05-rack-layout.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Generated: ch05-rack-layout.png")
