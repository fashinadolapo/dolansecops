export class WebSocketManager {
    ws: WebSocket | null = null;

    constructor(private url: string) {}

    connect(onMessage: (data: any) => void) {
        this.ws = new WebSocket(this.url);
        this.ws.onopen = () => console.log("WebSocket connected");
        this.ws.onmessage = (event) => onMessage(JSON.parse(event.data));
        this.ws.onclose = () => console.log("WebSocket disconnected");
        this.ws.onerror = (err) => console.error("WebSocket error", err);
    }

    send(message: any) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(message));
        }
    }
}
