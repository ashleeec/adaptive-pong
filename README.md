# 🎮 Smart Pong

**Smart Pong** is a Python-based arcade game inspired by the classic Pong — with a twist. The CPU opponent adapts its performance dynamically based on the score difference, making it easier or harder depending on how well you’re doing.

This is my **first graphics project** and my **first project using pygame** — built from the ground up to explore game development concepts like animation, collision detection, and state management in Python.

---

## 🚀 Features

- 🎯 Player vs. CPU gameplay
- 🧠 **Adaptive difficulty**: CPU becomes more/less accurate based on the score difference
- ⌨️ Keyboard controls (W and S)
- 🎨 Clear UI with 3 game states:
  - Start screen
  - Active gameplay
  - Game over screen
- 🏆 Win condition: first to 5 points

---

## Video Demo
<div>
    <a href="https://www.loom.com/share/688100828451471fa82888850423cb67">
    </a>
    <a href="https://www.loom.com/share/688100828451471fa82888850423cb67">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/688100828451471fa82888850423cb67-5cbdcb5f8664e248-full-play.gif">
    </a>
  </div>

---

## 🕹️ How to Play

1. Make sure you have Python 3 and [pygame](https://www.pygame.org/) installed:
   ```bash
   pip install pygame

2. Run the game
python smart_pong.py

3. Controls:
    W      - Move paddle up
    S      - Move paddle down
    SPACE  - Start the game
    R      - Restart the game after game over

---

## 🧠 How Adaptive CPU Works
The CPU paddle’s reaction time is determined by a `cpu_focus` value that adjusts based on the score difference:

- If the CPU is winning, it becomes less accurate (adds random error).
- If the CPU is losing, it tries harder to block the ball.

The initial difficulty of the CPU is randomized each game, and as you play, it will adapt to your abilities to guarentee a tight match.

---

## Lessons Learned
- Working with pygame for rendering and animations
- Managing game states and event loops
- Implementing basic physics (ball bounces and collisions)
- Using randomness to simulate realistic AI behavior

---

## Built With
- Python 3
- pygame library

