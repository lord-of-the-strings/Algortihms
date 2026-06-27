import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

array = [-1, 2, 4, -3, 5, 2, -5, 2]
n = len(array)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#f9f9f9')
ax.set_facecolor('#f9f9f9')

bars = ax.bar(range(n), array, color='#d0d0d0', edgecolor='white', linewidth=1.5, width=0.6, zorder=2)

ax.axhline(0, color='#aaaaaa', linewidth=1, zorder=1)
ax.set_xlim(-0.6, n - 0.4)
ax.set_ylim(min(array) - 2.5, max(sum(abs(x) for x in array) // 2 + 2, 15))
ax.set_xticks(range(n))
ax.set_xticklabels([f"[{i}]\n{val:+d}" for i, val in enumerate(array)], fontsize=11)
ax.set_title("Kadane's algorithm", fontsize=16, fontweight='bold', pad=16, loc='left', color='#222222')
ax.tick_params(axis='y', labelsize=10, colors='#666666')
ax.tick_params(axis='x', colors='#333333')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.yaxis.grid(True, color='#e5e5e5', linewidth=0.8, zorder=0)
ax.set_axisbelow(True)

info_box = ax.text(
    0.99, 0.97, "",
    transform=ax.transAxes,
    fontsize=11,
    family='monospace',
    verticalalignment='top',
    horizontalalignment='right',
    color='#222222',
    bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor='#dddddd', linewidth=1)
)

decision_box = ax.text(
    0.01, 0.97, "",
    transform=ax.transAxes,
    fontsize=11,
    family='monospace',
    verticalalignment='top',
    horizontalalignment='left',
    color='#1a5fa8',
    bbox=dict(boxstyle='round,pad=0.6', facecolor='#eef4fd', edgecolor='#b3cff0', linewidth=1)
)

legend_patches = [
    mpatches.Patch(color='#d0d0d0', label='unvisited'),
    mpatches.Patch(color='#f5a623', label='current window'),
    mpatches.Patch(color='#e05c00', label='current element'),
    mpatches.Patch(color='#2a7d32', label='best subarray'),
]
ax.legend(handles=legend_patches, loc='lower right', fontsize=9,
          framealpha=0.9, edgecolor='#cccccc', ncol=2)

state = {
    'current_sum': 0,
    'max_sum': float('-inf'),
    'start': 0,
    'end': 0,
    'temp_start': 0
}

def init():
    for bar in bars:
        bar.set_color('#d0d0d0')
    info_box.set_text("Ready")
    decision_box.set_text("")
    return list(bars) + [info_box, decision_box]

def update(frame):
    for bar in bars:
        bar.set_color('#d0d0d0')

    val = array[frame]
    prev_sum = state['current_sum']

    if prev_sum + val < val:
        state['current_sum'] = val
        state['temp_start'] = frame
        decision = f"start fresh: {val:+d}"
    else:
        state['current_sum'] += val
        decision = f"extend: {prev_sum:+d} + {val:+d} = {state['current_sum']:+d}"

    is_new_max = False
    if state['current_sum'] > state['max_sum']:
        state['max_sum'] = state['current_sum']
        state['start'] = state['temp_start']
        state['end'] = frame
        is_new_max = True

    for i in range(state['temp_start'], frame + 1):
        bars[i].set_color('#f5a623')
    bars[frame].set_color('#e05c00')

    if is_new_max:
        for i in range(state['start'], state['end'] + 1):
            bars[i].set_color('#2a7d32')

    info_box.set_text(
        f"Step {frame + 1}/{n}\n"
        f"Index: {frame}  value: {val:+d}\n"
        f"Window sum: {state['current_sum']:+d}\n"
        f"Best sum:   {state['max_sum']:+d}  (idx {state['start']}–{state['end']})"
    )
    decision_box.set_text(f"Decision: {decision}")

    return list(bars) + [info_box, decision_box]

ani = FuncAnimation(
    fig, update, frames=n, init_func=init,
    blit=False, repeat=False, interval=1500
)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.show(block=True)
