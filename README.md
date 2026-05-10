<div align="center">

<br/>

<img src="https://raw.githubusercontent.com/Abhay-Maddy/Language-Translator/main/assets/world-map-bg.png" alt="Language Translator Banner" width="100%" style="border-radius: 12px; opacity: 0.9;"/>

<br/><br/>

# 🌐 Language Translator

### *Break every language barrier — instantly.*

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Language%20Translator-34d399?style=for-the-badge&labelColor=060a14)](https://abhay-maddy.github.io/Language-Translator/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-8b5cf6?style=for-the-badge&logo=github&labelColor=060a14)](https://github.com/Abhay-Maddy/Language-Translator)

<br/>

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![MyMemory API](https://img.shields.io/badge/MyMemory-API-06b6d4?style=flat-square&logo=translate&logoColor=white)
![Web Speech API](https://img.shields.io/badge/Web%20Speech-API-34d399?style=flat-square&logo=googlechrome&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-8b5cf6?style=flat-square&logo=github-pages&logoColor=white)

<br/>

</div>

---

## ✨ Overview

**Language Translator** is a dual-platform, production-grade translation suite — a **modern web app** paired with a **Python desktop application**. Powered by the MyMemory Translation API and the native Web Speech API, it delivers real-time translation across **23+ languages** with voice input, audio playback, and an immersive glassmorphism UI.

> Built with pure HTML5, CSS3, and Vanilla JavaScript — no frameworks, no bloat. Just fast, accessible, and beautiful.

---

## 🎯 Features

| Feature | Description |
|---|---|
| ⚡ **Instant Translation** | Auto-translates 800ms after you stop typing — no button press needed |
| 🎤 **Voice-to-Text (STT)** | Continuous speech recognition via Web Speech API (Chrome / Edge) |
| 🔊 **Text-to-Speech (TTS)** | Audio playback for both source and translated text in native locale voices |
| 🔄 **Language Swap** | One-click swap of both languages and text content simultaneously |
| 🌐 **Auto Language Detection** | Detects the input language using Unicode script patterns and Latin word frequency analysis |
| 📋 **One-Click Copy** | Copies the translation to clipboard with visual confirmation |
| ⌨️ **Keyboard Shortcuts** | `Ctrl+Enter` to translate · `Ctrl+S` to swap · `Ctrl+Z` to undo |
| 📊 **Character Counter** | Live count with a 5,000-character limit and warning on approach |
| 🗂️ **Smart Text Chunking** | Breaks long text at sentence boundaries for accurate multi-chunk translation |
| 🖥️ **Desktop App** | Full offline-capable Python / Tkinter desktop version included |
| 📱 **Fully Responsive** | Mobile-first layout — adapts seamlessly from 320px to 4K |
| 🎨 **Glassmorphism UI** | Animated orbs, particle system, world-map background, and neon glow accents |

---

## 🌍 Supported Languages

<div align="center">

| | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 🇬🇧 English | 🇮🇳 Hindi | 🇫🇷 French | 🇩🇪 German | 🇪🇸 Spanish | 🇮🇹 Italian |
| 🇯🇵 Japanese | 🇰🇷 Korean | 🇨🇳 Chinese | 🇸🇦 Arabic | 🇵🇹 Portuguese | 🇷🇺 Russian |
| 🇧🇩 Bengali | 🇮🇳 Tamil | 🇮🇳 Telugu | 🇵🇰 Urdu | 🇹🇷 Turkish | 🇻🇳 Vietnamese |
| 🇹🇭 Thai | 🇳🇱 Dutch | 🇵🇱 Polish | 🇸🇪 Swedish | 🇺🇦 Ukrainian | 🌐 Auto Detect |

</div>

---

## 🖼️ Screenshots

<div align="center">

> **Live Demo →** [abhay-maddy.github.io/Language-Translator](https://abhay-maddy.github.io/Language-Translator/)

</div>

| Web App | Desktop App |
|:---:|:---:|
| Modern glassmorphism dark UI with neon accents | Python / Tkinter desktop with background image |
| Real-time translation, voice I/O, copy & swap | Translate, Clear & Swap buttons with scrollable text areas |

---

## 🏗️ Project Structure

```
Language-Translator/
│
├── index.html              # Web app entry point (semantic HTML5)
│
├── css/
│   └── style.css           # Glassmorphism design system (335 lines of pure CSS)
│
├── js/
│   └── app.js              # Core app logic — translation, STT, TTS, shortcuts
│
├── assets/
│   └── world-map-bg.png    # Background texture asset
│
├── background.jpg           # Desktop app background image
├── translator.py            # Python / Tkinter desktop application
└── README.md
```

---

## 🛠️ Tech Stack

### Web Application

| Layer | Technology |
|---|---|
| **Structure** | HTML5 (semantic, ARIA-compliant) |
| **Styling** | CSS3 — Glassmorphism, CSS Variables, Keyframe Animations, Media Queries |
| **Logic** | Vanilla JavaScript (ES6+) — IIFE module pattern |
| **Translation** | [MyMemory Translated API](https://mymemory.translated.net/) |
| **Voice Input** | Web Speech API — `SpeechRecognition` |
| **Voice Output** | Web Speech API — `SpeechSynthesisUtterance` |
| **Fonts** | Google Fonts — Inter & Poppins |
| **Deployment** | GitHub Pages |

### Desktop Application

| Layer | Technology |
|---|---|
| **Language** | Python 3 |
| **GUI** | Tkinter + ttk |
| **Translation** | `deep-translator` (GoogleTranslator) |
| **Image** | Pillow (`PIL`) |

---

## 🚀 Getting Started

### Web App

No build step required. Simply open `index.html` in any modern browser, or use a local development server:

```bash
# Clone the repository
git clone https://github.com/Abhay-Maddy/Language-Translator.git
cd Language-Translator

# Serve locally (any method works)
npx serve .
# or
python -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

> 💡 **Voice features require Chrome or Edge** — Firefox does not support the Web Speech API.

---

### Desktop App

```bash
# 1. Create & activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install deep-translator Pillow

# 3. Run the app
python translator.py
```

> Ensure `background.jpg` is in the same directory as `translator.py`.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + Enter` | Force translate immediately |
| `Ctrl + S` | Swap source and target languages |
| `Ctrl + Z` | Undo last input (native textarea) |
| `Ctrl + A` | Select all text in focused area |

---

## 📱 Responsive Design

The web app is built **mobile-first** with three responsive breakpoints:

| Breakpoint | Behaviour |
|---|---|
| `> 768px` | Side-by-side panel layout, full shortcuts bar visible |
| `≤ 768px` | Panels stack vertically, voice label hidden, full-width buttons |
| `≤ 480px` | Compact mode — font scales to 14px, shortcuts bar hidden, copy label hidden |

---

## 🔭 Future Enhancements

- [ ] 🕐 **Translation History** — session-based history panel with re-translation support
- [ ] 🌙 **Light / Dark Theme Toggle** — user-controlled theme preference with `localStorage` persistence
- [ ] 📄 **File Translation** — drag-and-drop `.txt` and `.pdf` file translation
- [ ] 🔌 **Offline Mode** — PWA support with service workers for cached operation
- [ ] 🌐 **Extended Language Pack** — expand to 100+ languages via LibreTranslate fallback
- [ ] 📊 **Usage Analytics Dashboard** — track most-used language pairs

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/<your-username>/Language-Translator.git

# 3. Create a feature branch
git checkout -b feat/your-feature-name

# 4. Commit your changes
git commit -m "feat: add your feature description"

# 5. Push and open a Pull Request
git push origin feat/your-feature-name
```

> Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 👨‍💻 Developers

<div align="center">

| | |
|:---:|:---:|
| [![Abhay-Maddy](https://github.com/Abhay-Maddy.png?size=80)](https://github.com/Abhay-Maddy) | [![ArShx17](https://github.com/ArShx17.png?size=80)](https://github.com/ArShx17) |
| **[Abhay-Maddy](https://github.com/Abhay-Maddy)** | **[ArShx17](https://github.com/ArShx17)** |
| Frontend · Desktop App | Frontend · UI Design |

</div>

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">

<br/>

*Crafted with ♥ by [Aryan](https://github.com/ArShx17) & [Abhay](https://github.com/Abhay-Maddy)*

<br/>

[![Live Demo](https://img.shields.io/badge/Try%20it%20Live-34d399?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=060a14)](https://abhay-maddy.github.io/Language-Translator/)
&nbsp;
[![Star on GitHub](https://img.shields.io/badge/⭐%20Star%20on%20GitHub-8b5cf6?style=for-the-badge&logo=github&logoColor=white&labelColor=060a14)](https://github.com/Abhay-Maddy/Language-Translator)

<br/>

</div>
