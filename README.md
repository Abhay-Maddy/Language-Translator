<div align="center">

<img src="./assets/banner.png" alt="Language Translator" width="100%" />

<br />
<br />

<a href="https://abhay-maddy.github.io/Language-Translator/">
  <img src="https://img.shields.io/badge/Live%20Demo-%E2%86%92-34d399?style=for-the-badge&labelColor=0d1117" alt="Live Demo" />
</a>
&nbsp;
<a href="https://github.com/Abhay-Maddy/Language-Translator">
  <img src="https://img.shields.io/badge/GitHub%20Repo-%E2%86%92-8b5cf6?style=for-the-badge&logo=github&labelColor=0d1117" alt="GitHub" />
</a>

<br />
<br />

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/MyMemory_API-06b6d4?style=flat-square&logoColor=white" />
<img src="https://img.shields.io/badge/Deployed_on-GitHub_Pages-8b5cf6?style=flat-square&logo=github&logoColor=white" />

<br />
<br />

> **Translate instantly across 23+ languages** — with voice input, text-to-speech, auto-detection, and a premium glassmorphism interface. Zero dependencies. Pure web.

<br />

</div>

---

## Features

```
⚡  Real-time translation   800ms debounce — translates as you type
🎤  Voice Input            Continuous speech recognition (Chrome / Edge)
🔊  Text-to-Speech         Native locale voices for both panels
🔄  Language Swap          Swaps languages + text with one click
🌐  Auto-Detection         Unicode script patterns + Latin word frequency
📋  One-Click Copy         Clipboard copy with animated confirmation
⌨️  Keyboard Shortcuts     Ctrl+Enter · Ctrl+S · Ctrl+Z
📊  Character Counter      Live count, 5 000-char limit with overflow warning
🗂️  Smart Chunking         Splits long text at sentence boundaries
🖥️  Desktop App            Offline-capable Python / Tkinter version
📱  Fully Responsive       Mobile-first — 320 px → 4K
```

---

## Supported Languages

<div align="center">

🇬🇧 English &nbsp;·&nbsp; 🇮🇳 Hindi &nbsp;·&nbsp; 🇫🇷 French &nbsp;·&nbsp; 🇩🇪 German &nbsp;·&nbsp; 🇪🇸 Spanish &nbsp;·&nbsp; 🇮🇹 Italian &nbsp;·&nbsp; 🇯🇵 Japanese &nbsp;·&nbsp; 🇰🇷 Korean
🇨🇳 Chinese &nbsp;·&nbsp; 🇸🇦 Arabic &nbsp;·&nbsp; 🇵🇹 Portuguese &nbsp;·&nbsp; 🇷🇺 Russian &nbsp;·&nbsp; 🇧🇩 Bengali &nbsp;·&nbsp; 🇮🇳 Tamil &nbsp;·&nbsp; 🇮🇳 Telugu &nbsp;·&nbsp; 🇵🇰 Urdu
🇹🇷 Turkish &nbsp;·&nbsp; 🇻🇳 Vietnamese &nbsp;·&nbsp; 🇹🇭 Thai &nbsp;·&nbsp; 🇳🇱 Dutch &nbsp;·&nbsp; 🇵🇱 Polish &nbsp;·&nbsp; 🇸🇪 Swedish &nbsp;·&nbsp; 🇺🇦 Ukrainian &nbsp;·&nbsp; 🌐 Auto Detect

</div>

---

## Tech Stack

| Layer | Web App | Desktop App |
|---|---|---|
| **Language** | HTML5 · CSS3 · JS (ES6+) | Python 3 |
| **UI** | Vanilla CSS — Glassmorphism | Tkinter + ttk |
| **Translation** | MyMemory Translated API | deep-translator (Google) |
| **Voice** | Web Speech API | — |
| **Fonts** | Inter · Poppins (Google Fonts) | — |
| **Deploy** | GitHub Pages | Local / .exe |

---

## Project Structure

```
Language-Translator/
├── index.html              # App shell — semantic HTML5, ARIA labels
├── css/
│   └── style.css           # Design system — variables, glass, animations
├── js/
│   └── app.js              # Core logic — translation, STT, TTS, shortcuts
├── assets/
│   ├── world-map-bg.png    # World map texture (background layer)
│   └── banner.png          # Repository banner
├── background.jpg          # Desktop app background
└── translator.py           # Python Tkinter desktop application
```

---

## Getting Started

### Web App

```bash
git clone https://github.com/Abhay-Maddy/Language-Translator.git
cd Language-Translator

# Any static server works
npx serve .
# or
python -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) — **voice features require Chrome or Edge.**

### Desktop App

```bash
# Install dependencies
pip install deep-translator Pillow

# Run
python translator.py
```

---

## Keyboard Shortcuts

| Keys | Action |
|---|---|
| `Ctrl` + `Enter` | Force translate immediately |
| `Ctrl` + `S` | Swap source ↔ target language |
| `Ctrl` + `Z` | Undo last input |
| `Ctrl` + `A` | Select all text in focused area |

---

## Responsive Breakpoints

| Viewport | Behaviour |
|---|---|
| `> 768px` | Side-by-side panels · full shortcuts bar |
| `≤ 768px` | Stacked panels · full-width buttons |
| `≤ 480px` | Compact mode · shortcuts bar hidden |

---

## Roadmap

- [ ] Translation history panel
- [ ] Light / dark theme toggle
- [ ] Drag-and-drop file translation (`.txt`, `.pdf`)
- [ ] PWA / offline mode via service workers
- [ ] Expanded language support (100+)

---

## Contributing

```bash
# 1. Fork → Clone
git clone https://github.com/<your-username>/Language-Translator.git

# 2. Branch
git checkout -b feat/your-feature

# 3. Commit (Conventional Commits)
git commit -m "feat: your feature description"

# 4. Push → Pull Request
git push origin feat/your-feature
```

---

## Authors

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Abhay-Maddy">
        <img src="https://github.com/Abhay-Maddy.png" width="72" style="border-radius:50%" /><br />
        <sub><b>Abhay-Maddy</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ArShx17">
        <img src="https://github.com/ArShx17.png" width="72" style="border-radius:50%" /><br />
        <sub><b>ArShx17</b></sub>
      </a>
    </td>
  </tr>
</table>

</div>

---

## License

Released under the [MIT License](LICENSE).

---

<div align="center">

Made with ♥ by [Abhay-Maddy](https://github.com/Abhay-Maddy) & [ArShx17](https://github.com/ArShx17)

<br />

<a href="https://abhay-maddy.github.io/Language-Translator/">
  <img src="https://img.shields.io/badge/Try%20it%20Live-34d399?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0d1117" />
</a>
&nbsp;
<a href="https://github.com/Abhay-Maddy/Language-Translator">
  <img src="https://img.shields.io/badge/%E2%AD%90%20Star%20on%20GitHub-8b5cf6?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117" />
</a>

</div>
