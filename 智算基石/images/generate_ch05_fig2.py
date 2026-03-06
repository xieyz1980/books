#!/usr/bin/env python3
"""
第5章 智算中心架构插图
图2: NVIDIA DGX SuperPOD架构图
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
fig, ax = plt.subplots(1, 1, figsize=(12, 10), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 配色
colors = {
    'dgx': '#76B900',           # NVIDIA绿色
    'nvlink': '#00A8E8',        # NVLink蓝
    'infiniband': '#FF6B35',    # InfiniBand橙
    'storage': '#9B59B6',       # 存储紫
    'mgmt': '#34495E',          # 管理灰
    'bg': '#F8F9FA',
}

# 标题
ax.text(50, 98, 'NVIDIA DGX SuperPOD Architecture', 
        fontsize=18, fontweight='bold', ha='center', va='top', color='#1A1A1A')
ax.text(50, 94, 'DGX SuperPOD 架构图 (H100/H200 Generation)', 
        fontsize=12, ha='center', va='top', color='#666666')

# ===== DGX BasePOD 单元 =====
# 每个SU (Scalable Unit) = 32 DGX nodes
ax.text(50, 90, 'Scalable Unit (SU) - 32 DGX Nodes', 
        fontsize=11, fontweight='bold', ha='center', color=colors['dgx'])

# 绘制DGX节点网格 (8x4)
node_positions = []
for row in range(4):
    for col in range(8):
        x = 10 + col * 10
        y = 65 - row * 8
        node_positions.append((x, y))
        
        # DGX节点
        dgx = FancyBboxPatch((x-3.5, y-3), 7, 6, 
                             boxstyle="round,pad=0.02,rounding_size=0.5",
                             facecolor=colors['dgx'], edgecolor='white', linewidth=1.5)
        ax.add_patch(dgx)
        ax.text(x, y, f'DGX\n{row*8+col+1}', fontsize=6, ha='center', va='center', 
                color='white', fontweight='bold')
        
        # 内部GPU示意
        for i in range(4):
            small_rect = Rectangle((x-3+i*1.5, y-2.5), 1.2, 1, 
                                   facecolor='white', alpha=0.3)
            ax.add_patch(small_rect)

# SU边框
su_border = FancyBboxPatch((5, 35), 90, 55, boxstyle="round,pad=0.02,rounding_size=1",
                           facecolor='none', edgecolor=colors['dgx'], linewidth=3, linestyle='--')
ax.add_patch(su_border)

# ===== NVSwitch 网络层 =====
ax.text(50, 31, 'NVSwitch Network (In-Node & Inter-Node)', 
        fontsize=10, fontweight='bold', ha='center', color=colors['nvlink'])

# NVSwitch盒子
nvsw_box = FancyBboxPatch((8, 22), 84, 7, boxstyle="round,pad=0.02,rounding_size=0.5",
                          facecolor='#E8F8FF', edgecolor=colors['nvlink'], linewidth=2)
ax.add_patch(nvsw_box)

# NVSwitch图标
for i, x in enumerate([18, 38, 58, 78]):
    circle = Circle((x, 25.5), 3, facecolor=colors['nvlink'], edgecolor='white', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, 25.5, f'NVSwitch\nLayer {i+1}', fontsize=6, ha='center', va='center', color='white')

# ===== InfiniBand 网络层 =====
ax.text(50, 19, 'InfiniBand NDR Network (400G/800G)', 
        fontsize=10, fontweight='bold', ha='center', color=colors['infiniband'])

ib_box = FancyBboxPatch((8, 10), 84, 7, boxstyle="round,pad=0.02,rounding_size=0.5",
                        facecolor='#FFF5F0', edgecolor=colors['infiniband'], linewidth=2)
ax.add_patch(ib_box)

# Spine-Leaf交换机
switches = [
    ('Leaf\nSwitch', 20, 13.5),
    ('Leaf\nSwitch', 40, 13.5),
    ('Leaf\nSwitch', 60, 13.5),
    ('Leaf\nSwitch', 80, 13.5),
    ('Spine\nSwitch', 30, 13.5),
    ('Spine\nSwitch', 70, 13.5),
]
for name, x, y in switches:
    sw = FancyBboxPatch((x-5, y-2.5), 10, 5, boxstyle="round,pad=0.01,rounding_size=0.3",
                        facecolor=colors['infiniband'], edgecolor='white', linewidth=1.5)
    ax.add_patch(sw)
    ax.text(x, y, name, fontsize=6, ha='center', va='center', color='white', fontweight='bold')

# ===== 存储和管理层 =====
storage_box = FancyBboxPatch((5, 2), 42, 6, boxstyle="round,pad=0.02,rounding_size=0.5",
                             facecolor='#F3E5F5', edgecolor=colors['storage'], linewidth=2)
ax.add_patch(storage_box)
ax.text(26, 6.5, 'DAS / Parallel Storage', fontsize=9, fontweight='bold', ha='center', color=colors['storage'])
ax.text(26, 3.5, 'GPUDirect Storage | NVMe-oF', fontsize=7, ha='center', color='#7B1FA2')

mgmt_box = FancyBboxPatch((53, 2), 42, 6, boxstyle="round,pad=0.02,rounding_size=0.5",
                          facecolor='#ECEFF1', edgecolor=colors['mgmt'], linewidth=2)
ax.add_patch(mgmt_box)
ax.text(74, 6.5, 'Management & Software', fontsize=9, fontweight='bold', ha='center', color=colors['mgmt'])
ax.text(74, 3.5, 'Baseboard Mgmt | SLURM | Kubernetes', fontsize=7, ha='center', color='#455A64')

# ===== 规格信息 =====
specs = [
    'SU Specs: 32 DGX H100/H200 | 256 GPUs | 640 CPU Cores | 20 TB System Memory',
    'GPU Memory: 256 × 80GB/96GB HBM3 = 20.5/24.6 TB',
    'AI Performance: ~1 EFLOPS FP8 (Sparse) per SU',
    'Network: NVLink 4.0 (900GB/s) + InfiniBand NDR (400G/800G)',
]
for i, spec in enumerate(specs):
    ax.text(50, -2-i*2.5, spec, fontsize=8, ha='center', color='#555555', style='italic')

# 图例
legend_elements = [
    mpatches.Patch(facecolor=colors['dgx'], label='DGX System (8× H100/H200 GPU)'),
    mpatches.Patch(facecolor=colors['nvlink'], label='NVSwitch Network'),
    mpatches.Patch(facecolor=colors['infiniband'], label='InfiniBand NDR'),
    mpatches.Patch(facecolor=colors['storage'], label='Storage'),
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.02, 0.85), 
          fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig('/workspace/projects/books/智算基石/images/ch05-dgx-superpod.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Generated: ch05-dgx-superpod.png")
