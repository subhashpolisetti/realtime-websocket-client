
# WebSocket Client-Server Interface for Real-time Communication

This project demonstrates a WebSocket-based real-time communication system with a client-server setup and a basic user interface. The client sends 10,000 messages to the server, which responds to each message, showcasing efficient, long-lasting, full-duplex communication.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Running the Application](#running-the-application)
   - [Start the Server](#start-the-server)
   - [Run the Client](#run-the-client)
   - [Launch the UI](#launch-the-ui)
5. [Project Structure](#project-structure)
6. [How It Works](#how-it-works)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

This project uses WebSockets to facilitate real-time communication between a client and a server, demonstrating the benefits of WebSocket's full-duplex connection for applications requiring continuous data exchange.

## Features

- **Full-duplex communication**: Both client and server can send and receive messages simultaneously.
- **Efficient message handling**: Test with 10,000 messages to ensure no messages are dropped.
- **Basic UI**: A Tkinter-based graphical user interface for user interactions.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python installed.
- **WebSocket Library**: Install the WebSocket library to run the server and client applications.
  
  ```bash
  pip install websocket-client
  ```

### Installation

1. Clone this repository.
   
   ```bash
   git clone https://github.com/yourusername/websocket-client-server.git
   cd websocket-client-server
   ```

2. Install the necessary packages:
   
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Start the Server

The server listens for client messages and responds to each, appending a random number to the incoming message.

Run the server:

```bash
python websocketserver.py
```

### Run the Client

The client will send 10,000 messages to the server, receiving and displaying the server’s responses.

Run the client:

```bash
python websocketclient.py
```

### Launch the UI

This application includes a simple Tkinter-based user interface to monitor communication.

To start the UI:

```bash
python websocket_ui.py
```

## Project Structure

- **`websocketserver.py`**: Handles server-side WebSocket connections, processes incoming client messages, and sends responses.
- **`websocketclient.py`**: Connects to the server as a client, sending messages and handling server responses.
- **`websocket_ui.py`**: Provides a graphical interface for users to interact with the WebSocket client-server system.

## How It Works

1. **Connection**: The client establishes a connection to the server using the WebSocket protocol.
2. **Message Exchange**: The client sends 10,000 messages to test the connection, and the server responds to each by appending a random number.
3. **UI Interaction**: The UI allows users to interact with the client-server setup and monitor real-time data exchange.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements.
