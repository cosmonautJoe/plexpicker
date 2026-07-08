# 🎬 PlexPicker

A fast, phone-friendly web app that helps you decide **what to watch next** from your
own [Plex](https://www.plex.tv/) movie library. It pulls your unwatched films, lets you
filter by genre, attention level, and runtime, and pitch the single best
pick for your taste — then lets you queue it, rate it, and find similar titles.

Built as a single self-contained HTML file with a tiny Python server for the home network.

## Features

- **Smart pick** — describe your mood with filters and get one AI-written recommendation
  that references your favorite films by name.
- **🎲 Surprise me** — instant random pick from the filtered shelf, no waiting, works offline.
- **Exclude toggles** — hide animated movies and/or documentaries globally; the setting
  persists between sessions.
- **Library browser** — poster grid with search, watched/unwatched status, genre and
  attention filters.
- **Attention levels** — tag films as *background*, *half*, or *full focus* (great if you
  game or multitask while watching).
- **Queue** — build a watchlist and copy it to your clipboard.
- **Rate & scrobble** — rate a film and it syncs back to Plex as watched.
- **Similar movies** — tap any poster to get AI-picked lookalikes from your own library.
- **Installable PWA** — add it to your iPhone home screen; runs full-screen.
- **🔄 Refresh** — re-pull your library from Plex without restarting the server.

## Tech

- Vanilla HTML / CSS / JavaScript — **no build step, no framework, one file**
- Python standard-library HTTP server (`serve.py`) with an optional system-tray icon
- Plex Media Server REST API
- Anthropic Messages API for the recommendation text

## Running it locally

You need [Plex Media Server](https://www.plex.tv/media-server-downloads/) running on your
network and Python 3.

```bash
python serve.py
```

This serves the app on your local network and prints a URL. Open it in a browser (or on
your phone over the same WiFi) and paste your
[Plex token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)
to connect. Your token is stored only in your browser's local storage — it is never
committed to this repo.

### Configuration

Point the app at your own Plex server by editing one line near the top of the `<script>`
block in [`plex_picker.html`](plex_picker.html):

```js
const PLEX_URL = 'http://192.168.1.50:32400'; // your Plex server's LAN address
```

## A note on hosting

PlexPicker talks **directly** to your Plex server over your local network, so it's
designed to run at home. A public HTTPS site can't reach a home server's `http://`
address (browsers block mixed content), so this is a personal / LAN tool by design rather
than something to deploy for the public web.

## License

[MIT](LICENSE) © Joe Krupnicki
