from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def chatroom():
    return """
    <html>
    <head>
        <title>Chatroom</title>
    </head>
    <body>
        <h1>Welcome to the Chatroom</h1>
        <div id="chat"></div>
        <input type="text" id="message" placeholder="Type a message..." onkeyup="sendMessage(event)">
        <script>
            function sendMessage(event) {
                if (event.key === 'Enter') {
                    const message = document.getElementById('message').value;
                    document.getElementById('message').value = '';
                    const chat = document.getElementById('chat');
                    chat.innerHTML += '<p>' + message + '</p>';
                }
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
