#!/usr/bin/env python3
"""
第5章 智算中心架构插图
图1: 智算中心整体架构图（计算/网络/存储/管理分层）
300dpi, 印刷级质量
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'WenQuanYi Micro Hei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布 - A4横向, 300dpi
fig, ax = plt.subplots(1, 1, figsize=(11.69, 8.27), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 配色方案 - 专业科技风格
colors = {
    'compute': '#1E3A8A',      # 深蓝 - 计算层
    'network': '#047857',       # 翠绿 - 网络层  
    'storage': '#B45309',       # 琥珀 - 存储层
    'mgmt': '#7C3AED',          # 紫罗兰 - 管理层
    'bg_light': '#F8FAFC',      # 浅灰背景
    'border': '#334155',        # 边框色
    'text': '#1E293B',          # 深色文字
    'accent': '#0EA5E9',        # 强调色
}

# 绘制标题
ax.text(50, 96, 'Intelligent Computing Center Architecture', 
        fontsize=20, fontweight='bold', ha='center', va='top', color=colors['text'])
ax.text(50, 91, '智算中心整体架构图', 
        fontsize=14, ha='center', va='top', color='#64748B')

# ===== 第四层：管理层 (顶部) =====
mgmt_box = FancyBboxPatch((5, 75), 90, 12, boxstyle="round,pad=0.02,rounding_size=1",
                           facecolor='#EDE9FE', edgecolor=colors['mgmt'], linewidth=2)
ax.add_patch(mgmt_box)
ax.text(50, 84, 'Management Layer / 管理层', fontsize=13, fontweight='bold', 
        ha='center', va='center', color=colors['mgmt'])

# 管理层子模块
mgmt_modules = [
    ('Resource\nScheduler', 12),
    ('Monitoring\n& Alert', 28),
    ('Workload\nManager', 44),
    ('Security\nCenter', 60),
    ('DevOps\nPlatform', 76),
    ('Billing\nSystem', 88)
]
for name, x in mgmt_modules:
    box = FancyBboxPatch((x-6, 76), 12, 6, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor='white', edgecolor=colors['mgmt'], linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, 79, name, fontsize=7, ha='center', va='center', color=colors['text'])

# ===== 第三层：网络层 =====
net_box = FancyBboxPatch((5, 55), 90, 18, boxstyle="round,pad=0.02,rounding_size=1",
                          facecolor='#D1FAE5', edgecolor=colors['network'], linewidth=2)
ax.add_patch(net_box)
ax.text(50, 70, 'Network Layer / 网络层', fontsize=13, fontweight='bold', 
        ha='center', va='center', color=colors['network'])

# 网络子系统
net_items = [
    ('High-Speed\nInterconnect\n(InfiniBand/NVLink)', 18, 62),
    ('Spine-Leaf\nFabric', 40, 62),
    ('Load\nBalancer', 58, 62),
    ('Security\nGateway', 76, 62),
]
for name, x, y in net_items:
    box = FancyBboxPatch((x-8, y-4), 16, 9, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor='white', edgecolor=colors['network'], linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, y+0.5, name, fontsize=7, ha='center', va='center', color=colors['text'])

# 网络速度标识
speeds = ['400G/800G', '200G/400G', '100G', '25G/100G']
speed_x = [18, 40, 58, 76]
for s, x in zip(speeds, speed_x):
    ax.text(x, 57, s, fontsize=6, ha='center', va='center', color=colors['network'], fontweight='bold')

# ===== 第二层：计算层 =====
compute_box = FancyBboxPatch((5, 28), 90, 25, boxstyle="round,pad=0.02,rounding_size=1",
                              facecolor='#DBEAFE', edgecolor=colors['compute'], linewidth=2)
ax.add_patch(compute_box)
ax.text(50, 50, 'Compute Layer / 计算层', fontsize=13, fontweight='bold', 
        ha='center', va='center', color=colors['compute'])

# GPU集群
clusters = [
    ('AI Training\nCluster', 'H100/H800\n× 1024 GPUs', 15, 40, '#1E40AF'),
    ('Inference\nCluster', 'A100/A10\n× 2048 GPUs', 35, 40, '#2563EB'),
    ('HPC\nCluster', 'CPU+GPU\nHybrid', 55, 40, '#3B82F6'),
    ('Edge\nNodes', 'Lightweight\nInference', 75, 40, '#60A5FA'),
]

for title, spec, x, y, c in clusters:
    # 外框
    box = FancyBboxPatch((x-8, y-8), 16, 16, boxstyle="round,pad=0.01,rounding_size=0.5",
                         facecolor=c, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y+3, title, fontsize=8, fontweight='bold', ha='center', va='center', color='white')
    ax.text(x, y-3, spec, fontsize=6, ha='center', va='center', color='#E0F2FE')

# 计算层底部说明
ax.text(50, 30, 'GPU Interconnect: NVLink 4.0 | NVSwitch | PCIe Gen5', 
        fontsize=8, ha='center', va='center', color=colors['compute'], style='italic')

# ===== 第一层：存储层 (底部) =====
storage_box = FancyBboxPatch((5, 5), 90, 21, boxstyle="round,pad=0.02,rounding_size=1",
                              facecolor='#FEF3C7', edgecolor=colors['storage'], linewidth=2)
ax.add_patch(storage_box)
ax.text(50, 23, 'Storage Layer / 存储层', fontsize=13, fontweight='bold', 
        ha='center', va='center', color=colors['storage'])

# 存储层级
storage_tiers = [
    ('Hot Tier\nNVMe SSD\n~100TB', 18, 14, '#D97706'),
    ('Warm Tier\nParallel FS\n~1PB', 40, 14, '#F59E0B'),
    ('Cold Tier\nObject Storage\n~10PB', 62, 14, '#FBBF24'),
    ('Archive\nTape/Cloud\n~100PB', 84, 14, '#FCD34D'),
]

for name, x, y, c in storage_tiers:
    box = FancyBboxPatch((x-9, y-5), 18, 11, boxstyle="round,pad=0.01,rounding_size=0.3",
                         facecolor=c, edgecolor='white', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(x, y+1, name, fontsize=8, fontweight='bold', ha='center', va='center', color='white')

# 存储协议
ax.text(50, 7, 'Protocols: NVMe-oF | GPUDirect Storage | Lustre | Ceph | S3', 
        fontsize=8, ha='center', va='center', color=colors['storage'], style='italic')

# ===== 连接箭头 =====
arrow_style = dict(arrowstyle='->', color='#94A3B8', lw=1.5, connectionstyle='arc3,rad=0')

# 层间连接示意
layer_arrows = [
    ((50, 75), (50, 72), 'API'),
    ((50, 55), (50, 53), 'RDMA'),
    ((50, 28), (50, 26), 'PCIe/NVLink'),
]

for start, end, label in layer_arrows:
    ax.annotate('', xy=end, xytext=start, 
                arrowprops=dict(arrowstyle='<->', color='#64748B', lw=2))

# 图例
legend_y = 2
ax.text(50, legend_y, 'Data Flow: ↑ Northbound (Management) | ↓ Southbound (Compute) | ↔ East-West (Network)', 
        fontsize=8, ha='center', va='center', color='#64748B', style='italic')

plt.tight_layout()
plt.savefig('/workspace/projects/books/智算基石/images/ch05-architecture-overview.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Generated: ch05-architecture-overview.png")
