# Public DNS Tool

A simple tool for publishing and monitoring project URLs. Perfect for keeping track of Gradio experiments and other web projects.

## Installation

```bash
pip install -e .
```

## Usage

### Adding a URL
```bash
public-dns add "My Gradio App" "https://12345.gradio.live" --description "My cool experiment"
```

### Listing URLs
```bash
public-dns list
```

### Removing a URL
```bash
public-dns remove "My Gradio App"
```

## Web Interface

The tool includes a web interface that shows all your published URLs with their current status. To access it:

1. Your URLs are stored in `~/.public_dns_tool/urls.json`
2. The static website in the `static/` directory can be deployed to GitHub Pages
3. The page will automatically check URL status when loaded

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT 