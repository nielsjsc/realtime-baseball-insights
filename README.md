# MLB Strategy Explainer

Real-time baseball strategy explanations using Gemini AI and MLB data.

## Description

This project uses Google Cloud's Gemini AI and the MLB Stats API to provide real-time insights into baseball strategy for casual viewers. It connects to the MLB GUMBO live feed via WebSockets, processes the game data, and generates strategic explanations using Gemini.

## Features

*   Real-time game updates via WebSocket connection to MLB GUMBO feed.
*   AI-powered strategic explanations using Google Cloud's Gemini.
*   [Planned] Historical context integration.
*   [Planned] Multi-language support (English, Spanish, Japanese).
*   [Planned] User-friendly interface.

## Technologies Used

*   Python
*   websockets
*   requests
*   Google Cloud Platform (Gemini, Vertex AI)
*   MLB Stats API

## Getting Started

1.  Clone the repository:

    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/mlb-strategy-explainer.git
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate      # On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:

    ```bash
    python src/main.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[Choose a license, e.g., MIT License](https://opensource.org/licenses/MIT)

## Project Structure