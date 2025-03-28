# 🐵 Ayumu Memory Game

## The Chimp Who Outsmarted Humans

This game is inspired by the famous cognitive research study featuring Ayumu, a chimpanzee at the Primate Research Institute of Kyoto University. Ayumu demonstrated remarkable working memory capabilities that often exceeded those of human adults in rapid memory tasks.

![Ayumu the chimp](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Ai_and_Ayumu_2.jpg/320px-Ai_and_Ayumu_2.jpg)

## 🎮 The Game

Challenge yourself against Ayumu's legendary memory skills! This game recreates the memory test where numbers must be remembered and clicked in ascending order after being briefly displayed.

### How to Play

1. Numbers from 1-9 appear on a grid
2. Memorize their positions during the brief display period
3. After the numbers disappear, click the squares in ascending order (1→2→3...)
4. Progress through increasingly difficult levels
5. One wrong click = Game Over!

### Difficulty Progression

| Level | Grid Size | Numbers | Memorization Time |
|-------|-----------|---------|-------------------|
| 1-2   | 1×2, 2×2 | 1-4     | 2 seconds        |
| 3-4   | 2×3, 2×4 | 1-6/8   | 3 seconds        |
| 5-6   | 3×3, 3×4 | 1-9     | 5 seconds        |
| 7-9   | 4×4, 4×5, 5×5 | 1-9 | 8 seconds       |

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Pygame

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ayumu-memory-game.git

# Navigate to the project directory
cd ayumu-memory-game

# Install required packages
pip install pygame
```

### Running the Game

```bash
python main.py
```

## 🎯 Controls

- **Mouse**: Click the cards in ascending order
- **Space**: Start new game/Continue to next level
- **ESC**: Quit game

## 🧠 The Science Behind It

In the original study, Ayumu consistently outperformed humans in memory tasks, particularly when the display time was reduced to 0.21 seconds! This game is designed to help you train your working memory and perhaps even approach Ayumu's remarkable capabilities.

### Research Reference
> Inoue, S., & Matsuzawa, T. (2007). Working memory of numerals in chimpanzees. Current Biology, 17(23), R1004-R1005.

## 🛠️ Technical Details

Built with:
- Python 3
- Pygame
- Love for cognitive science 🧪

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests! Some ideas for improvements:
- Add sound effects
- Implement high score system
- Add more challenging levels
- Create different game modes

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Ayumu and the research team at Kyoto University
- The primate research community for their fascinating work
- The Pygame community

---
*Remember: If a chimp can do it, so can you! (Maybe...)*
