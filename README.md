# opencosmos · 观星书院

> AstroVerseDAO 新版官网设计实验 —— 东方书院 × 深空观测站

纯静态站（HTML / CSS / 原生 JS），**零构建、零依赖**，推到 `main` 即可用 GitHub Pages 直接托管。

## 设计语言

- **墨黑宣纸底** `#060608` + 暖纸白字 + 细金线描边
- **竖排汉字**（writing-mode）营造书院楹柱感
- **Canvas 星野**：鼠标视差、星辰闪烁、偶发流星；尊重 `prefers-reduced-motion`
- **五大航向碑牌**：每航向一个专属色，hover 染色 + 竖排透镜名
- **修习机制轨道**：滚动驱动的金色描线生长
- 字体：Noto Serif SC（标题/正文）· Cormorant Garamond（西文）· IBM Plex Mono（数据）

## 本地预览

```bash
# 任意静态服务器均可，例如：
python -m http.server 8000
# 打开 http://localhost:8000
```

## 部署

仓库 Settings → Pages → Source 选 `main` 分支根目录即可。

## License

MIT
